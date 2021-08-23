"""badger_buddy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from discussion_board.users.forms import EmailValidationOnForgotPassword

from django_registration.backends.activation.views import RegistrationView
from discussion_board.users.forms import UserRegistrationForm

handler404 = 'discussion_board.error_handling.views.page_not_found'

urlpatterns = [
    path('board/', include('discussion_board.discussion_board.urls')),
    path('users/password_reset/', auth_views.PasswordResetView.as_view(form_class=EmailValidationOnForgotPassword), name='password_reset'),
    path('users/register/',
        RegistrationView.as_view(
            form_class=UserRegistrationForm
        ),
        name='django_registration_register',
    ),
    path('users/',
        include('django_registration.backends.activation.urls')
    ),
    path('users/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('help/', include('discussion_board.help.urls')),
    path('profile/', include('discussion_board.users.urls')),
    path('exercises/', include('discussion_board.exercises.urls'))
]
