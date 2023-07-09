import datetime

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from . import models
from .forms import CompanyForm, ReportForm
from .finddate import finddate




def index(request):
    return render(request, 'companies/base.html')


def companies(request):
    company = models.Company.objects.filter(parent=request.user)
    report = models.Report.report_name.field
    deadline = models.Report.deadline.field
    done = models.Report.done.field
    comment = models.Report.comment.field
    return render(request, 'companies/company.html', {'company': company, 'report': report,
                                                      'deadline': deadline, 'done': done, 'comment': comment})


def reports(request, id):
    company = models.Company.objects.filter(parent=request.user, id=id)
    print(models.Report.objects.all())
    print(company.values)
    for rep in models.Report.objects.all():
        print(rep.deadline, datetime.date.today())
        if not rep.done and rep.deadline < datetime.date.today():
            rep.deadline_status = True
            rep.save()
    report = models.Report.report_name.field
    period = models.Report.period.field
    year = models.Report.year.field
    deadline = models.Report.deadline.field
    deadline_status = models.Report.deadline_status.field
    done = models.Report.done.field
    comment = models.Report.comment.field

    return render(request, 'companies/reports.html', {'company': company, 'report': report, 'period': period, 'year': year,
                                                      'deadline': deadline, 'deadline_status': deadline_status, 'done': done, 'comment': comment})


def redact(response, id):
    company = models.Company.objects.get(id=id)
    if response.method == "POST":
        form = CompanyForm(response.POST, instance=company)

        if form.is_valid():
            form.save()
            return redirect("/companies")

    form = CompanyForm(instance=company)
    return render(response, 'companies/company_redact.html', {'form': form})


@csrf_exempt
def redact_report(response, id1, id2):
    company = models.Company.objects.get(id=id1)
    report = models.Report.objects.get(id=id2)
    if response.method == "POST":
        form = ReportForm(response.POST, instance=report)

        if form.is_valid():
            f = form.save(commit=False)
            f.deadline = finddate(f.year, f.period)
            f.save()
            return redirect(f"/companies/{form['company'].value()}/reports")

    form = ReportForm(instance=report)
    return render(response, 'companies/report_redact.html', {'form': form})


def new_company(response):
    if response.method == "POST":
        form = CompanyForm(response.POST)

        if form.is_valid():
            f = form.save(commit=False)
            f.parent = response.user
            f.save()
            return redirect("/companies")

    form = CompanyForm()
    return render(response, "companies/new_comp.html", {"form": form})


def new_report(response):

    if response.method == "POST":
        form = ReportForm(response.POST)

        if form.is_valid():
            f = form.save(commit=False)
            f.deadline = finddate(f.year, f.period)
            f.save()

            return redirect(f"/companies/{f.company.id}/reports")


    form = ReportForm()
    return render(response, "companies/new_report.html", {"form": form})


def del_report(response, id1, id2):
    company = models.Company.objects.get(id=id1)
    report = models.Report.objects.get(id=id2)
    report.delete()
    return redirect(f"/companies/{id1}/reports")

def del_company(request, id):
    company = models.Company.objects.filter(id=id)
    company.delete()
    return redirect("/companies/")
