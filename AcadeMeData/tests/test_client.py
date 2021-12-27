from AcadeMe import views


def test_homepage(client):
    assert response.status_code == 200

def test_homepage_html(client):
    request = client.get('')
    response = views.homePage(request)
    expected_html = render_to_string('landing/homepage.html', request=request)
    assert response.content.decode() == expected_html

def test_contactus(client):
    request = client.get('contact_us/')
    response = views.contact(request)
    assert response.status_code == 200
