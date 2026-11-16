import json  # noqa: F401


def test_h03_oljcespc7z_rub_0001(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h03_66vchsjnup_sek_0002(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h03_1ymwwn1n4o_sgd_0003(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h03_l9ecav7kim_thb_0004(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "THB"


def test_h03_2zyfj3gm2n_try_0005(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h03_0puk6v6ev0_usd_0006(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "USD"
    assert product["priceUsd"]["units"] == 175
    assert product["priceUsd"]["nanos"] == 0


def test_h03_ls4psxunum_zar_0007(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h03_9siqt8tojo_aud_0008(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h03_6e92zmyyfz_bgn_0009(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h03_hqtgwgpnh4_brl_0010(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h03_oljcespc7z_cad_0011(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h03_66vchsjnup_chf_0012(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h03_1ymwwn1n4o_cny_0013(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h03_l9ecav7kim_czk_0014(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h03_2zyfj3gm2n_dkk_0015(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h03_0puk6v6ev0_eur_0016(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h03_ls4psxunum_gbp_0017(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h03_9siqt8tojo_hkd_0018(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h03_6e92zmyyfz_hrk_0019(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h03_hqtgwgpnh4_huf_0020(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h03_oljcespc7z_idr_0021(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h03_66vchsjnup_ils_0022(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h03_1ymwwn1n4o_inr_0023(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "INR"


def test_h03_l9ecav7kim_isk_0024(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h03_2zyfj3gm2n_jpy_0025(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h03_0puk6v6ev0_krw_0026(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h03_ls4psxunum_mxn_0027(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h03_9siqt8tojo_myr_0028(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h03_6e92zmyyfz_nok_0029(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h03_hqtgwgpnh4_nzd_0030(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h03_oljcespc7z_php_0031(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h03_66vchsjnup_pln_0032(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h03_1ymwwn1n4o_ron_0033(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "RON"


def test_h03_l9ecav7kim_rub_0034(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h03_2zyfj3gm2n_sek_0035(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h03_0puk6v6ev0_sgd_0036(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h03_ls4psxunum_thb_0037(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "THB"


def test_h03_9siqt8tojo_try_0038(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h03_6e92zmyyfz_usd_0039(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "USD"
    assert product["priceUsd"]["units"] == 69
    assert product["priceUsd"]["nanos"] == 950000000


def test_h03_hqtgwgpnh4_zar_0040(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h03_oljcespc7z_aud_0041(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h03_66vchsjnup_bgn_0042(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h03_1ymwwn1n4o_brl_0043(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h03_l9ecav7kim_cad_0044(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h03_2zyfj3gm2n_chf_0045(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h03_0puk6v6ev0_cny_0046(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h03_ls4psxunum_czk_0047(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h03_9siqt8tojo_dkk_0048(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h03_6e92zmyyfz_eur_0049(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h03_hqtgwgpnh4_gbp_0050(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h03_oljcespc7z_hkd_0051(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h03_66vchsjnup_hrk_0052(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h03_1ymwwn1n4o_huf_0053(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h03_l9ecav7kim_idr_0054(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h03_2zyfj3gm2n_ils_0055(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h03_0puk6v6ev0_inr_0056(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "INR"


def test_h03_ls4psxunum_isk_0057(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h03_9siqt8tojo_jpy_0058(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h03_6e92zmyyfz_krw_0059(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h03_hqtgwgpnh4_mxn_0060(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h03_oljcespc7z_myr_0061(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h03_66vchsjnup_nok_0062(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h03_1ymwwn1n4o_nzd_0063(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h03_l9ecav7kim_php_0064(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h03_2zyfj3gm2n_pln_0065(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h03_0puk6v6ev0_ron_0066(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "RON"


def test_h03_ls4psxunum_rub_0067(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h03_9siqt8tojo_sek_0068(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h03_6e92zmyyfz_sgd_0069(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h03_hqtgwgpnh4_thb_0070(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "THB"


def test_h03_oljcespc7z_try_0071(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h03_66vchsjnup_usd_0072(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "USD"
    assert product["priceUsd"]["units"] == 349
    assert product["priceUsd"]["nanos"] == 950000000


def test_h03_1ymwwn1n4o_zar_0073(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h03_l9ecav7kim_aud_0074(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h03_2zyfj3gm2n_bgn_0075(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h03_0puk6v6ev0_brl_0076(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h03_ls4psxunum_cad_0077(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h03_9siqt8tojo_chf_0078(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h03_6e92zmyyfz_cny_0079(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h03_hqtgwgpnh4_czk_0080(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h03_oljcespc7z_dkk_0081(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h03_66vchsjnup_eur_0082(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h03_1ymwwn1n4o_gbp_0083(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h03_l9ecav7kim_hkd_0084(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h03_2zyfj3gm2n_hrk_0085(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h03_0puk6v6ev0_huf_0086(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h03_ls4psxunum_idr_0087(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h03_9siqt8tojo_ils_0088(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h03_6e92zmyyfz_inr_0089(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "INR"


def test_h03_hqtgwgpnh4_isk_0090(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h03_oljcespc7z_jpy_0091(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h03_66vchsjnup_krw_0092(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h03_1ymwwn1n4o_mxn_0093(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h03_l9ecav7kim_myr_0094(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h03_2zyfj3gm2n_nok_0095(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h03_0puk6v6ev0_nzd_0096(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h03_ls4psxunum_php_0097(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h03_9siqt8tojo_pln_0098(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h03_6e92zmyyfz_ron_0099(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "RON"


def test_h03_hqtgwgpnh4_rub_0100(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h03_oljcespc7z_sek_0101(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h03_66vchsjnup_sgd_0102(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h03_1ymwwn1n4o_thb_0103(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "THB"


def test_h03_l9ecav7kim_try_0104(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h03_2zyfj3gm2n_usd_0105(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "USD"
    assert product["priceUsd"]["units"] == 209
    assert product["priceUsd"]["nanos"] == 950000000


def test_h03_0puk6v6ev0_zar_0106(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h03_ls4psxunum_aud_0107(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h03_9siqt8tojo_bgn_0108(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h03_6e92zmyyfz_brl_0109(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h03_hqtgwgpnh4_cad_0110(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h03_oljcespc7z_chf_0111(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h03_66vchsjnup_cny_0112(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h03_1ymwwn1n4o_czk_0113(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h03_l9ecav7kim_dkk_0114(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h03_2zyfj3gm2n_eur_0115(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h03_0puk6v6ev0_gbp_0116(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h03_ls4psxunum_hkd_0117(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h03_9siqt8tojo_hrk_0118(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h03_6e92zmyyfz_huf_0119(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h03_hqtgwgpnh4_idr_0120(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "IDR"
