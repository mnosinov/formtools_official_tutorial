from django import forms


class StepOneForm(forms.Form):
    name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
    email = forms.EmailField()


class StepTwoForm(forms.Form):
    job = forms.CharField(max_length=100)
    salary = forms.CharField(max_length=100)
    job_description = forms.CharField(widget=forms.Textarea)
