def test_index(app):
    with app.test_client() as client:
        resp = client.get('/')
        assert resp.status_code == 200

def test_search(app):
    with app.test_client() as client:
        resp = client.get('/search')
        assert resp.status_code == 200

def test_all_books(app):
    with app.test_client() as client:
        resp = client.get('/all-books')
        assert resp.status_code == 200
