from django.contrib import admin
from django.urls import path, include, re_path
from django.http import HttpResponse
from django.conf import settings

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
]

if settings.ENVIRONMENT == 'Staging':
    urlpatterns.append(re_path(r'robots.txt',
                               lambda request: HttpResponse("User-agent: *\nDisallow: /", content_type="text/plain"),
                               name="robots_file"))
