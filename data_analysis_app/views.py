from django.shortcuts import render
from django.contrib import messages
from .data_processing import load_data


def main_page(request):

    if request.method == "POST":
        file = request.FILES['file']
        data = load_data(file)
        if data is None:
            messages.error(request, 'Incorrect data!')
        else:
            messages.success(request, 'Success!')

    return render(request, 'data_analysis_app/index.html')
