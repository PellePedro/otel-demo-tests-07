import json  # noqa: F401


def test_h11_9siqt8tojo_x2_isk_0001(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'ISK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ISK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x3_jpy_0002(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'JPY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "JPY"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x4_krw_0003(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'KRW', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "KRW"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x5_mxn_0004(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'MXN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MXN"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x10_myr_0005(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'MYR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MYR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x1_nok_0006(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'NOK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NOK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x2_nzd_0007(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'NZD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NZD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x3_php_0008(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'PHP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PHP"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x4_pln_0009(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'PLN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PLN"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x5_ron_0010(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'RON', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RON"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_9siqt8tojo_x10_rub_0011(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'RUB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RUB"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x1_sek_0012(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'SEK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SEK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x2_sgd_0013(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'SGD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SGD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x3_thb_0014(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'THB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "THB"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x4_try_0015(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'TRY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "TRY"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x5_usd_0016(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'USD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "USD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x10_zar_0017(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'ZAR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ZAR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x1_aud_0018(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'AUD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "AUD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x2_bgn_0019(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'BGN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BGN"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x3_brl_0020(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'BRL', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BRL"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_9siqt8tojo_x4_cad_0021(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CAD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CAD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x5_chf_0022(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CHF', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CHF"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x10_cny_0023(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'CNY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CNY"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x1_czk_0024(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CZK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CZK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x2_dkk_0025(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'DKK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "DKK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x3_eur_0026(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'EUR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "EUR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x4_gbp_0027(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'GBP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "GBP"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x5_hkd_0028(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'HKD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HKD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x10_hrk_0029(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'HRK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HRK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x1_huf_0030(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'HUF', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HUF"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_9siqt8tojo_x2_idr_0031(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'IDR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "IDR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x3_ils_0032(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'ILS', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ILS"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x4_inr_0033(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'INR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "INR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x5_isk_0034(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'ISK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ISK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x10_jpy_0035(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'JPY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "JPY"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x1_krw_0036(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'KRW', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "KRW"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x2_mxn_0037(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'MXN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MXN"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x3_myr_0038(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'MYR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MYR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x4_nok_0039(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'NOK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NOK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x5_nzd_0040(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'NZD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NZD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_9siqt8tojo_x10_php_0041(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'PHP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PHP"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x1_pln_0042(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'PLN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PLN"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x2_ron_0043(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'RON', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RON"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x3_rub_0044(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'RUB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RUB"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x4_sek_0045(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'SEK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SEK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x5_sgd_0046(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'SGD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SGD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x10_thb_0047(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'THB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "THB"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x1_try_0048(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'TRY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "TRY"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x2_usd_0049(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'USD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "USD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x3_zar_0050(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'ZAR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ZAR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_9siqt8tojo_x4_aud_0051(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'AUD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "AUD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x5_bgn_0052(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'BGN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BGN"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x10_brl_0053(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'BRL', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BRL"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x1_cad_0054(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CAD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CAD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x2_chf_0055(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CHF', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CHF"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x3_cny_0056(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CNY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CNY"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x4_czk_0057(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CZK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CZK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x5_dkk_0058(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'DKK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "DKK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x10_eur_0059(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'EUR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "EUR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x1_gbp_0060(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'GBP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "GBP"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_9siqt8tojo_x2_hkd_0061(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'HKD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HKD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x3_hrk_0062(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'HRK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HRK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x4_huf_0063(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'HUF', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HUF"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x5_idr_0064(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'IDR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "IDR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x10_ils_0065(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'ILS', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ILS"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x1_inr_0066(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'INR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "INR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x2_isk_0067(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'ISK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ISK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x3_jpy_0068(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'JPY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "JPY"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x4_krw_0069(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'KRW', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "KRW"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x5_mxn_0070(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'MXN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MXN"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_9siqt8tojo_x10_myr_0071(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'MYR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MYR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x1_nok_0072(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'NOK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NOK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x2_nzd_0073(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'NZD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NZD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x3_php_0074(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'PHP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PHP"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x4_pln_0075(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'PLN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PLN"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x5_ron_0076(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'RON', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RON"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x10_rub_0077(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'RUB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RUB"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x1_sek_0078(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'SEK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SEK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x2_sgd_0079(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'SGD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SGD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x3_thb_0080(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'THB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "THB"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_9siqt8tojo_x4_try_0081(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'TRY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "TRY"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x5_usd_0082(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'USD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "USD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x10_zar_0083(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'ZAR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ZAR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x1_aud_0084(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'AUD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "AUD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x2_bgn_0085(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'BGN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BGN"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x3_brl_0086(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'BRL', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BRL"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x4_cad_0087(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CAD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CAD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x5_chf_0088(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'CHF', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CHF"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x10_cny_0089(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CNY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CNY"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x1_czk_0090(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CZK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CZK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_9siqt8tojo_x2_dkk_0091(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'DKK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "DKK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x3_eur_0092(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'EUR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "EUR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x4_gbp_0093(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'GBP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "GBP"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x5_hkd_0094(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'HKD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HKD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x10_hrk_0095(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'HRK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HRK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x1_huf_0096(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'HUF', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HUF"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x2_idr_0097(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'IDR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "IDR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x3_ils_0098(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'ILS', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ILS"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x4_inr_0099(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'INR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "INR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x5_isk_0100(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'ISK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ISK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_9siqt8tojo_x10_jpy_0101(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'JPY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "JPY"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x1_krw_0102(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'KRW', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "KRW"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x2_mxn_0103(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'MXN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MXN"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x3_myr_0104(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'MYR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MYR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x4_nok_0105(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'NOK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NOK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x5_nzd_0106(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'NZD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NZD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x10_php_0107(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'PHP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PHP"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x1_pln_0108(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'PLN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PLN"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x2_ron_0109(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'RON', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RON"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x3_rub_0110(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'RUB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RUB"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_9siqt8tojo_x4_sek_0111(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'SEK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SEK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x5_sgd_0112(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'SGD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SGD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x10_thb_0113(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'THB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "THB"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x1_try_0114(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'TRY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "TRY"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x2_usd_0115(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'USD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "USD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x3_zar_0116(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'ZAR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ZAR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x4_aud_0117(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'AUD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "AUD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x5_bgn_0118(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'BGN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BGN"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x10_brl_0119(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'BRL', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BRL"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x1_cad_0120(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CAD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CAD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_9siqt8tojo_x2_chf_0121(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CHF', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CHF"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x3_cny_0122(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CNY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CNY"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x4_czk_0123(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'CZK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CZK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x5_dkk_0124(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'DKK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "DKK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x10_eur_0125(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'EUR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "EUR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x1_gbp_0126(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'GBP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "GBP"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x2_hkd_0127(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'HKD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HKD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x3_hrk_0128(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'HRK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HRK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x4_huf_0129(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'HUF', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HUF"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x5_idr_0130(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'IDR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "IDR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_9siqt8tojo_x10_ils_0131(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'ILS', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ILS"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x1_inr_0132(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'INR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "INR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x2_isk_0133(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'ISK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ISK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x3_jpy_0134(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'JPY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "JPY"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x4_krw_0135(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'KRW', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "KRW"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x5_mxn_0136(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'MXN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MXN"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x10_myr_0137(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'MYR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MYR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x1_nok_0138(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'NOK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NOK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x2_nzd_0139(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'NZD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NZD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x3_php_0140(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'PHP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PHP"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_9siqt8tojo_x4_pln_0141(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'PLN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PLN"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x5_ron_0142(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'RON', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RON"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x10_rub_0143(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'RUB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RUB"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x1_sek_0144(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'SEK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SEK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x2_sgd_0145(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'SGD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SGD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x3_thb_0146(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'THB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "THB"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x4_try_0147(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'TRY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "TRY"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x5_usd_0148(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'USD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "USD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x10_zar_0149(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'ZAR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ZAR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x1_aud_0150(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'AUD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "AUD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_9siqt8tojo_x2_bgn_0151(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'BGN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BGN"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x3_brl_0152(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'BRL', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BRL"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x4_cad_0153(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'CAD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CAD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x5_chf_0154(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CHF', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CHF"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x10_cny_0155(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CNY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CNY"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x1_czk_0156(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CZK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CZK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x2_dkk_0157(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'DKK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "DKK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x3_eur_0158(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'EUR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "EUR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x4_gbp_0159(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'GBP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "GBP"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x5_hkd_0160(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'HKD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HKD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_9siqt8tojo_x10_hrk_0161(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'HRK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HRK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x1_huf_0162(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'HUF', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HUF"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x2_idr_0163(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'IDR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "IDR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x3_ils_0164(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'ILS', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ILS"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x4_inr_0165(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'INR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "INR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x5_isk_0166(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'ISK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ISK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x10_jpy_0167(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'JPY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "JPY"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x1_krw_0168(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'KRW', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "KRW"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x2_mxn_0169(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'MXN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MXN"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x3_myr_0170(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'MYR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MYR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_9siqt8tojo_x4_nok_0171(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'NOK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NOK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x5_nzd_0172(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'NZD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NZD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x10_php_0173(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'PHP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PHP"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x1_pln_0174(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'PLN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PLN"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x2_ron_0175(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'RON', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RON"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x3_rub_0176(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'RUB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RUB"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x4_sek_0177(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'SEK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SEK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x5_sgd_0178(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'SGD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SGD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x10_thb_0179(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'THB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "THB"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x1_try_0180(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'TRY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "TRY"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_9siqt8tojo_x2_usd_0181(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'USD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "USD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x3_zar_0182(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'ZAR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ZAR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x4_aud_0183(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'AUD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "AUD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x5_bgn_0184(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'BGN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BGN"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x10_brl_0185(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'BRL', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BRL"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x1_cad_0186(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CAD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CAD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x2_chf_0187(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CHF', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CHF"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x3_cny_0188(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'CNY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CNY"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x4_czk_0189(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CZK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CZK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x5_dkk_0190(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'DKK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "DKK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_9siqt8tojo_x10_eur_0191(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'EUR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "EUR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x1_gbp_0192(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'GBP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "GBP"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x2_hkd_0193(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'HKD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HKD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x3_hrk_0194(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'HRK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HRK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x4_huf_0195(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'HUF', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HUF"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x5_idr_0196(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'IDR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "IDR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x10_ils_0197(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'ILS', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ILS"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x1_inr_0198(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'INR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "INR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x2_isk_0199(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'ISK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ISK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x3_jpy_0200(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'JPY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "JPY"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_9siqt8tojo_x4_krw_0201(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'KRW', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "KRW"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x5_mxn_0202(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'MXN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MXN"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x10_myr_0203(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'MYR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MYR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x1_nok_0204(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'NOK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NOK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x2_nzd_0205(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'NZD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NZD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x3_php_0206(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'PHP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PHP"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x4_pln_0207(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'PLN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PLN"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x5_ron_0208(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'RON', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RON"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x10_rub_0209(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'RUB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RUB"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x1_sek_0210(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'SEK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SEK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_9siqt8tojo_x2_sgd_0211(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'SGD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SGD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x3_thb_0212(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'THB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "THB"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x4_try_0213(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'TRY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "TRY"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x5_usd_0214(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'USD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "USD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x10_zar_0215(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'ZAR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ZAR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x1_aud_0216(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'AUD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "AUD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x2_bgn_0217(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'BGN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BGN"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x3_brl_0218(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'BRL', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BRL"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x4_cad_0219(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CAD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CAD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x5_chf_0220(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CHF', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CHF"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_9siqt8tojo_x10_cny_0221(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CNY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CNY"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x1_czk_0222(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CZK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CZK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x2_dkk_0223(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'DKK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "DKK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x3_eur_0224(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'EUR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "EUR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x4_gbp_0225(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'GBP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "GBP"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x5_hkd_0226(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'HKD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HKD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x10_hrk_0227(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'HRK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HRK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x1_huf_0228(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'HUF', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HUF"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x2_idr_0229(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'IDR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "IDR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x3_ils_0230(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'ILS', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ILS"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_9siqt8tojo_x4_inr_0231(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'INR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "INR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x5_isk_0232(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'ISK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ISK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x10_jpy_0233(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'JPY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "JPY"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x1_krw_0234(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'KRW', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "KRW"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x2_mxn_0235(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'MXN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MXN"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x3_myr_0236(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'MYR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MYR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x4_nok_0237(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'NOK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NOK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x5_nzd_0238(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'NZD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NZD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x10_php_0239(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'PHP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PHP"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x1_pln_0240(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'PLN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PLN"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_9siqt8tojo_x2_ron_0241(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'RON', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RON"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x3_rub_0242(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'RUB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RUB"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x4_sek_0243(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'SEK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SEK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x5_sgd_0244(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'SGD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SGD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x10_thb_0245(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'THB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "THB"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x1_try_0246(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'TRY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "TRY"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x2_usd_0247(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'USD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "USD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x3_zar_0248(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'ZAR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ZAR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x4_aud_0249(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'AUD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "AUD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x5_bgn_0250(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'BGN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BGN"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_9siqt8tojo_x10_brl_0251(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'BRL', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BRL"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x1_cad_0252(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CAD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CAD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x2_chf_0253(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'CHF', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CHF"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x3_cny_0254(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CNY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CNY"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x4_czk_0255(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CZK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CZK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x5_dkk_0256(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'DKK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "DKK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x10_eur_0257(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'EUR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "EUR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x1_gbp_0258(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'GBP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "GBP"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x2_hkd_0259(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'HKD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HKD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x3_hrk_0260(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'HRK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HRK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_9siqt8tojo_x4_huf_0261(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'HUF', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HUF"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x5_idr_0262(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'IDR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "IDR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x10_ils_0263(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'ILS', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ILS"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x1_inr_0264(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'INR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "INR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x2_isk_0265(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'ISK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ISK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x3_jpy_0266(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'JPY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "JPY"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x4_krw_0267(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'KRW', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "KRW"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x5_mxn_0268(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'MXN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MXN"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x10_myr_0269(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'MYR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MYR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x1_nok_0270(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'NOK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NOK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_9siqt8tojo_x2_nzd_0271(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'NZD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NZD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x3_php_0272(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'PHP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PHP"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x4_pln_0273(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'PLN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PLN"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x5_ron_0274(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'RON', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RON"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x10_rub_0275(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'RUB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RUB"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x1_sek_0276(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'SEK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SEK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x2_sgd_0277(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'SGD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SGD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x3_thb_0278(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'THB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "THB"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x4_try_0279(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'TRY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "TRY"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x5_usd_0280(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'USD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "USD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_9siqt8tojo_x10_zar_0281(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'ZAR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ZAR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x1_aud_0282(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'AUD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "AUD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x2_bgn_0283(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'BGN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BGN"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x3_brl_0284(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'BRL', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BRL"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x4_cad_0285(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CAD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CAD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x5_chf_0286(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CHF', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CHF"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x10_cny_0287(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CNY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CNY"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x1_czk_0288(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'CZK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CZK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x2_dkk_0289(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'DKK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "DKK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x3_eur_0290(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'EUR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "EUR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_9siqt8tojo_x4_gbp_0291(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'GBP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "GBP"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x5_hkd_0292(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'HKD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HKD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x10_hrk_0293(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'HRK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HRK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x1_huf_0294(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'HUF', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HUF"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x2_idr_0295(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'IDR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "IDR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x3_ils_0296(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'ILS', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ILS"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x4_inr_0297(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'INR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "INR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x5_isk_0298(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'ISK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ISK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x10_jpy_0299(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'JPY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "JPY"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x1_krw_0300(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'KRW', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "KRW"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_9siqt8tojo_x2_mxn_0301(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'MXN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MXN"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x3_myr_0302(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'MYR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MYR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x4_nok_0303(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'NOK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NOK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x5_nzd_0304(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'NZD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NZD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x10_php_0305(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'PHP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PHP"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x1_pln_0306(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'PLN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PLN"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x2_ron_0307(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'RON', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RON"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x3_rub_0308(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'RUB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RUB"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x4_sek_0309(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'SEK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SEK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x5_sgd_0310(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'SGD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SGD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_9siqt8tojo_x10_thb_0311(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'THB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "THB"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x1_try_0312(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'TRY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "TRY"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x2_usd_0313(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'USD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "USD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x3_zar_0314(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'ZAR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ZAR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x4_aud_0315(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'AUD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "AUD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x5_bgn_0316(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'BGN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BGN"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x10_brl_0317(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'BRL', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BRL"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x1_cad_0318(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'CAD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CAD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x2_chf_0319(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CHF', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CHF"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x3_cny_0320(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CNY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CNY"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []
