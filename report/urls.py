from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views


app_name = 'report'
urlpatterns = [
    path('', views.ReportListView.as_view(), name='report_list'),
    path('<int:pk>', views.ReportDetailView.as_view(), name='report_detail'),
    path('create/', views.ReportCreate.as_view(), name='report_create'),
    # path('update/<int:pk>', views.UpdateView(), name='report_update'),
]