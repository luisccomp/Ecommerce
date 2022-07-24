from django.views.generic import FormView, TemplateView

from .forms import UserCreationForm


class LoginPageView(TemplateView):
    template_name = 'users/login.html'


class RegisterFormView(FormView):
    template_name = 'users/register.html'
    form_class = UserCreationForm
    success_url = '/login/'
    
    def form_valid(self, form):
        form.save()
        
        return super().form_valid(form)
