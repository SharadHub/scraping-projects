# Scraping Projects

A collection of Python web scraping projects built with [Scrapy](https://scrapy.org/) and [Playwright](https://playwright.dev/), covering a range of real-world scraping techniques — from basic HTML parsing to JavaScript-rendered pages, form login, PDF generation, and screenshots.

---

## Projects Overview

| Project | Spider | Target Site | Technique | Output |
|---|---|---|---|---|
| `my_scraper` | `ebook` | books.toscrape.com | Pagination + detail page crawl | CSV / Excel |
| `my_scraper` | `login` | scrapethissite.com | Form-based authentication | Console |
| `my_scraper` | `table` | books.toscrape.com | HTML table parsing | Console |
| `oscars` | `oscar` | scrapethissite.com | Playwright + Ajax/JS click | JSON |
| `pdf` | `pdfs` | docs.scrapy.org | Playwright PDF export | `overview.pdf` |
| `quotes` | `quote` | stealmylogin.com | Playwright form fill & submit | JSON |
| `screenshot` | `screenshot` | quotes.toscrape.com | Playwright screenshot | `oscar.png` |

---

## Requirements

- Python 3.10+
- Google Chrome (required by Playwright)

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/SharadHub/scraping-projects.git
cd scraping-projects
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

Each sub-project shares the same dependencies. Install from the root:

```bash
pip install scrapy scrapy-playwright openpyxl itemloaders
```

### 4. Install Playwright browsers

```bash
playwright install chromium
```

---

## Running the Spiders

Navigate into the sub-project directory first, then run the spider.

### my_scraper

```bash
cd my_scraper
```

| Spider | What it does | Command |
|---|---|---|
| `ebook` | Scrapes travel ebooks (title, price, availability) from books.toscrape.com | `scrapy crawl ebook -o ebooks.csv` |
| `login` | Submits a login form and prints the server response | `scrapy crawl login` |
| `table` | Parses an HTML product table and prints key-value pairs | `scrapy crawl table` |

Supported output formats for `ebook`: `.csv`, `.json`, `.xlsx`

---

### oscars

```bash
cd oscars
scrapy crawl oscar -o movies.json
```

Uses Playwright to click a year button (`2015`) on a JavaScript-rendered page, waits for the Ajax response, then scrapes film titles and award counts.

---

### pdf

```bash
cd pdf
scrapy crawl pdfs
```

Uses Playwright to render the Scrapy documentation overview page and exports it as `overview.pdf` in the current directory.

---

### quotes

```bash
cd quotes
scrapy crawl quote -o quotes.json
```

Uses Playwright to fill and submit a login form, then scrapes the heading and paragraph from the resulting page.

---

### screenshot

```bash
cd screenshot
scrapy crawl screenshot
```

Uses Playwright to visit quotes.toscrape.com and saves a full-page screenshot as `oscar.png` in the current directory.

---

## Project Structure

```
scraping-projects/
├── my_scraper/
│   └── my_scraper/
│       ├── spiders/
│       │   ├── ebook.py       # Travel ebook scraper with detail page crawl
│       │   ├── login.py       # Form-based login demo
│       │   └── table.py       # HTML table parser
│       ├── items.py
│       └── pipelines.py
├── oscars/
│   └── oscars/spiders/
│       └── oscar.py           # Ajax/JS page scraper via Playwright click
├── pdf/
│   └── pdf/spiders/
│       └── pdfs.py            # Webpage to PDF via Playwright
├── quotes/
│   └── quotes/spiders/
│       └── quote.py           # Login form automation via Playwright
└── screenshot/
    └── screenshot/spiders/
        └── screenshots.py     # Full-page screenshot via Playwright
```

---

## License

This project is open source and available under the [MIT License](LICENSE).
