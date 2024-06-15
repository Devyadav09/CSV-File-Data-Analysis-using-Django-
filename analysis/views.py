from django.shortcuts import render
from .forms import UploadFileForm
import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg') 
import seaborn as sns
import io
import base64
from django.conf import settings

def handle_uploaded_file(f):
    file_path = os.path.join(settings.MEDIA_ROOT, f.name)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_path

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_path = handle_uploaded_file(request.FILES['file'])
            data = pd.read_csv(file_path)
            context = analyze_data(data)
            return render(request, 'analysis/results.html', context)
    else:
        form = UploadFileForm()
    return render(request, 'analysis/upload.html', {'form': form})

def analyze_data(data):
    
    first_rows = data.head()

  
    summary_stats = data.describe()

 
    missing_values = data.isnull().sum().reset_index()
    missing_values.columns = ['Column', 'Missing Values']

 
    file_name = 'plot.png'
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    sns.histplot(data.select_dtypes(include=['number']).melt(), x="value", hue="variable").figure.savefig(file_path, format='png')
    return {
        'first_rows': first_rows.to_html(),
        'summary_stats': summary_stats.to_html(),
        'missing_values': missing_values.to_html(index=False),
        'plot_url': os.path.join(settings.MEDIA_URL, file_name),
    }
