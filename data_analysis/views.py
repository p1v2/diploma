from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render


@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'data_analysis/index.html')
