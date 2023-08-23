
from django.contrib import admin
from django.urls import path, reverse_lazy
from main import views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView



urlpatterns = [

    path('', views.index, name="home"),
    path('signup/', views.signup, name='signup'),
    path('enroll/', views.etant_eleve, name='etant-eleve'),
     path('about/', views.about_us_view, name='about'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('account/settings/', views.Settings.as_view(), name="settings"),
    path('account/settings/password-change/', PasswordChangeView.as_view(template_name='main/password_change.html', success_url=reverse_lazy('password-change-done')), name='password-change'),
    path('account/settings/passord-change-done/', PasswordChangeDoneView.as_view(template_name='main/password_change_done.html'), name='password-change-done'),
    path('user/profile/<str:username>', views.user_profile, name="user-profile"),
    path('user-profile-photo-full/<str:username>', views.user_photo_full, name="user-photo-full"),
]