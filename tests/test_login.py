from utils import login

def test_login_success(browser_context):
    page = browser_context
    login(page)
    assert "inventory.html" in page.url
