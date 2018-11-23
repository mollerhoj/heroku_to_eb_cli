from application import application

client = application.test_client()

def test_index():
    response = client.get('/')
    assert b'Hello world' in response.data
