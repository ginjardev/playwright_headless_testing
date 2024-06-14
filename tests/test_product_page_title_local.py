from conftest import playwright_local_grid_page
from pages.product_page_title_local import ProductPageTitle

# using playwright_local_grid_page for local test
def test_product_page_title_local(playwright_local_grid_page):
    pp_title = ProductPageTitle(playwright_local_grid_page)
    pp_title.navigate_product_page()
    title = pp_title.get_product_page_title()
    assert title == "Palm Treo Pro", "Expected 'Palm Treo Pro'"
