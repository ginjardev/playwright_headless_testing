class ProductPageTitle:

    def __init__(self, page):
        self.page = page
        self.page.goto("https://ecommerce-playground.lambdatest.io/")

    def navigate_product_page(self):
        self.page.get_by_role("link", name="Palm Treo Pro", exact=True).click()

    def get_product_page_title(self):
        return self.page.title()
