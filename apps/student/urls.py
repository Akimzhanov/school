from django.urls import path
from .views import *
# tariff_view
urlpatterns = [
    path('', home, name='home'),
    path('account/register/', register, name='register'),
    path('account/update_user/<int:user_id>/', update_user, name='update_user'),
    path('account/delete_user/<int:user_id>/', delete_user, name='delete_user'),
    path('account/users/', user_list, name='user_list'),
    path('account/login/', login_view, name='login'),
    path('account/logout/', logout_view, name='logout'),
    path('account/profile/<int:user_id>/', user_profile_view, name='user_profile'),
    path('tariffs/', tariff_list, name='tariff_list'),
    path('tariffs/new/', tariff_create, name='tariff_create'),
    path('tariffs/<int:pk>/edit/', tariff_update, name='tariff_update'),
    path('tariffs/<int:pk>/delete/', tariff_delete, name='tariff_delete'),
    path('tariffs/<int:pk>/', tariff_view, name='tariff_view'),

]
