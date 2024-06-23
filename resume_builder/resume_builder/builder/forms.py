from django import forms
from .models import PersonalInfo

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = [
            'first_name', 'last_name', 'email', 'phone', 'address', 'linkedin',
            'school_name', 'degree', 'field_of_study', 'education_start_date', 'education_end_date',
            'job_title', 'company_name', 'job_start_date', 'job_end_date', 'job_description',
            'certification_name', 'certification_issuer', 'certification_date',
            'project_title', 'project_description', 'skills'
        ]
