from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from feedback import forms


def feedback(request, message=''):
    template = 'feedback/feedback.html'
    form = forms.FeedbackForm(request.POST or None)

    if form.is_valid():
        text = form.cleaned_data.get('text')
        user_email = form.cleaned_data.get('email')
        send_mail(
            'Спасибо за обратную связь!',
            f'Мы получили Ваше сообщение:\n\n{text}\n\n'
            f'Постараемся помочь Вам как можно скорее!',
            settings.EMAIL,
            [user_email],
            fail_silently=False,
        )
        messages.add_message(request, messages.SUCCESS,
                             'Ваше обращение успешно отправлено')
        return redirect('feedback:feedback')

    context = {'form': form, 'message': message}
    return render(request, template, context)
