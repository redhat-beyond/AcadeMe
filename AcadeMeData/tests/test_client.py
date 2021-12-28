from AcadeMe import views


@pytest.mark.django_db
def test_homepage(client):
    request = client.get('')
    response = views.homePage(request)
    assert response.status_code == 200

@pytest.mark.django_db
def test_contactus(client):
    request = client.get('contact_us/')
    response = views.contact(request)
    assert response.status_code == 200
