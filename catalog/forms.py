from django import forms
from django.forms import widgets
from .models import Visit

class ScheduleVisitForm(forms.ModelForm):

    class Meta:
        model = Visit
        fields = ['full_name', 'visit_date', 'visit_time']  # Add 'visit_time' here
        widgets = {
            'visit_date': forms.DateInput(attrs={'type': 'date'}),
            'visit_time': forms.TimeInput(attrs={'type': 'time'}),  # Add this line for a time input widget
        }

    def clean_visit_date(self):
        date = self.cleaned_data['visit_date']
        # Add validation for the date here if needed.
        return date

    def clean_visit_time(self):
        time = self.cleaned_data.get('visit_time', None)  # Change to use get() to avoid KeyError
        # Add validation for the time here if needed.
        return time


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user_profile = UserProfile.objects.create(user=user)
        return user
