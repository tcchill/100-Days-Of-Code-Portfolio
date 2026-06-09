# Day 93 – BrSE Job Market Scraper 🕵️

A Python web scraper that collects live BrSE job listings from TopCV and exports the data to a structured CSV file.

## Features

- Scrapes live job listings from TopCV using Selenium
- Extracts job title, company, salary, location, experience, and posted date
- Exports clean data to CSV with UTF-8 encoding (Excel-compatible)

## Tech Stack

- Python 3
- `selenium` — browser automation for dynamic page rendering
- `beautifulsoup4` — HTML parsing and data extraction
- `pandas` — data structuring and CSV export

## How to Run

**1. Install dependencies**

```bash
pip install -r requirements.txt
```

**2. Run the scraper**

```bash
python main.py
```

Output will be saved as `brse_jobs.csv` in the same directory.

## Sample Output

| job_title | company | salary | location | experience | posted_date |
|---|---|---|---|---|---|
| BrSE - JLPT N3, Max 3000USD | City Ascom Việt Nam | Tới 3,000 USD | Hà Nội | 1 năm | 4 tuần trước |
| Project Manager/BrSE | Reeracoen Việt Nam | 55 - 75 triệu | Hà Nội | Trên 5 năm | 1 tuần trước |

## What I Learned

- Handling JavaScript-rendered pages with Selenium
- Parsing complex nested HTML structures with BeautifulSoup
- Cleaning and structuring scraped data with Pandas
- Identifying and targeting CSS selectors for dynamic web content