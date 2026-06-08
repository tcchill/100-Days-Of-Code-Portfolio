from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

# =====================================================
JOB_KW = "brse"
JOB_URL = "https://www.topcv.vn/tim-viec-lam-"
TARGET_URL = f"{JOB_URL}{JOB_KW}/"
# =====================================================

class Scraper:
    def __init__(self):
        # ================================================
        self.jobs = None
        self.chrome_options = Options()
        # self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        # ================================================
        self.wait = WebDriverWait(self.driver, 10)
        # ================================================

    def scrape(self):
        self.driver.get(TARGET_URL)

        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "job-list-search-result"))
        )

        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        job_cards = soup.find_all("div", class_="job-item-search-result")

        jobs = []
        for card in job_cards:
            # Job title
            title = card.find("h3", class_="title")
            title = title.find("span").text.strip() if title else "N/A"

            # Company
            company = card.find("span", class_="company-name")
            company = company.text.strip() if company else "N/A"

            # Salary
            salary = card.find("label", class_="title-salary")
            salary = salary.text.strip() if salary else "N/A"

            # Location
            location = card.find("span", class_="city-text")
            location = location.text.strip() if location else "N/A"

            # Experience
            exp = card.find("label", class_="exp")
            exp = exp.text.strip() if exp else "N/A"

            # Posted date
            posted = card.find("label", class_="label-update")
            if posted:
                # Xóa span "Đăng " đi, chỉ lấy text còn lại
                span = posted.find("span", class_="hidden-on-quick-view")
                if span:
                    span.decompose()  # xóa span khỏi DOM
                posted = posted.get_text(strip=True)
            else:
                posted = "N/A"
            print(posted)

            jobs.append({
                "job_title": title,
                "company": company,
                "salary": salary,
                "location": location,
                "experience": exp,
                "posted_date": posted
            })

        self.jobs = jobs

    def to_df(self):
        # Export CSV
        df = pd.DataFrame(self.jobs)
        df.to_csv(f"{JOB_KW}_jobs.csv", index=False, encoding="utf-8-sig")

# =====================================================
scraper = Scraper()
scraper.scrape()
scraper.to_df()
