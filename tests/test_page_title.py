from conftest import browser, page, set_test_status
# from conftest import *
from pages.page_title import PageTitle
import pytest


def test_page_title(page, set_test_status):
	page_title = PageTitle(page)

	title = page_title.get_page_title()
    
	if "Your Store" in title:
		set_test_status(status="passed", remark="Title matched")
	else:
		set_test_status(status="failed", remark="Title did not match")
	
	assert title == "Your Store", "Expected page title to be 'Your Store'"
