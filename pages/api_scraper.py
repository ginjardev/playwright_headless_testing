"""LambdaTest API scraper Class"""

import os
from dotenv import load_dotenv

load_dotenv("../.env", override=True)


class APIScraper:

    def __init__(self, page):
        self.page = page
        self.page.goto("https://www.lambdatest.com/support/api-doc/")

    # sign in with LambdaTest username & access key to authenticate & authorise API
    def authorise_api_doc(self):
        self.page.frame_locator(".embed-responsive-item >> nth=0").get_by_role(
            "button", name="Authorize"
        ).click()

        # select username input field & fill in LambdaTest username from '.env' file
        self.page.frame_locator(".embed-responsive-item >> nth=0").locator(
            'input[name="username"]'
        ).click()
        self.page.frame_locator(".embed-responsive-item >> nth=0").locator(
            'input[name="username"]'
        ).fill(os.getenv("LT_USERNAME"))

        # select password input field & fill in LambdaTest password from '.env' file
        self.page.frame_locator(".embed-responsive-item >> nth=0").locator(
            'input[name="password"]'
        ).click()
        self.page.frame_locator(".embed-responsive-item >> nth=0").locator(
            'input[name="password"]'
        ).fill(os.getenv("LT_ACCESS_KEY"))

        # click on the authorise button & close modal after
        self.page.frame_locator(".embed-responsive-item >> nth=0").locator(
            "form"
        ).get_by_role("button", name="Authorize").click()
        self.page.frame_locator(".embed-responsive-item >> nth=0").get_by_role(
            "button", name="Close"
        ).click()

    # Enter 'fromdate' parameter to fetch response data
    def fetch_build_data(self):
        # click on Build API endpoint
        self.page.frame_locator(".embed-responsive-item >> nth=0").locator(
            "#operations-Build-builds"
        ).get_by_text("GET").click()
        # click 'Try it out' button
        self.page.frame_locator(".embed-responsive-item >> nth=0").get_by_role(
            "button", name="Try it out"
        ).click()
        # select the 'fromdate' input field and fill in start date
        self.page.frame_locator(".embed-responsive-item >> nth=0").get_by_placeholder(
            "fromdate - To fetch the list"
        ).click()
        self.page.frame_locator(".embed-responsive-item >> nth=0").get_by_placeholder(
            "fromdate - To fetch the list"
        ).fill("2024-05-01")
        # click execute button
        self.page.frame_locator(".embed-responsive-item >> nth=0").get_by_role(
            "button", name="Execute"
        ).click()

    # scrape response body
    def scrape_build_data(self):
        # select the response body locator and extract text
        return (
            self.page.frame_locator(".embed-responsive-item >> nth=0")
            .get_by_text('{ "Meta": { "attributes": { "org_id": 1677164 }')
            .inner_text()
        )
