from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image, ExifTags
from django.dispatch import receiver


YN_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]


SCHOOLTYPE_CHOICES = [
        ('Public', 'Public'),
        ('Private', 'Private'),
    ]

SEMESTER_CHOICES = [
        ('1st', '1st'),
        ('2nd', '2nd'),
    ]
    
STRAND_CHOICES = [
        ('',''),
        ('Accountancy, Business and Management', 'ABM'),
        ('Humanities and Social Sciences', 'HUMSS'),
        ('Science, Technology, Engineering, and Mathematics', 'STEM'),
        ('General Academic Strand', 'GAS'),
    ]

TRACK_CHOICES = [
        ('',''),
        ('Academic Track', 'Academic Track'),
        ('Technical-Vocational-Livelihood', 'Technical-Vocational-Livelihood'),
        ('Sports Track', 'Sports Track'),
        ('Arts and Design Track', 'Arts and Design Track'),
    ]

SEX_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

EDUCATTAIN_CHOICES = [
        ('',''),
        ('Elementary Graduate', 'Elementary Graduate'),
        ('High School Graduate', 'High School Graduate'),
        ('College Graduate', 'College Graduate'),
        ('Vocational', 'Vocational'),
        ('Masters/Doctorate degree', 'Masters/Doctorate degree'),
        ('Did not attend school', 'Did not attend school'),
    ]

EMPSTATUS_CHOICES = [
        ('Full time', 'Full time'),
        ('Part time', 'Part time'),
        ('Self employed', 'Self employed'),
        ('Unemployed due to ECQ', 'Unemployed due to ECQ'),
        ('Not working', 'Not working'),
    ]


GRADE_CHOICES = [
        ('Grade 11', 'Grade 11'),
        ('Grade 12', 'Grade 12'),
    ]


class STUDENT_INFO(models.Model):
    psa_cer_no = models.CharField(max_length=50, null=True, blank=True)
    lrn = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    extension_name = models.CharField(max_length=50, null=True, blank=True)
    birthdate = models.DateTimeField(default=timezone.now)
    age = models.CharField(max_length=3)
    sex = models.CharField(max_length=6, choices=SEX_CHOICES)
    ip = models.CharField(max_length=3, choices=YN_CHOICES, null=True, blank=True)
    ip_specify = models.CharField(max_length=100, null=True, blank=True)
    mother_tongue = models.CharField(max_length=50, null=True, blank=True)
    religion = models.CharField(max_length=50, null=True, blank=True)
    special_ed_needs = models.CharField(max_length=3, choices=YN_CHOICES, null=True, blank=True)
    speed_needs_specify = models.CharField(max_length=50, null=True, blank=True)
    technology_devices = models.CharField(max_length=3, choices=YN_CHOICES, null=True, blank=True)
    technology_devices_specify = models.CharField(max_length=50, null=True, blank=True)
    house_number_and_street = models.CharField(max_length=50, null=True, blank=True)
    barangay = models.CharField(max_length=50)
    city_municipality = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    region = models.CharField(max_length=50)

    school_year1 = models.CharField(max_length=4)
    school_year2 = models.CharField(max_length=4)
    wlrn = models.CharField(max_length=4, choices=YN_CHOICES)
    returning = models.CharField(max_length=4, choices=YN_CHOICES)
    grade_level_to_enroll = models.CharField(max_length=50, choices=GRADE_CHOICES)
    last_grade_level_com = models.CharField(max_length=50)
    last_school_year_com = models.CharField(max_length=20)
    last_school_attended = models.CharField(max_length=200)
    school_id = models.CharField(max_length= 50)
    school_address = models.CharField(max_length= 200)
    school_type = models.CharField(max_length=8, choices=SCHOOLTYPE_CHOICES)
    school_to_enroll_in = models.CharField(max_length=200)
    school_id_to_enroll = models.CharField(max_length=50)
    school_address_to_enroll = models.CharField(max_length= 200)
    semester = models.CharField(max_length=4, choices=SEMESTER_CHOICES)
    track = models.CharField(max_length=100, choices= TRACK_CHOICES, null=True, blank=True)
    strand = models.CharField(max_length=100, choices= STRAND_CHOICES)

    father_full_name = models.CharField(max_length=100, null=True, blank=True)
    father_educ_attainment = models.CharField(max_length=50, choices= EDUCATTAIN_CHOICES, null=True, blank=True)
    father_employment_status = models.CharField(max_length=50, null=True, blank=True)
    father_working_from_home_due_to_ecq = models.CharField(max_length=3, choices=YN_CHOICES, null=True, blank=True)
    father_contact = models.CharField(max_length=13, null=True, blank=True)
    mother_full_name = models.CharField(max_length=100, null=True, blank=True)
    mother_educ_attainment = models.CharField(max_length=50, choices= EDUCATTAIN_CHOICES, null=True, blank=True)
    mother_employment_status = models.CharField(max_length=50, null=True, blank=True)
    mother_working_from_home_due_to_ecq = models.CharField(max_length=3, choices=YN_CHOICES, null=True, blank=True)
    mother_contact = models.CharField(max_length=13, null=True, blank=True)
    guardian_full_name = models.CharField(max_length=100, null=True, blank=True)
    guardian_educ_attainment = models.CharField(max_length=50, choices= EDUCATTAIN_CHOICES, null=True, blank=True)
    guardian_employment_status = models.CharField(max_length=50, null=True, blank=True)
    guardian_working_from_home_due_to_ecq = models.CharField(max_length=3, choices=YN_CHOICES, null=True, blank=True)
    guardian_contact = models.CharField(max_length=13, null=True, blank=True)

    image = models.FileField(default='default.png', upload_to='student_pics', blank=True, null=True)
    form_137 = models.FileField(default='default.png', upload_to='form_137', blank=True, null=True)
    birth_certificate = models.FileField(default='default.png', upload_to='birth_certificate', blank=True, null=True)

    def __str__(self):
        return self.last_name + self.first_name

    def get_absolute_url(self):
        return reverse('stem:home')