# Create your views here.
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from . import forms, models

# @login_required
class userProfileSummary(DetailView):
    model= models.User
    #
    slug_field = 'display_name'
    slug_url_kwarg = 'display_name'

    template_name= 'accounts/user_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
    # template_name= "accounts/user_profile.html"

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"
