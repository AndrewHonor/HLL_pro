import requests
from bs4 import BeautifulSoup


def get_urls_from_page(page_url):
    try:
        response = requests.get(page_url)
        #response.raise_for_status()  # Перевірка на помилки
        soup = BeautifulSoup(response.text, 'html.parser')
        urls = []

        for link in soup.find_all('a', href=True):
            url = link['href']
            if url.startswith('http'):
                urls.append(url)

        return urls

    except requests.RequestException as e:
        #print(f"An error occurred: {e}")
        return []


def collect_urls(start_page_url, num_urls=100):
    collected_urls = []
    to_visit = [start_page_url]

    while to_visit and len(collected_urls) < num_urls:
        current_page = to_visit.pop(0)
        urls = get_urls_from_page(current_page)

        for url in urls:
            if url not in collected_urls:
                collected_urls.append(url)
                if len(collected_urls) >= num_urls:
                    break
            if url not in to_visit:
                to_visit.append(url)

    return collected_urls[:num_urls]


#start_page = 'https://example.com'
#urls = collect_urls(start_page)
#print(urls)
#print(len(urls))


