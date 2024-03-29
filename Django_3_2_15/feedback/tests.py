from django.forms import widgets
from django.test import Client, TestCase
from django.urls import reverse

from .forms import FeedbackForm


class TestContextFormFeedback(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = FeedbackForm()

    def test_able_get_form_page(self):
        response = Client().get(reverse('feedback:feedback'))
        self.assertEqual(response.status_code, 200)

    def test_get_form(self):
        response = Client().get(reverse('feedback:feedback'))
        self.assertIn('form', response.context)

    def test_text_label(self):
        text_label = TestContextFormFeedback.form.fields['text'].label
        self.assertEquals(text_label, 'Текст обращения')

    def test_email_label(self):
        email_label = TestContextFormFeedback.form.fields['email'].label
        self.assertEquals(email_label, 'Ваша электронная почта')

    def test_text_help_text(self):
        text_help_text = TestContextFormFeedback.form.fields['text'].help_text
        self.assertEquals(text_help_text, 'Что вы хотите нам сказать?')

    def test_email_help_text(self):
        email_help_text = TestContextFormFeedback.form.fields[
            'email'].help_text
        self.assertEquals(email_help_text,
                          'Оставьте почту, чтобы мы могли с вами связаться')

    def test_text_area(self):
        area = TestContextFormFeedback.form.fields['text'].widget
        self.assertIsInstance(area, widgets.Textarea)

    def test_email_area(self):
        area = TestContextFormFeedback.form.fields['email'].widget
        self.assertIsInstance(area, widgets.EmailInput)

    def test_button_exists(self):
        response = Client().get(reverse('feedback:feedback'))
        self.assertContains(response, 'button')

    def test_redirect_after_submit(self):
        form_data = {
            'text': 'some_text',
            'email': 'some@email.com'
            }
        responce = Client().post(
            reverse('feedback:feedback'),
            data=form_data,
            follow=True
        )
        self.assertRedirects(responce, reverse('feedback:feedback'))

    def tearDown(self):
        super(TestContextFormFeedback, self).tearDown()
