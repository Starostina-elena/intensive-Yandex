from django import forms

from .models import Feedback


class FeedbackForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Feedback
        fields = '__all__'
        labels = {
            'text': 'Текст обращения',
            'email': 'Ваша электронная почта',
        }
        help_texts = {
            'text': 'Что вы хотите нам сказать?',
            'email': 'Оставьте почту, чтобы мы могли с вами связаться'
        }
        widgets = {
            'email': forms.EmailInput()
        }
