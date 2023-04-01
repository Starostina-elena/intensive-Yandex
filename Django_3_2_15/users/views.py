

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.timezone import datetime, timedelta

from pytz import UTC

from .forms import UserChangeProfile, UserChangeProfileBasic, UserRegisterForm
from .models import Profile


def signup(request):
    template = 'users/signup.html'
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        email = form.cleaned_data.get('email')
        user = User.objects.create_user(
            username,
            is_active=settings.DEBUG,
            email=email,
            )
        user.set_password(password)
        user.save()
        profile = Profile.objects.create(user=user)
        profile.save()
        send_mail(
            'Благодарим за регистрацию!',
            f'Чтобы завершить регистрацию, пройдите по этой ссылке:\n\n'
            f'http://{settings.ALLOWED_HOSTS[0]}:8000/'
            f'auth/activate/{username}',
            settings.EMAIL,
            [email],
            fail_silently=False,
        )
        return redirect('/auth/login')

    context = {'form': form}
    return render(request, template, context)


def activate(request, username):
    user = get_object_or_404(
        User.objects,
        username=username
    )
    template = 'users/user_activated.html'
    if (datetime.now() - timedelta(hours=12)).replace(tzinfo=UTC) \
            <= user.date_joined:
        user.is_active = True
        user.save()
        context = {'message': 'Ваш аккаунт успешно активирован'}
    else:
        context = {'message': 'Ссылка для активации уже истекла'}
    return render(request, template, context)


def user_list(request):
    template = 'users/user_list.html'
    context = {'users': User.objects.filter(is_active=True)}
    return render(request, template, context)


def user_detail(request, user_id):
    template = 'users/user_detail.html'
    user = get_object_or_404(
        User.objects,
        id=user_id
    )
    context = {'user_info': user}
    return render(request, template, context)


@login_required
def profile(request):
    template = 'users/profile.html'
    user = User.objects.get(username=request.user.get_username())
    form1 = UserChangeProfileBasic(request.POST or None)
    form2 = UserChangeProfile(request.POST or None)

    if form1.is_valid() and form2.is_valid():
        email = form1.cleaned_data.get('email')
        name = form1.cleaned_data.get('first_name')
        surname = form1.cleaned_data.get('last_name')
        birthday = form2.cleaned_data.get('birthday')
        userpic = form2.cleaned_data.get('userpic')
        user.email = email
        user.first_name = name
        user.last_name = surname
        user.profile.image = userpic
        user.profile.birthday = birthday
        user.profile.save()
        user.save()
        messages.add_message(request, messages.SUCCESS,
                             'Изменения сохранены')
        return redirect('/users/profile')
    else:
        form1.fields['email'].initial = user.email
        form1.fields['first_name'].initial = user.first_name
        form1.fields['last_name'].initial = user.last_name
        form2.fields['birthday'].initial = user.profile.birthday

    context = {'form1': form1, 'form2': form2}
    return render(request, template, context)
