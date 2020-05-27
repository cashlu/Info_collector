from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .form import ReportForm
from .models import Report
from .utils.report_maker import data_preparer, make_report, make_ledger


class ReportListView(LoginRequiredMixin, ListView):
    """报告列表视图"""
    model = Report
    context_object_name = 'report_list'
    template_name = 'report/report-list.html'


def report_create(request):
    report = None
    if request.mothod == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save()

    else:
        form = ReportForm()

    return render(request, 'report/report-edit.html',
                  {'report': report, 'report_form': form})


# class ReportFormView(FormView):
#     """报告表单视图"""
#     template_name = 'report/report-edit.html'
#     form_class = ReportForm
#
#     success_url = '/success/'
#
#     def get(self, request, *args, **kwargs):
#         form = self.form_class
#         return self.render_to_response({'report_form': form})
#
#     def form_valid(self, form):
#         # 验证表单
#         # form.save()
#         return super().form_valid(form)


class ReportCreate(LoginRequiredMixin, CreateView):
    model = Report
    template_name = 'report/report-edit.html'
    success_url = '/report/'

    fields = (
        'bid', 'name', 'identity', 'decade', 'city', 'town', 'village',
        'purpose',
        'comment',
        'structure', 'security', 'groundsill', 'tilt', 'upon', 'fence',
        'security_detail', 'groundsill_detail', 'tilt_detail',
        'upon_detail', 'fence_detail',
        'assess_level', 'advice', 'street_contract', 'street_contract_phone',
        'village_contract', 'village_contract_phone', 'reviewer',)


# class ReportUpdate(UpdateView):
#     model = Report
#     fields = [field for field in Report._meta.get_fields()]


# class ReportDelete(DeleteView):
#     model = Report
#     fields = [field for field in Report._meta.get_fields()]


class ReportDetailView(LoginRequiredMixin, DetailView):
    """报告详情页"""
    model = Report
    template_name = 'report/detail.html'
    context_object_name = 'report'


def reports(request):
    make_report()
    return HttpResponse("Reports Done")


def town_ledger(request):
    make_ledger("town")
    return HttpResponse("Town Ledger Done")


def village_ledger(request):
    make_ledger("village")
    return HttpResponse("Village Ledger Done")
