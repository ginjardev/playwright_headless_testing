"""ProductPageTitle Class Test"""

from conftest import playwright_local_page
from pages.product_page_title_local import ProductPageTitle

# using playwright_local_grid_page for local test
def test_product_page_title_local(playwright_local_page):
    product_page_title = ProductPageTitle(playwright_local_page)
    product_page_title.navigate_product_page()
    title = product_page_title.get_product_page_title()
    print(title)
    assert title == "Palm Treo Pro", "Expected 'Palm Treo Pro'"
