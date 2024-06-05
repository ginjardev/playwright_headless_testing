from conftest import playwright_local_grid_page
from conftest import browser, page, set_test_status
from pages.ecommerce_scraper import EcommerceScraper
from playwright.sync_api import expect


def test_product_title_list(page, set_test_status):
    scraper = EcommerceScraper(page)
    scraper.select_product_category()
    product_title_list = scraper.product_title_grid_list()

    if len(product_title_list) == 15:
        set_test_status(status="passed", remark="Product names scraped")
    else:
        set_test_status(status="failed", remark="Product names not scraped")

    assert isinstance(
        product_title_list, list
    ), f"Expected {product_title_list} to be a list"
    assert (
        len(product_title_list) == 15
    ), f"Expected {product_title_list} to contain product names"


def test_product_price_list(page, set_test_status):
    scraper = EcommerceScraper(page)
    scraper.select_product_category()
    product_price_list = scraper.product_price_grid_list()

    if len(product_price_list) == 15:
        set_test_status(status="passed", remark="Product prices scraped")
    else:
        set_test_status(status="failed", remark="Product prices not scraped")

    assert isinstance(
        product_price_list, list
    ), f"Expected {product_price_list} to be a list"
    assert (
        len(product_price_list) == 15
    ), f"Expected {product_price_list} to contain product prices"


def test_product_image_link_list(page, set_test_status):
    scraper = EcommerceScraper(page)
    scraper.select_product_category()
    image_link_list = scraper.product_image_grid_list()

    if len(image_link_list) == 15:
        set_test_status(status="passed", remark="Product-image links scraped")
    else:
        set_test_status(status="failed", remark="Product-image links not scraped")

    assert isinstance(image_link_list, list), f"Expected {image_link_list} to be a list"
    assert (
        len(image_link_list) == 15
    ), f"Expected {image_link_list} to contain product-image links"


def test_product_detail_list(page, set_test_status):
    scraper = EcommerceScraper(page)
    scraper.select_product_category()
    product_detail_list = scraper.display_scraped_product_details()

    print("Scraped Product Details: ", product_detail_list)

    if len(product_detail_list) == 15:
        set_test_status(status="passed", remark="Product names scraped")
    else:
        set_test_status(status="failed", remark="Product names not scraped")

    assert isinstance(
        product_detail_list, list
    ), f"Expected {product_detail_list} to be a list"
    assert isinstance(
        product_detail_list[0], dict
    ), f"Expected {product_detail_list} to be Python dict"
    assert (
        len(product_detail_list) == 15
    ), f"Expected {product_detail_list} to contain product detail dictionary"
