from django.urls import path, include

from . import views


urlpatterns = [
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
]
