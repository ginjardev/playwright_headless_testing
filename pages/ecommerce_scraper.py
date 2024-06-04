# LambdaTest ecommerce playground web scraper
import time

class EcommerceScraper:

    def __init__(self, page):
        self.page = page
        self.page.goto("https://ecommerce-playground.lambdatest.io/")
        

    def select_product_category(self):
        self.page.get_by_role("button", name="Shop by Category").click()
        self.page.wait_for_load_state()
        self.page.get_by_role("link", name="Laptops & Notebooks").click()
    

    def scroll_down_page(self):
        for _ in range(5):
            self.page.mouse.wheel(0, 400)
            time.sleep(1)
        self.page.screenshot(path="take.png", full_page=True)
            

    def page_title(self):
        return self.page.title()

    def product_title_grid_list(self):
        self.page.wait_for_load_state("domcontentloaded")
        return (
            self.page.locator("#entry_212408 div")
            .locator(".product-grid div")
            .locator(".caption")
            .locator(".title")
            .all_inner_texts()
        )

    def product_price_grid_list(self):
        self.page.wait_for_load_state("domcontentloaded")
        return (
            self.page.locator("#entry_212408 div")
            .locator(".product-grid div")
            .locator(".caption")
            .locator(".price")
            .all_inner_texts()
        )

    def product_image_grid_list(self):
        self.page.wait_for_load_state("domcontentloaded")
        self.scroll_down_page()
        images = (
            self.page.locator("#entry_212408 div")
            .locator(".product-grid div")
            .locator(".product-thumb-top")
            .locator(".image .carousel-inner")
            .locator(".active > img")
        )
        links = []
        for i in images.all():
            links.append(i.get_attribute("src"))
        
        return links
    

    def display_scraped_product_details(self):
        prices = self.product_price_grid_list()
        product_names = self.product_title_grid_list()
        product_image_links = self.product_image_grid_list()
        
        details_zip = zip(product_image_links, product_names, prices)
        
        details_list = list(details_zip)
        result = []
        for item in details_list:
            result.append({"image link": item[0], "product name": item[1], "product price": item[2]})
        return result
            
        

            
            
