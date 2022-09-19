import os

from utils.sessions import demoqa


def test_add_to_cart_authorized():

    login = os.getenv('user_login')
    password = os.getenv('user_password')
    auth_cookie_name = 'NOPCOMMERCE.AUTH'

    response = demoqa().get('/login', data={
        'Email': login, 'Password': password}, allow_redirects=False)
    auth_cookie_value = response.cookies.get(auth_cookie_name)

    response = demoqa().post(
        '/addproducttocart/catalog/31/1/1',
        cookies={auth_cookie_name: auth_cookie_value}
    )

    print(response.json())
    assert response.status_code == 200
    assert response.json()['success'] is True
    assert response.json()['message'] == 'The product has been added to your <a href=\"/cart\">shopping cart</a>'

