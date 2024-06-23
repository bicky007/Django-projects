from django.db import models

class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    linkedin = models.URLField(max_length=200, blank=True)

    # Education
    school_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=50)
    field_of_study = models.CharField(max_length=50)
    education_start_date = models.DateField()
    education_end_date = models.DateField()

    # Experience
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    job_start_date = models.DateField()
    job_end_date = models.DateField()
    job_description = models.TextField()

    # Certification
    certification_name = models.CharField(max_length=100, blank=True)
    certification_issuer = models.CharField(max_length=100, blank=True)
    certification_date = models.DateField(null=True, blank=True)

    # Projects
    project_title = models.CharField(max_length=100, blank=True)
    project_description = models.TextField(blank=True)

    # Skills
    skills = models.TextField(blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
