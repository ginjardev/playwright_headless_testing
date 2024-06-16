"""LambdaTest ecommerce playground web scraper Class"""

import time


class EcommerceScraper:

    def __init__(self, page):
        self.page = page
        self.page.goto("https://ecommerce-playground.lambdatest.io/")

    # navigate to product category to scrape data
    def select_product_category(self):
        self.page.get_by_role("button", name="Shop by Category").click()
        self.page.wait_for_load_state()
        self.page.get_by_role("link", name="Laptops & Notebooks").click()

    # initiate scrolling to make lazy load images visible in viewport
    def scroll_down_page(self):
        # scroll down to lazy load 5 rows of product grid
        for _ in range(5):
            self.page.mouse.wheel(0, 400)
            time.sleep(1)

        # take screenshot to firm downward scroll
        self.page.screenshot(path="screenshot.png", full_page=True)


    # scrape product names/titles
    def product_title_grid_list(self):
        # ensure DOM content is loaded
        self.page.wait_for_load_state("domcontentloaded")

        # scrape product names
        return (
            self.page.locator("#entry_212408 div")
            .locator(".product-grid div")
            .locator(".caption")
            .locator(".title")
            .all_inner_texts()
        )

    def product_price_grid_list(self):
        # ensure DOM content is loaded
        self.page.wait_for_load_state("domcontentloaded")

        # scrape product prices 
        return (
            self.page.locator("#entry_212408 div")
            .locator(".product-grid div")
            .locator(".caption")
            .locator(".price")
            .all_inner_texts()
        )

    def product_image_grid_list(self):
        # ensure DOM content is loaded
        self.page.wait_for_load_state("domcontentloaded")

        # initial downward scroll 
        self.scroll_down_page()

        # scrape product image links
        images = (
            self.page.locator("#entry_212408 div")
            .locator(".product-grid div")
            .locator(".product-thumb-top")
            .locator(".image .carousel-inner")
            .locator(".active > img")
        )

        # append scraped links in a list and return
        links = []
        for i in images.all():
            links.append(i.get_attribute("src"))

        return links

    def display_scraped_product_details(self):
        product_prices = self.product_price_grid_list()
        product_names = self.product_title_grid_list()
        product_image_links = self.product_image_grid_list()

        # match product image, name and price for each item
        details_zip = zip(product_image_links, product_names, product_prices)

        # make a list of the zip object 'details_zip'
        details_list = list(details_zip)

        # convert list of product detail tuple to Python dict
        # append to a list and return same
        result = []
        for item in details_list:
            result.append(
                {
                    "image link": item[0],
                    "product name": item[1],
                    "product price": item[2],
                }
            )
        return result
