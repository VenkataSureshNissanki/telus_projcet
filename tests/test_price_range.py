from utils import login

def test_total_between_30_and_60(browser_context):
    page = browser_context
    login(page)

    page.click('button[data-test="add-to-cart-sauce-labs-backpack"]')
    page.click('button[data-test="add-to-cart-sauce-labs-bike-light"]')

    page.click('.shopping_cart_link')
    page.click('button[data-test="checkout"]')
    page.fill('input[data-test="firstName"]', "Jane")
    page.fill('input[data-test="lastName"]', "Smith")
    page.fill('input[data-test="postalCode"]', "54321")
    page.click('input[data-test="continue"]')

    total = page.locator('.summary_subtotal_label').inner_text()
    total_val = float(total.replace('Item total: $', ''))
    assert 30 <= total_val <= 60
    page.click('button[data-test="finish"]')
