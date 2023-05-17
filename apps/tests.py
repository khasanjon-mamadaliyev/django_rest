from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory, APIClient
from rest_framework.test import APITestCase
from apps.apiviews import PollViewSet


class TestPoll(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.factory = APIRequestFactory()
        self.view = PollViewSet.as_view({'get': 'list'})
        self.url = '/polls'
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            'test',
            email='testuser@test.com',
            password='test'
        )

    def test_list(self):
        request = self.factory.get(
            self.url,
            HTTP_AUTHORIZATION='Token {}'.format(self.token.key)
        )
        request.user = self.user
        response = self.view(request)

        self.assertEqual(response.status_code, 200,
                         'Excepted Response Code 200, received {0} instead.'.format(response.status_code))

    def test_list2(self):
        self.client.login(username='test', password='test')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200,
                         'Excepted Response Code 200, received {0} instead.'.format(response.status_code))

    def test_create(self):
        self.client.login(username='test', password='test')
        params = {
            "question": "How are you ?",
            "created_by": 1
        }
        response = self.client.post(self.url, params)
        self.assertEqual(response.status_code, 201,
                         'Excepted Response Code 201, received {0} instead.'.format(response.status_code))

        print('Muvaffaqiyatli post qilindi')
