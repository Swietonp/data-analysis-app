from django.shortcuts import render
from django.contrib import messages


def main_page(request):

    if request.method == "POST":
        messages.success(request, "Success!")

    return render(request, 'data_analysis_app/index.html')
