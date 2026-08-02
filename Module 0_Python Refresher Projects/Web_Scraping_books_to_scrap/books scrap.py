import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from bs4 import BeautifulSoup
import pandas as pd
import time
from urllib.parse import urljoin


BASE_URL = "http://books.toscrape.com/catalogue/page-1.html"

session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36'
})

retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[500, 502, 503, 504]
)

adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount("http://", adapter)
session.mount("https://", adapter)

RATING_MAP = {
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5
}

def parse_book(book_element, current_url):
    try:
        title_tag = book_element.find('h3').find('a')
        title = title_tag['title'] if title_tag and 'title' in title_tag.attrs else title_tag.text
        
        price_text = book_element.find('p', class_='price_color').text
        price_gbp = float(price_text.replace('£', '').strip())
        
        rating_tag = book_element.find('p', class_='star-rating')
        rating_class = rating_tag['class'][1] if rating_tag else 'Zero'
        rating_int = RATING_MAP.get(rating_class, 0)
        
        availability_text = book_element.find('p', class_='instock availability').text.strip()
        in_stock = "In stock" in availability_text
        
        relative_link = title_tag['href']
        product_url = urljoin(current_url, relative_link)
        
        return {
            'Title': title,
            'Price_GBP': price_gbp,
            'Rating': rating_int,
            'In_Stock': in_stock,
            'Product_URL': product_url
        }
    except (AttributeError, KeyError, ValueError) as e:
        print(f"[!] Error processing book element: {e}")
        return None

all_books = []
current_page_url = BASE_URL
page_count = 1

print("[+] Starting data scraping process...")

while current_page_url:
    print(f"[*] Fetching page {page_count}...")
    try:
        response = session.get(current_page_url, timeout=(3, 5))
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        book_elements = soup.find_all('article', class_='product_pod')
        
        for book_elem in book_elements:
            parsed_data = parse_book(book_elem, current_page_url)
            if parsed_data:
                all_books.append(parsed_data)
                
        next_button = soup.find('li', class_='next')
        if next_button and next_button.find('a'):
            next_relative_url = next_button.find('a')['href']
            current_page_url = urljoin(current_page_url, next_relative_url)
            page_count += 1
            time.sleep(1)
        else:
            print("[+] Reached the end of pagination.")
            current_page_url = None
            
    except requests.exceptions.RequestException as req_err:
        print(f"[-] Network error fetching page {current_page_url}: {req_err}")
        break

if all_books:
    df = pd.DataFrame(all_books)
    
    df['Title'] = df['Title'].astype(str)
    df['Price_GBP'] = df['Price_GBP'].astype(float)
    df['Rating'] = df['Rating'].astype(int)
    df['In_Stock'] = df['In_Stock'].astype(bool)
    
    output_filename = "books_catalog.csv"
    df.to_csv(output_filename, index=False)
    
    print(f"\n[SUCCESS] Completed successfully! Saved {len(df)} books to '{output_filename}'.")
    print(df.head())
else:
    print("[!] No data fetched.")