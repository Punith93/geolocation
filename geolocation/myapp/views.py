import os

from django.shortcuts import render, redirect, Http404
from django.template.response import TemplateResponse
from django.conf import settings
from django.http import HttpResponse
from .forms import DocumentForm
from werkzeug.utils import secure_filename
from django.contrib import messages
from django.utils.translation import pgettext
from django.core.files.base import ContentFile
from .utils import formatter_address
from geolocation.settings import *
import json

from django.core.files.storage import FileSystemStorage

# Create your views here.
def home(request):
	form = DocumentForm(request.POST, request.FILES)
	if request.method == 'POST':
		if form.is_valid():
			file = request.FILES['document']
			if file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
				result = formatter_address(file)
				if result:
					return redirect('success')
				else:
					messages.error(request, 'Please try after some time')
					return redirect('home')
	        else:
	        	messages.error(request, 'Please upload excel file only')
	        	return redirect('home')

	ctx = {
	'form': form,
	}
	return TemplateResponse(request, 'index.html', ctx)


def download(request):
	file_path = UPLOAD_FOLDER+'/'+'geo_details.csv'
	if os.path.exists(file_path):
	    with open(file_path, 'rb') as fh:
	        response = HttpResponse(fh, content_type="application/vnd.ms-excel")
	        response['Content-Disposition'] = 'attachment; filename=' + 'geo_details.xlsx'
	    return response


def success(request):
	context = {}
	return TemplateResponse(request, 'sucess.html', context)