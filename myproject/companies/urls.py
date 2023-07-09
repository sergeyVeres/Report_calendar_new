from . import views

from django.urls import path

urlpatterns = [

    path('', views.companies),
    path('<int:id>/reports/', views.reports),
    path('<int:id>/redact/', views.redact),
    path('new_company/', views.new_company, name='new_company'),
    path('new_report/', views.new_report),
    path('<int:id1>/reports/<int:id2>/redact_report/', views.redact_report, name='redact_report'),
    path('<int:id1>/reports/<int:id2>/delete_report/', views.del_report),
    path('<int:id>/delete', views.del_company),
]