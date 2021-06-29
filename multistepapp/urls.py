from django.urls import path

from .views import index, FormWizardView

urlpatterns = [
    path('', index, name='index'),
    path('start_wizard/', FormWizardView.as_view(), name='start_wizard'),
]
