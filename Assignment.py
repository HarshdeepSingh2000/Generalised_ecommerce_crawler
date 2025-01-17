import asyncio
from playwright.async_api import async_playwright
import re
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Regular expressions for product URLs
PRODUCT_PATTERNS = [r"/product/", r"/item/", r"/p/", r"/shop/", r"/buy/"]

def is_product_url(url):
    return any(re.search(pattern, url) for pattern in PRODUCT_PATTERNS)

async def crawl_domain_with_playwright(domain, max_pages=5):
    logging.info(f"Starting crawl for {domain}")
    visited = set()
    to_visit = [domain]  # Start from the given URL
    product_urls = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        while to_visit and len(product_urls) < max_pages:
            url = to_visit.pop(0)
            if url in visited:
                continue
            visited.add(url)

            try:
                await page.goto(url, timeout=30000)
                content = await page.content()

                # Extract all links on the page
                links = page.evaluate(
                    """() => Array.from(document.querySelectorAll('a')).map(a => a.href)"""
                )

                for link in await links:
                    if is_product_url(link):
                        product_urls.append(link)
                    elif link not in visited and domain in link:
                        to_visit.append(link)
            except Exception as e:
                logging.warning(f"Failed to fetch {url}: {e}")

        await browser.close()

    return list(set(product_urls))

async def main(domains):
    results = {}
    for domain in domains:
        results[domain] = await crawl_domain_with_playwright(domain)
    with open("product_urls.json", "w") as f:
        json.dump(results, f, indent=4)
    logging.info("Crawling complete. Results saved to product_urls.json.")

if __name__ == "__main__":
    # List of domains to crawl
    domains = ["https://www.flipkart.com/search?q=iphone","https://www.flipkart.com/search?q=realme+5g+mobile&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=realme+5g+mobile%7CMobiles&requestId=e821789f-8dbe-43d7-8a8c-86c5533eb53b&as-searchtext=Re"]
    asyncio.run(main(domains))
