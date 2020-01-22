from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views, forms
from django.conf import settings
from django.conf.urls.static import static


app_name= 'accounts'

urlpatterns= [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name= 'logout'),

    path('signup/', views.userCreateView.as_view(), name= 'signup'),
    # path('user_profile/', views.userProfileSummary.as_view(template_name= 'accounts/user_profile.html')),
    path('<slug:pk>/', views.userDetailView.as_view(),name='user_detail'),
    path('update/<pk>/', views.userUpdateView.as_view(),name='user_update'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
