# Create your views here.
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from . import forms, models

# Sign Up View
class userCreateView(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")    #Succesful login reroutes to login page
    template_name = "accounts/signup.html"


# @login_required
class userDetailView(DetailView):
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

class userCreateView(CreateView):
    form_class = forms.UserCreateForm
    models.User
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"

class userUpdateView(UpdateView):
    form_class = forms.UserEditForm
    model = models.User

    template_name = 'accounts/edit_profile.html'

    def get_success_url(self, display_name):
        display_name = self.kwargs['pk']
        return reverse_lazy('accounts:edit_profile', kwargs={'pk': display_name})

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context
    #
    # def get_object(self, queryset=None):
    #     return self.request.user
    #
    # def get(self, request, **kwargs):
    #     self.object = User.objects.get(username=self.request.user.username)
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     context = self.get_context_data(object=self.object, form=form)
    #     return self.render_to_response(context)
    #
    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.user = self.request.user
    #     self.object.save()
    #     return HttpResponseRedirect(self.get_success_url())
