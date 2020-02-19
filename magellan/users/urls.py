from django.urls import path
from .views import user_list, user_profile, user_update

urlpatterns = [
    path('list/', user_list, name='user_list'),
    path('profile/<url_short>/', user_profile, name='user_profile'),
    path('profile/<url_short>/edit/', user_update, name='user_update'),
]
