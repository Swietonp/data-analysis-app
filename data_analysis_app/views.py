from django.shortcuts import render


def main_page(request):
    return render(request, 'data_analysis_app/index.html')
