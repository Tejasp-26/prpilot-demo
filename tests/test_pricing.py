from bookstore.pricing import cart_total


def test_cart_total():
    assert cart_total([1.10, 2.20]) == 3.3
