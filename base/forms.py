from django.forms import ModelForm
from .models import Task, User
from django.contrib.auth.forms import UserCreationForm


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class AddTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['user', 'completed']



class UpdateTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['user']