# get_job_listings.py
from utils import get_soup

def get_job_listings(url):
    soup = get_soup(url)
    return soup.find_all("a", class_="gb-results-list__item")
