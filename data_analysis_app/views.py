from django.shortcuts import render, redirect
from django.contrib import messages
from .data_processing import load_data


def main_page(request):

    if request.method == "POST":
        try:
            file = request.FILES['file']
            data = load_data(file)
            if data is None:
                messages.error(request, 'Incorrect data!')
            else:
                messages.success(request, 'Success!')
                request.session['data'] = data.to_html(
                    index=False, classes='table table-striped table-bordered table-hover table-sm')\
                    .replace('<tr style="text-align: right;">', '<tr>')
                request.session['summary'] = data.describe().to_html(
                    classes='table table-hover table-light table-sm')\
                    .replace('<tr style="text-align: right;">', '<tr>')
                numeric_data = data.select_dtypes(include='number')
                numeric_data_dict = {}
                for column in numeric_data.columns:
                    numeric_data_dict[column] = numeric_data[column].to_list()
                request.session['numeric_data'] = numeric_data_dict
                return redirect('/results')
        except:
            messages.error(request, 'No data!')

    return render(request, 'data_analysis_app/index.html')


def results_page(request):

    context = {
        'data': request.session.get('data'),
        'summary': request.session.get('summary')
    }

    return render(request, 'data_analysis_app/results.html', context)
