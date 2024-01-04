from django.urls import path, reverse_lazy
from . import views
from .views import PostCreateView, ContactFormView, PostDetailView, PostListView, unregister_module
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from users.views import CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView
from django.conf.urls.static import static 
from django.conf import settings

app_name = 'itreporting'
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact/', ContactFormView.as_view(), name = 'contact'),
    path('modulelist/<int:fk>', PostListView.as_view(), name='modules'),
    path('module/<int:pk>', PostDetailView.as_view(), name = 'module-detail'), 
    path('register_module/<int:module_id>/', views.register_module, name='register_module'),
    path('unregister_module/<int:module_id>/', unregister_module, name='unregister-module'),
    path('my_registrations/', views.my_registrations, name='my-registrations'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', views.custom_password_reset_complete, name='password_reset_complete'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)