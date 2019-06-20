from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name= 'accounts'

urlpatterns= [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'),
        name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name= 'thanks'),
    path('signup/', views.SignUp.as_view(), name= 'signup'),
    # path('user_profile/', views.userProfileSummary.as_view(template_name= 'accounts/user_profile.html')),
    path('<slug:display_name>/', views.userProfileSummary.as_view(),name='user_profile'),

]
