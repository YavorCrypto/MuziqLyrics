from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import views as auth_views, login, logout, get_user_model
from django.urls import reverse_lazy
from django.views import generic as views

from MuziqLyrics.accounts.models import Listener, MuziqUser
from MuziqLyrics.artists.models import Artist

# Create your views here.

UserModel = get_user_model()

# class SignInUserView(auth_views.LoginView):
#     template_name = 'accounts/signin-user.html'
#     redirect_authenticated_user = True


class MuziqUserCreationForm(auth_forms.UserCreationForm):
    user = None
    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('username','account_type',)

class SignUpUserView(views.CreateView):
    template_name = 'accounts/signup-user.html'
    form_class = MuziqUserCreationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, form.instance)
        return result


def signout_user(request):
    logout(request)
    return redirect('index')

class SignInUserView(auth_views.LoginView):
    template_name = 'accounts/signin-user.html'
    redirect_authenticated_user = True

class ProfileDetailsView(views.DetailView):
    template_name = 'accounts/details-user.html'

    def get_queryset(self):
        # Retrieve the user object based on the ID provided in the URL
        user_id = self.kwargs.get('pk')  # Assuming 'pk' is used in the URL conf
        user = get_object_or_404(MuziqUser, pk=user_id)

        # Check the account type of the user and return the corresponding queryset
        if user.account_type == 'Artist':
            queryset = Artist.objects.filter(user=user).prefetch_related('user').all()
        else:
            queryset = Listener.objects.filter(user=user).prefetch_related('user').all()

        return queryset

    def get_model(self):
        return MuziqUser