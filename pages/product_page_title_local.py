class ProductPageTitle:

    def __init__(self, page):
        self.page = page
        self.page.goto("https://ecommerce-playground.lambdatest.io/")
        # self.page.wait_for_load_state()
        # self.page.get_by_role("link", name="Cameras", exact=True).click()
        # self.page.wait_for_load_state()
        # self.page.get_by_role("link", name="Palm Treo Pro", exact=True).click()

    def navigate_product_page(self):
        self.page.get_by_role("link", name="Palm Treo Pro", exact=True).click()

    def get_product_page_title(self):
        return self.page.title()
