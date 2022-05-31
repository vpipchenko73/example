"""example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
# from django.http import HttpResponse
# from django.utils.translation import gettext as _ # импортируем функцию для перевода
# from django.views import View
# from django.shortcuts import render
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth.decorators import login_required
 
# Create your views here.
 
# class Index(View):
#     def get(self, request):
#         #. Translators: This message appears on the home page only
#         string = _('Hello world')
#
#         context = {
#             'string': string,
#         }
#
#         return HttpResponse(render(request, 'index.html', context))
#

# @login_required
# def set_language(request):
#     lang = request.GET.get('ru', 'en')
#     request.session[settings.LANGUAGE_SESSION_KEY] = lang
#     response = HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
#     response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)
#     return response


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')), # подключаем встроенные эндопинты для работы с локализацией
    path('admin/', admin.site.urls),
    #path('', Index.as_view()),
    path('', include('example.urls1'))
]

