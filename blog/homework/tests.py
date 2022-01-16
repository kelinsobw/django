import requests
import pytest
urls = ["http://127.0.0.1:8000/homework_index/?name=fsfghfgh",
        "http://127.0.0.1:8000/homework_index/?name=fsfghfgh",
        "http://127.0.0.1:8000/",
        "http://127.0.0.1:8000/admin",
        "http://127.0.0.1:8000/homework_index_post/"]

@pytest.fixture()
def connect():
    answer=[]
    for url in urls:
        r = (requests.get(url)).status_code
        answer.append(r)
    return(answer)


def test_connect(connect):
    answer_test=[]
    for i in range(len(urls)):
        answer_test.append(200)
    print(answer_test)
    assert connect == answer_test




