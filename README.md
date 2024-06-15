Overview
This project is a web application built using Django, designed to allow users to upload CSV files, perform data analysis on the uploaded data using pandas, and display the results and visualizations on the web interface. This tool is useful for quick data exploration and visualization without needing to write code.


Features:
-File Upload: Users can upload CSV files through a web form.
-Data Analysis: The application processes the CSV file to:
-Display the first few rows.
-Calculate summary statistics (mean, median, standard deviation) for numerical columns.
-Identify and handle missing values.
-Data Visualization: The application generates histograms for numerical columns and displays these plots on the web page.
-User Interface: Simple and user-friendly interface using Django templates.


Requirements:
-Python 3.x
-Django 3.x or later
-pandas
-numpy
-matplotlib
-seaborn


Project Structure
-views.py: Contains the logic for handling file uploads, data analysis, and visualization.
-forms.py: Defines the form for file upload.
-templates/analysis/upload.html: Template for the file upload page.
-templates/analysis/results.html: Template for displaying analysis results and visualizations.
-settings.py: Configuration file for Django settings, including media file handling.


Usage
-Upload CSV File: Go to the file upload page and upload a CSV file.
-View Analysis: After uploading, you will be redirected to a results page showing the first few rows of the data, summary statistics, missing values, and 
 histograms.


Sample csv file for the Data Analysis - business-financial-data-march-2024-csv
