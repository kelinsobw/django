import pytest
from django.test import Client


@pytest.mark.django_db
class TestProfiles:
    def test_user_posts(self):
        client = Client()

        response = client.get("/posts/posts_user/3/")
        assert response.status_code == 200

        response = client.get("/posts/posts_user/2/")
        assert response.status_code == 200