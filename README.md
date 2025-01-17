# Product URL Crawler for E-commerce Websites

## **Overview**
This project implements a web crawler designed to extract product URLs from e-commerce websites. It uses **Playwright** to handle dynamic JavaScript-rendered content, ensuring that product links are properly identified and extracted. The output is stored in a structured JSON file, mapping each input domain to its discovered product URLs.

---

## **Features**
- **Dynamic Content Handling**: Uses Playwright to render JavaScript-heavy pages.
- **Product URL Filtering**: Identifies product pages using customizable URL patterns.
- **Asynchronous Crawling**: Leverages asynchronous programming for faster execution.
- **Domain-Specific Crawling**: Restricts crawling to the given domain to prevent irrelevant data collection.
- **Configurable Depth**: Limits the number of pages crawled for performance optimization.

---

## **Setup Instructions**

### **1. Install Dependencies**
Ensure you have Python installed (version 3.8 or higher). Then, create a virtual environment and install the required packages:
```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate    # On Windows

# Install dependencies
pip install -r requirements.txt


### **3. Run the Script**
Provide the list of domains or starting URLs in the script and run it:
```bash
python script_name.py
```

---

## **Configuration**

### **Input Domains**
Update the `domains` list in the script to specify the websites you want to crawl:
```python
domains = [
    "https://www.flipkart.com/search?q=iphone",
    "https://www.example.com/shop"
]
```

### **Product URL Patterns**
The crawler identifies product pages using predefined patterns:
```python
PRODUCT_PATTERNS = [
    r"/product/",
    r"/item/",
    r"/p/",
    r"/shop/",
    r"/buy/"
]
```

## **Output**
The script generates a `product_urls.json` file containing the discovered product URLs for each domain. Example:
```json
{
  "https://www.flipkart.com/search?q=iphone": [
    "https://www.flipkart.com/product/12345",
    "https://www.flipkart.com/item/67890"
  ]
}
