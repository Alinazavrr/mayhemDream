from django.urls import path
from . import views
# namespace = 'accounts' # reverse('user_login'/'accounts:user_login')

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    # path('logout/', LogoutView.as_view(next_page='user_login'), name='user_logout'),
    path('logout/', views.my_logout, name='user_logout'),
    path('change_password/', views.UserPasswordChangeView.as_view(), name='change_password'),
    path('change_password/done/', views.UserPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('profile/permissions/', views.UserPermissions.as_view(), name='user_permissions'),
    path('register/', views.SignUpView.as_view(), name='user_register'),
    path('delete_account/', views.DeleteAccountView.as_view(), name='delete_account_page'),
]
