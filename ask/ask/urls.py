"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
# from django.urls import include
# from ask.qa.views import test
#
# urlpatterns = [
#     path('', test, name="home"),
#     path('login/', test, name="login"),
#     path('signup/', test, name="signup"),
#     path('question/', test, name="question"),
#     path('ask/', test, name="ask"),
#     path('popular/', test, name="popular"),
#     path('new/', test, name="new"),
# ]

from django.conf.urls import url, include
from django.contrib import admin

# from ask.ask.views import found, not_found, init25
# from ask.qa.views import index, popular, ask, login_view, signup
from ask.qa.views import test

urlpatterns = [

    url(r'^$', test),
    url(r'^init25/', test),
    url(r'^login/', test),
    url(r'^signup/', test),
    url(r'^ask/', test),
    # url(r'^answer/', answer),
    url(r'^popular/', test),
    url(r'^new/', test),
    url(r'^question/', test),
]
