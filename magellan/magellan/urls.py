from django.contrib import admin
from django.urls import path, include, re_path
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('users/', include('users.urls')),
    path('manifest.json', lambda request: JsonResponse(settings.WEB_APP_MANIFEST))
]

# Serve a robot.txt on staging server to prevent search engines from indexing
if settings.ENVIRONMENT == 'Staging':
    urlpatterns.append(re_path(r'robots.txt',
                               lambda request: HttpResponse("User-agent: *\nDisallow: /", content_type="text/plain"),
                               name="robots_file"))
# Serve media files locally
if settings.ENVIRONMENT == 'Development':
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
