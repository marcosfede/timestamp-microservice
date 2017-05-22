from apistar.test import TestClient
from project.views import timestamp


def test_timestamp():
    """
    Testing a view directly.
    """
    natural = timestamp("December 15, 2015")
    assert natural == {
        "unix": 1450137600,
        "natural": "December 15, 2015"
    }
    unix = timestamp("1450137600")
    assert unix == {
        "unix": 1450137600,
        "natural": "December 14, 2015"
    }


# def test_http_request():
#     """
#     Testing a view, using the test client.
#     """
#     client = TestClient()
#     response = client.get("/December 15, 2015")
#     assert response.status_code == 200
#     assert response.json() == {
#         "unix": 1450148400,
#         "natural": "December 15, 2015"
#     }
