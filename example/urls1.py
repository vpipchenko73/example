# from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.utils.translation import gettext as _ # импортируем функцию для перевода
from django.views import View
from django.shortcuts import render
#from django.conf.urls.i18n import i18n_patterns
#from django.utils.translation import activate, get_supported_language_variant, LANGUAGE_SESSION_KEY
from django.utils import timezone
from django.shortcuts import redirect
import pytz #  импортируем стандартный модуль для работы с часовыми поясами

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

class Index(View):
    def get(self, request):

        string = _('Hello world')
        curent_time = timezone.now()

        context = {
            'string': string,
            'current_time': timezone.now(),
            'timezones': pytz.common_timezones #  добавляем в контекст все доступные часовые пояса
        }

        return HttpResponse(render(request, 'index.html', context))

    #  по пост-запросу будем добавлять в сессию часовой пояс, который и будет обрабатываться написанным нами ранее middleware
    def post(self, request):
        request.session['django_timezone'] = request.POST['timezone']
        print (request.session['django_timezone'], timezone.now())
        return redirect('http://127.0.0.1:8000/')









urlpatterns = [
    #path('i18n/', include('django.conf.urls.i18n')), # подключаем встроенные эндопинты для работы с локализацией
    #path('admin/', admin.site.urls),
    path('', Index.as_view()),
    #path('', include("path('index/', Index.as_view())"))
]
