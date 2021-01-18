from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StockForm


def index(request):
    # if request.method =='POST':
    #     form = StockForm(request.POST)
    #     if form.is_valid():
    #         return 
    return render(request, "Stack/index.html")
