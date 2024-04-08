from django.urls import path

from MuziqLyrics.accounts.views import SignUpUserView, signout_user, SignInUserView, ProfileDetailsView

urlpatterns = (
    path('signup/', SignUpUserView.as_view(), name='account_signup'),
    path('signout/', signout_user, name='account_signout'),
    path('signin/', SignInUserView.as_view(), name='account_signin'),
    path('<int:pk>/details/',ProfileDetailsView.as_view(), name='account_details')
)