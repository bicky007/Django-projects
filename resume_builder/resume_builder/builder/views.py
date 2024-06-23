from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from .forms import PersonalInfoForm
from .models import PersonalInfo

def index(request):
    if request.method == 'POST':
        form = PersonalInfoForm(request.POST)
        if form.is_valid():
            personal_info = form.save()
            return redirect('view_resume', personal_info_id=personal_info.id)
    else:
        form = PersonalInfoForm()
    return render(request, 'builder/index.html', {'form': form})

def view_resume(request, personal_info_id):
    personal_info = PersonalInfo.objects.get(id=personal_info_id)
    if request.GET.get('download'):
        html_string = render_to_string('builder/view_resume.html', {'personal_info': personal_info})
        html = HTML(string=html_string)
        pdf = html.write_pdf()
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="resume_{personal_info.id}.pdf"'
        return response
    return render(request, 'builder/view_resume.html', {'personal_info': personal_info})
