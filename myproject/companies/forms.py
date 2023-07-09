from django import forms
from django.forms import ModelForm
from .models import Company, Report


class CompanyForm(ModelForm):

    class Meta:
        model = Company
        fields = ['name']


class ReportForm(ModelForm):

    class Meta:
        model = Report
        fields = ['report_name', 'year', 'period', 'done', 'company', 'comment']


