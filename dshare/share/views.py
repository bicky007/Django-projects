import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import FileResponse, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .Custom_Secret import PASSWORD

uploaded_files = {}

def login_view(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        if password == PASSWORD:
            return redirect('home')
    return render(request, 'share/login.html')

def home_view(request):
    return render(request, 'share/home.html')

@csrf_exempt
def upload_view(request):
    if request.method == 'POST':
        if 'file' in request.FILES:
            uploaded_file = request.FILES['file']
            # Ensure the media directory exists
            if not os.path.exists(settings.MEDIA_ROOT):
                os.makedirs(settings.MEDIA_ROOT)
            file_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
            with open(file_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            uploaded_files['file'] = file_path
            return JsonResponse({'status': 'File uploaded'})
        elif 'text' in request.POST:
            uploaded_text = request.POST['text']
            uploaded_files['text'] = uploaded_text
            return JsonResponse({'status': 'Text uploaded'})
    return JsonResponse({'status': 'No file or text uploaded'})

def download_view(request):
    file_path = uploaded_files.get('file')
    if file_path:
        response = FileResponse(open(file_path, 'rb'))
        return response
    text = uploaded_files.get('text')
    if text:
        return HttpResponse(text, content_type='text/plain')
    return JsonResponse({'status': 'No file or text uploaded'})