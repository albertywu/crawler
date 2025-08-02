A basic web crawler in <100 LoC

Run it:
```
❯ uv run crawler.py https://en.wikipedia.org/wiki/Value_theory
Installed 6 packages in 3ms
Crawling https://en.wikipedia.org/wiki/Value_theory (depth=2, max=20 pages)

Crawling: https://en.wikipedia.org/wiki/Value_theory (depth=0)
Crawling: https://en.wikipedia.org/wiki/R._B._Perry (depth=1)
Crawling: https://en.wikipedia.org/wiki/Avicennism (depth=1)
Crawling: https://en.wikipedia.org/wiki/Special:BookSources/978-0-19-090534-7 (depth=1)
Crawling: https://en.wikipedia.org/wiki/Structuralism (depth=1)
Crawling: https://en.wikipedia.org/wiki/Piero_Sraffa (depth=1)
Crawling: https://en.wikipedia.org/wiki/New_Confucianism (depth=1)
Crawling: https://en.wikipedia.org/wiki/Czech_philosophy (depth=1)
Crawling: https://en.wikipedia.org/wiki/Particular (depth=1)
Crawling: https://en.wikipedia.org/wiki/Internalism_and_externalism (depth=1)
Crawling: https://en.wikipedia.org/wiki/Special:BookSources/978-1-5416-4744-2 (depth=1)
Crawling: https://en.wikipedia.org/wiki/Ancient_Roman_philosophy (depth=1)
Crawling: https://en.wikipedia.org/wiki/Special:BookSources/978-0-19-152136-2 (depth=1)
Crawling: https://en.wikipedia.org/wiki/Social_relationships (depth=1)
Crawling: https://en.wikipedia.org/wiki/Wikipedia:Contents (depth=1)
Crawling: https://en.wikipedia.org/wiki/Predicative_expression (depth=1)
Crawling: https://en.wikipedia.org/wiki/David_Hume (depth=1)
Crawling: https://en.wikipedia.org/wiki/Special:BookSources/978-1-009-47674-4 (depth=1)
Crawling: https://en.wikipedia.org/wiki/Ren_(philosophy) (depth=1)
Crawling: https://en.wikipedia.org/wiki/Norm_(philosophy) (depth=1)

Depth 0: 1 pages
  Value theory - Wikipedia (1145 links)

Depth 1: 19 pages
  Ralph Barton Perry - Wikipedia (280 links)
  Avicennism - Wikipedia (613 links)
  Book sources - Wikipedia (1354 links)
  Structuralism - Wikipedia (1140 links)
  Piero Sraffa - Wikipedia (299 links)
  New Confucianism - Wikipedia (1071 links)
  Czech philosophy - Wikipedia (482 links)
  Particular - Wikipedia (139 links)
  Internalism and externalism - Wikipedia (555 links)
  Book sources - Wikipedia (1354 links)
  Ancient Roman philosophy - Wikipedia (343 links)
  Book sources - Wikipedia (1354 links)
  Social relation - Wikipedia (185 links)
  Wikipedia:Contents - Wikipedia (208 links)
  Predicative expression - Wikipedia (117 links)
  David Hume - Wikipedia (3773 links)
  Book sources - Wikipedia (1354 links)
  Ren (philosophy) - Wikipedia (710 links)
  Norm (philosophy) - Wikipedia (390 links)

Total: 20 pages, max depth: 1
```

Run it w/depth & max pages:
```
❯ uv run crawler.py https://en.wikipedia.org/wiki/Value_theory --depth=3 --max-pages=10
Crawling https://en.wikipedia.org/wiki/Value_theory (depth=3, max=10 pages)

Crawling: https://en.wikipedia.org/wiki/Value_theory (depth=0)
Crawling: https://en.wikipedia.org/wiki/Counterfactual_thinking (depth=1)
Crawling: https://en.wikipedia.org/wiki/Special:BookSources/978-0-19-514779-7 (depth=1)
Crawling: https://en.wikipedia.org/wiki/John_Stuart_Mill (depth=1)
Crawling: https://en.wikipedia.org/wiki/Category:Philosophy (depth=1)
Crawling: https://en.wikipedia.org/wiki/Theory_of_forms (depth=1)
Crawling: https://en.wikipedia.org/wiki/Systemics (depth=1)
Crawling: https://en.wikipedia.org/wiki/Special:BookSources/978-0-87840-888-7 (depth=1)
Crawling: https://en.wikipedia.org/wiki/Special:BookSources/978-0-231-54532-7 (depth=1)
Crawling: https://en.wikipedia.org/wiki/Event_(philosophy) (depth=1)

Depth 0: 1 pages
  Value theory - Wikipedia (1145 links)

Depth 1: 9 pages
  Counterfactual thinking - Wikipedia (199 links)
  Book sources - Wikipedia (1354 links)
  John Stuart Mill - Wikipedia (3055 links)
  Category:Philosophy - Wikipedia (322 links)
  Theory of forms - Wikipedia (553 links)
  Systemics - Wikipedia (220 links)
  Book sources - Wikipedia (1354 links)
  Book sources - Wikipedia (1354 links)
  Event (philosophy) - Wikipedia (386 links)

Total: 10 pages, max depth: 1
```
