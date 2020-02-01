# Create your views here.
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from . import forms, models

decorators = [login_required]

#Sign Up views
class userCreateView(CreateView):
    form_class = forms.UserCreateForm
    models.User
    success_url = reverse_lazy("login")
    template_name = "accounts/signup/user_signup.html"

class organizationCreateView(CreateView):
    form_class = forms.organizationCreateForm
    models.User
    success_url = reverse_lazy("login")
    template_name = "accounts/signup/organization_signup.html"

class artistCreateView(CreateView):
    form_class = forms.artistCreateForm
    models.User
    success_url = reverse_lazy("login")
    template_name = "accounts/signup/artist_signup.html"


#User Info page
@method_decorator(decorators, name='dispatch')
class userDetailView(DetailView):
    model= models.User

    slug_field = 'display_name'
    slug_url_kwarg = 'display_name'

    template_name= 'accounts/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

@method_decorator(decorators, name='dispatch')
class userUpdateView(UpdateView):
    form_class = forms.UserEditForm
    model = models.User

    template_name = 'accounts/user_update.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('accounts:user_detail', kwargs={'pk': pk })
