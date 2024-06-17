"""APIScraper Class Test"""

from pages.api_scraper import APIScraper
from conftest import browser, page, set_test_status


def test_api_doc_scraper(page, set_test_status):
    api_scraper = APIScraper(page)

    api_scraper.authorise_api_doc()
    api_scraper.fetch_builds_data()
    result = api_scraper.scrape_builds_data()

    print(result)

    if isinstance(result, str):
        set_test_status(status="passed", remark="API meta data scraped")
    else:
        set_test_status(status="failed", remark="API meta data not scraped")
    assert "Meta" in result, f"Expected 'Meta' in {result}"
    assert (
        '"status": "success"' in result
    ), f'Expected \'"status": "success"\' in {result}'
