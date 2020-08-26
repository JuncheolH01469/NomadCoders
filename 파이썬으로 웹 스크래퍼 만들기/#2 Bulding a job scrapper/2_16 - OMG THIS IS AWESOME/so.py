import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python&sort=i"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)
    # last_page = pages[-2].text
    # last_page = last_page.replace("\n", "").strip()
    return int(last_page)


def extract_job(html):
    title = html.find("h2").text.strip()
    company_location = html.find("h3", {"class": "fc-black-700"})
    company, location = company_location.find_all("span", recursive=False)
    company = company.text.replace("\n", "").strip()
    location = location.text.replace("\n", "").strip()
    job_id = html['data-jobid']
    return {
        'title': title,
        'company': company,
        'location': location,
        'apply_link': f"https://stackoverflow.com/jobs/{job_id}"
    }


def extract_jobs(last_page):
    jobs = []

    for page in range(last_page):
        print(f"Scrapping SO - Page : {page}")
        result = requests.get(f"{URL}&pg={page + 1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})

        for result in results:
            job = extract_job(result)
            jobs.append(job)

    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
