from freezegun import freeze_time

from django.contrib.auth.models import User
from django.test import Client, TestCase

from .forms import UserRegisterForm


class TestRegister(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = UserRegisterForm()
        cls.user = User.objects.create(
            username='username',
            email='email@email.com',
        )
        cls.user.set_password('best_password')

    def test_able_get_form_page(self):
        response = Client().get('/auth/signup/')
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        form_data = {
            'username': 'some_username',
            'password1': 'password',
            'password2': 'password',
            'email': 'some@email.com'
            }
        responce = Client().post(
            '/auth/signup/',
            data=form_data,
            follow=True
        )
        self.assertEqual(responce.status_code, 200)

    def test_activate_success(self):
        response = Client().get('/auth/activate/username')
        self.assertContains(
            response,
            'Ваш аккаунт успешно активирован',
            status_code=200
            )

    @freeze_time('2222-04-09')
    def test_activate_expired(self):
        response = Client().get('/auth/activate/username')
        self.assertContains(
            response,
            'Ссылка для активации уже истекла',
            status_code=200
            )

    def tearDown(self):
        super(TestRegister, self).tearDown()
