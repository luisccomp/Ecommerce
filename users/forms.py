from django.contrib.auth import forms


class UserCreationForm(forms.UserCreationForm):
    
    class Meta(forms.UserCreationForm.Meta):
        fields = forms.UserCreationForm.Meta.fields + ('email',)
