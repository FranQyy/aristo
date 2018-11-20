from django.urls import path, include
from . import views
from . import endpoints

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),

    path('api/', include(endpoints)),
    path('api/auth/', include('knox.urls')),
    path('rest-auth/', include('rest_auth.urls')),

]
