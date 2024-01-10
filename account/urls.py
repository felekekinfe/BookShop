from django.urls import path
from account import views


urlpatterns = [
    path('register/',views.register,name='register'),
    path('edit_profile/',views.profile_edit,name='profile_edit'),
    path('login_page/',views.login_page,name='login_page'),
    path('logout_page/',views.logout,name='logout_page'),
     path('change_password/',views.change_passwword,name='change_password'),
    #path('login_page/',UserLoginView.as_view(),name='login_page')
]
