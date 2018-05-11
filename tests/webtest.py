from urllib import request


def inc(x):  # one more example
    return x + 1
def d(x):
    return x + 4


class TestClass(object):
    # every test function has to begin : test_
    def test_web_response(self):
        try:
            handler = request.urlopen('http://localhost:5000/')
            code = handler.getcode()
            if code == 200:
                assert True
            else:
                assert False
        except:
            assert False


    def test_simple(self):
        assert True


    def test_answer(self):
        assert inc(3) == 5


    def test_moj(self):
        assert d(5) == 9