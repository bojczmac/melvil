def test_index(app):
    with app.test_client() as client:
        resp = client.get('/')
        assert resp.status_code == 200

def test_amelinium(app):
    with app.test_client() as client:
        resp = client.get('/amelinium')
        assert resp.status_code == 200

def test_people(app):
    with app.test_client() as client:
        resp = client.get('/people')
        assert resp.status_code == 400
        resp = client.get('/people?n=15')
        assert resp.status_code == 200 and resp.content_type == 'application/json'