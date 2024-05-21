# from conftest import browser, page

class PageTitle:

    def __init__(self, page):
        self.page = page
        self.page.goto("https://ecommerce-playground.lambdatest.io/")

    def get_page_title(self):
        return self.page.title()
