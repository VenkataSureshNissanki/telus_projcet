from utils import login

def test_add_3_items_buy_2(browser_context):
    page = browser_context
    login(page)
    
    page.click('button[data-test="add-to-cart-sauce-labs-backpack"]')
    page.click('button[data-test="add-to-cart-sauce-labs-bike-light"]')
    page.click('button[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]')
    
    page.click('.shopping_cart_link')
    page.click('button[data-test="remove-sauce-labs-bolt-t-shirt"]')
    
    page.click('button[data-test="checkout"]')
    page.fill('input[data-test="firstName"]', "John")
    page.fill('input[data-test="lastName"]', "Doe")
    page.fill('input[data-test="postalCode"]', "12345")
    page.click('input[data-test="continue"]')
    page.click('button[data-test="finish"]')

    assert "checkout-complete.html" in page.url
