from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import View

from user.form import LoginForm


class LoginView(View):
    # def post(self, request):
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     user = authenticate(username=username, password=password)
    #
    #     if user:
    #         request.session['is_login'] = True
    #         request.session['username'] = user
    #         return HttpResponseRedirect('/report/')
    #     else:
    #         return HttpResponseRedirect(settings.LOGIN_URL)
    #
    # def get(self, request):
    #     return render(request, 'report/login.html')
    def get(self, request):
        return render(request, 'user/login.html')

    def post(self, request):
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('report:report_list'))
                else:
                    return render(request, 'user/login.html',
                                  {'msg': '该用户未激活'})
            else:
                return render(request, 'user/login.html',
                              {'msg': '用户名活着密码错误'})
        else:
            return render(request, 'user/login.html',
                          {'login_form': login_form})
