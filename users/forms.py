from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "password1", "password2"]

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["email"]