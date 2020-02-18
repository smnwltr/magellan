from django.urls import path

from .views import Home, Imprint, Privacy

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('imprint/', Imprint.as_view(), name='imprint'),
    path('privacy-policy/', Privacy.as_view(), name='imprint'),
]
