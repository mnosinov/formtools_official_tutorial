from django.shortcuts import render
from formtools.wizard.views import SessionWizardView
from .forms import StepOneForm, StepTwoForm


def index(request):
    return render(request, 'multistepapp/index.html')


class FormWizardView(SessionWizardView):
    template_name ='multistepapp/steps.html'
    form_list = [StepOneForm, StepTwoForm]

    def get(self, request, *args, **kwargs):
        try:
            return self.render(self.get_form())
        except KeyError:
            return super().get(request, *args, **kwargs)

    def done(self, form_list, **kwargs):
        return render(
            self.request,
            'multistepapp/done.html',
            {
                'form_data': [form.cleaned_data for form in form_list],
            }
        )
