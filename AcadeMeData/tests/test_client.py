from AcadeMe import views


def test_homepage(client):
    request = client.get('')
    response = views.homePage(request)
    assert response.status_code == 200


def test_contactus(client):
    request = client.get('contact_us/')
    response = views.contact(request)
    assert response.status_code == 200
