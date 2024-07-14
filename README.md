This project consist of two parts: eBay scraper and Country Information Fetcher

# eBay Scraper
## Overview
This script is designed to scrape product details from an eBay product page. It fetches the page content using the requests library and parses the HTML using BeautifulSoup. The parsed data includes the product URL, title, price, image URLs, seller information, and shipping price.
## Requirements
 - Python 3.x
 - requests library
 - beautifulsoup4 library
   You can install the required libraries using pip:
   pip install requests beautifulsoup4
## Usage
 - Save the script to a file, e.g., ebay_scraper.py.
 - Run the script using Python: python ebay_scraper.py
 - Enter the eBay product URL when prompted.
 - Enter the filename to save the scraped data when prompted. The data will be saved as a JSON file with the specified name.
## Example
- $ python ebay_scraper.py
- Enter the eBay product URL: https://www.ebay.com/itm/296246887870
- Enter the filename to save the data: product_data
- Data saved to product_data.json
## Notes
 - Ensure the URL provided is a valid eBay product URL.
 - The script handles cases where certain data might be missing, such as an empty seller title or missing shipping price.

# Country Information Fetcher
## Overview
This script fetches and displays information about a country using the REST Countries API. It retrieves the country's name, capital, and flag URL and displays this information in a table format using the tabulate library.
## Requirements
 - Python 3.x
 - requests library
 - tabulate library
   You can install the required libraries using pip:
   pip install requests tabulate
## Usage
 - Save the script to a file, e.g., country_info.py.
 - Run the script using Python: python country_info.py
 - Enter the valid country name in English when prompted.
 - The script will display the country's name, capital, and flag URL in a formatted table.
