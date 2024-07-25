"""LambdaTest API Metadata Class Test"""

from pages.fetch_api_metadata import APImetadata
from conftest import set_test_status


def test_builds_metadata(set_test_status):
    api_metadata = APImetadata()

    builds = api_metadata.fetch_builds_data()
    assert builds.get('status') == 'success', f'Expected \'success\' as value of "status" key'

    if isinstance(builds, dict):
        set_test_status(status="passed", remark="API builds metadata returned")
    else:
        set_test_status(status="failed", remark="API builds metadata not returned")
    assert "Meta" in builds, f"Expected 'Meta' in {builds}"


def test_sessions_metadata(set_test_status):
    api_metadata = APImetadata()

    sessions = api_metadata.fetch_sessions_data()
    assert sessions["data"] is not None, f"Expected {sessions['data']} is not None"

    if isinstance(sessions, dict):
        set_test_status(status="passed", remark="API sessions metadata returned")
    else:
        set_test_status(status="failed", remark="API sessions metadata not returned")
