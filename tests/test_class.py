from models import models
import requests





class TestClass(object):
    # def test_one(self):
    #     x = "this"
    #     assert 'h' in x
    #
    # def test_two(self):
    #     x = "hello"
    #     assert hasattr(x, 'check')
    def test_new_user(self):
        """
        ADDS a new user and test its username, email, password
        """
        new_user = models.User(username='nickname', email='nickname@gmail.com', password_hash='my_password')
        assert new_user.username == 'nickname'
        assert new_user.email == 'nickname@gmail.com'
        assert new_user.password_hash == 'my_password'

    def test_status_code(self):
        req = requests.get('http://localhost:5000/')
        assert req.status_code == 200







