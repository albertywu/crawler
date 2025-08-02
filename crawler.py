#!/usr/bin/env -S uv run --quiet
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "requests<3",
#   "click>=8.0",
#   "mypy>=1.8"
# ]
# ///

import click
import requests
import re
from collections import deque, defaultdict
from urllib.parse import urljoin, urlparse
from typing import TypedDict

class NodeMeta(TypedDict):
    depth: int
    title: str
URL = str
Graph = dict[URL, set[URL]]
Nodes = dict[URL, NodeMeta]

def crawl(start_url: URL, max_depth: int = 2, max_pages: int = 20) -> tuple[Graph, Nodes]:
    """BFS web crawler that returns graph and node metadata."""
    graph = {}
    nodes = {}
    visited = set()
    queue = deque([(start_url, 0)])
    base_domain = urlparse(start_url).netloc
    
    while queue and len(visited) < max_pages:
        url, depth = queue.popleft()
        if url in visited or depth > max_depth:
            continue
            
        try:
            print(f"Crawling: {url} (depth={depth})")
            html = requests.get(url, timeout=10).text
            
            # Extract title
            title_match = re.search(r"<title>(.*?)</title>", html, re.I | re.S)
            title = title_match.group(1).strip() if title_match else "No title"
            
            # Extract and filter links
            links = set()
            for href in re.findall(r'href=[\'"]?([^\'" >]+)', html, re.I):
                full_url = urljoin(url, href).split("#")[0]
                
                # Skip non-HTTP(S)
                if not full_url.startswith(('http://', 'https://')):
                    continue
                
                # Skip common non-HTML resources
                if any(full_url.lower().endswith(ext) for ext in ('.jpg', '.png', '.css', '.js', '.svg', '.ico', '.pdf', '.woff')):
                    continue

                links.add(full_url)
        except Exception as e:
            print(f"Error: {url} - {e}")
            title, links = "Error", set()
        
        visited.add(url)
        graph[url] = links
        nodes[url] = {"depth": depth, "title": title}
        
        # Queue same-domain unvisited links
        for link in links:
            if link not in visited and urlparse(link).netloc == base_domain:
                queue.append((link, depth + 1))
    
    return graph, nodes

@click.command()
@click.argument('url')
@click.option('--depth', '-d', default=2, help='Max depth')
@click.option('--max-pages', '-m', default=20, help='Max pages')
def main(url: str, depth: int, max_pages: int) -> None:
    """Simple web crawler using BFS."""
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    print(f"Crawling {url} (depth={depth}, max={max_pages} pages)\n")
    graph, nodes = crawl(url, depth, max_pages)
    
    # Group by depth and print summary
    by_depth = defaultdict(list)
    for url, data in nodes.items():
        by_depth[data['depth']].append((url, data['title'], len(graph.get(url, []))))
    
    for d in sorted(by_depth):
        print(f"\nDepth {d}: {len(by_depth[d])} pages")
        for url, title, links in by_depth[d]:
            print(f"  {title[:50]} ({links} links)")
    
    print(f"\nTotal: {len(nodes)} pages, max depth: {max(by_depth.keys())}")

if __name__ == "__main__":
    main()