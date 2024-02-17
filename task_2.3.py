import os
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import pdfkit

def save_as_pdf(url, folder):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.find('title').text

    path = os.path.join(folder, f"{title}.pdf")

    pdfkit.from_url(url, path)

def scrape_and_save_all_pages(base_url, folder):
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    links = soup.find_all('a')

    with ThreadPoolExecutor() as executor:
        for link in links:
            url = link.get('href')
            if url:

                url = urljoin(base_url, url)

                executor.submit(save_as_pdf, url, folder)

base_url = "https://www.tilshunos.com/paronims/"
folder = "paronims"

scrape_and_save_all_pages(base_url, folder)