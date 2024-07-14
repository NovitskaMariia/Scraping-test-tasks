import json

import requests
from bs4 import BeautifulSoup


class EbayScraper:
    """
    This class is used to parse the content of a given eBay URL.
    It retrieves the page content using the requests library and
    parses the HTML content using BeautifulSoup. The parsed data includes
    product URL, product title, price, image URLs, seller information, and shipping price.
    """

    def __init__(self, url):
        self.url = url

    def get_page_content(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching page content: {e}")
            return None

    def parse_content(self, html_content):
        if html_content:
            soup = BeautifulSoup(html_content, "html.parser")

            title = soup.find("h1", {"class": "x-item-title__mainTitle"})
            price = soup.select_one("div.x-price-primary > span.ux-textspans")
            images = soup.find_all("div", class_="ux-image-carousel-item")
            image_urls = []
            for element in images:
                img_tag = element.find("img")
                if img_tag:
                    img_url = (
                        img_tag.get("data-zoom-src")
                        or img_tag.get("data-src")
                        or img_tag.get("src")
                    )
                    if img_url:
                        image_urls.append(img_url)
            seller = soup.select_one("div.x-sellercard-atf__info__about-seller")
            shipping_price = soup.select_one(
                "div.ux-labels-values__values span.ux-textspans--SECONDARY"
            )
            if not shipping_price or (
                "EUR" not in shipping_price.get_text()
                or "$" not in shipping_price.get_text()
            ):
                shipping_price = soup.select_one(
                    "div.ux-layout-section__textual-display--shippingError span.ux-textspans--BOLD"
                )
            print(shipping_price)

            data = {}
            data["url"] = self.url
            data["title"] = title.text.strip() if title else None
            data["price"] = price.text.strip() if price else None
            data["image_urls"] = list(set(image_urls))
            if seller and seller.get("title"):
                data["seller"] = seller["title"]
            else:
                seller_span = soup.select_one(
                    "div.x-sellercard-atf__info__about-seller + ul li span.ux-textspans"
                )
                data["seller"] = (
                    seller_span.get_text(strip=True).split()[0] if seller_span else None
                )
            data["shipping_price"] = (
                shipping_price.get_text(strip=True) if shipping_price else None
            )
            return data

    def save_to_json(self, data):
        ask_filename = input("Enter the filename to save the data: ")
        filename = ask_filename + ".json"
        self.filename = filename
        if data:
            with open(filename, "w") as f:
                json.dump(data, f, indent=4)

    def scrape(self):
        page_content = self.get_page_content()
        if page_content:
            data = self.parse_content(page_content)
            self.save_to_json(data)
            print(f"Data saved to {self.filename}")
        else:
            print("Failed to fetch page content.")


if __name__ == "__main__":
    url = input("Enter the eBay product URL: ")
    scraper = EbayScraper(url)
    scraper.scrape()
