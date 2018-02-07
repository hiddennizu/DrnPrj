from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    # name = forms.CharField(
    #     label='Course Name ',
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the name of course'})
    # )
    #
    # code = forms.CharField(
    #     label='Course Code',
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the code of course'})
    #
    # )

    class Meta:
        model = Course
        fields = ['name', 'code']
