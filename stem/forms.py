from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import STUDENT_INFO


YN_CHOICES = [
        ('No', 'No'),
        ('Yes', 'Yes'),
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


GRADE_CHOICES = [
        ('Grade 11', 'Grade 11'),
        ('Grade 12', 'Grade 12'),
    ]


LGRADE_CHOICES = [
        ('Grade 6', 'Grade 6'),
        ('Grade 7', 'Grade 7'),
        ('Grade 8', 'Grade 8'),
        ('Grade 9', 'Grade 9'),
        ('Grade 10', 'Grade 10'),
        ('Grade 11', 'Grade 11'),
        ('Grade 12', 'Grade 12'),
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


EMPSTATUS_CHOICES = [
        ('Full time', 'Full time'),
        ('Part time', 'Part time'),
        ('Self employed', 'Self employed'),
        ('Unemployed due to ECQ', 'Unemployed due to ECQ'),
        ('Not working', 'Not working'),
    ]


YEARS= [x for x in range(1990,2020)]


class StudentRegisterForm(forms.ModelForm):
    school_year1 = forms.CharField(label='A1. School Year')
    school_year2 = forms.CharField(label='-----------')
    wlrn = forms.ChoiceField(label='A2. Has LRN', choices=YN_CHOICES)
    returning = forms.ChoiceField(label='A3. Returning (Balik eskwela)', choices=YN_CHOICES)
    grade_level_to_enroll = forms.ChoiceField(label='A4. Grade Level to Enroll', choices=GRADE_CHOICES)
    last_grade_level_com = forms.ChoiceField(label='A5. Last grade level completed', choices=LGRADE_CHOICES)
    last_school_year_com = forms.CharField(label='A6. Last school year completed')
    school_id_to_enroll = forms.CharField(label='A12. School ID')
    last_school_attended = forms.CharField(label='A7. Last School Attended')
    school_id = forms.CharField(label='A8. School ID')
    school_address = forms.CharField(label='A9. School Address')
    school_type = forms.ChoiceField(label='A10. School Type', choices=SCHOOLTYPE_CHOICES)
    school_to_enroll_in = forms.CharField(label='A11. School to enroll in')
    school_address_to_enroll = forms.CharField(label='A13. School Address')
    semester = forms.ChoiceField(label='A14. Semester', choices=SEMESTER_CHOICES)
    track = forms.ChoiceField(label='A15. Track', choices=TRACK_CHOICES)
    strand = forms.ChoiceField(label='A16. Strand', choices=STRAND_CHOICES, required=False)

    psa_cer_no = forms.CharField(label='B1. PSA Birth Certificate No. (if available upon enrolment)', required=False)
    lrn = forms.CharField(label='B2. Learners Reference Number (LRN)')
    last_name = forms.CharField(label='B3. Last Name')
    first_name = forms.CharField(label='B4. First Name')
    middle_name = forms.CharField(label='B5. Middle Name', required=False)
    extension_name = forms.CharField(label='B6. Extension Name', required=False)
    birthdate = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    age = forms.CharField(label='B8. Age')
    sex = forms.ChoiceField(label='B9. Sex', choices=SEX_CHOICES)
    ip = forms.ChoiceField(label='B10. Belonging to Indigenous People (IP)', choices=YN_CHOICES, required=False)
    ip_specify = forms.CharField(label='B11. If yes, please specify:', required=False)
    mother_tongue = forms.CharField(label='B12. Mother tongue', required=False)
    religion = forms.CharField(label='B13. Religion', required=False)
    special_ed_needs = forms.ChoiceField(label='B14. Does the learner have special education needs?', choices=YN_CHOICES, required=False)
    speed_needs_specify = forms.CharField(label='B15. If yes, please specify:', required=False)
    technology_devices = forms.ChoiceField(label='B16. Do you have any assistive technology devices available at home?', choices=YN_CHOICES, required=False)
    technology_devices_specify = forms.CharField(label='B17. If yes, please specify:', required=False)
    house_number_and_street = forms.CharField(label='B18. House number and street', required=False)
    barangay = forms.CharField(label='B19. Barangay')
    city_municipality = forms.CharField(label='B20. City/Municipality')
    province = forms.CharField(label='B21. Province')
    region = forms.CharField(label='B22. Region')
    
    father_full_name = forms.CharField(label='C1. Father Full name (surname, name, middle name)')
    father_educ_attainment = forms.ChoiceField(label='C2. Father Educational Attainment', choices=EDUCATTAIN_CHOICES)
    father_working_from_home_due_to_ecq = forms.ChoiceField(label='C4. Working from home due to_ECQ', choices=YN_CHOICES)
    mother_full_name = forms.CharField(label='C7. Mother Full name (surname, name, middle name)')
    mother_educ_attainment = forms.ChoiceField(label='C8. Mother Educational Attainment', choices=EDUCATTAIN_CHOICES)
    mother_working_from_home_due_to_ecq = forms.ChoiceField(label='C10. Working from home due to_ECQ', choices=YN_CHOICES)
    guardian_full_name = forms.CharField(label='C13. Guardian Full name (surname, name, middle name)', required=False)
    guardian_educ_attainment = forms.ChoiceField(label='C14. Guardian Educational Attainment', choices=EDUCATTAIN_CHOICES)
    guardian_working_from_home_due_to_ecq = forms.ChoiceField(label='C16. Working from home due to_ECQ', choices=YN_CHOICES)

    image = forms.FileInput()
    birth_certificate = forms.FileField(label='Birth Certificate', required=False)
    form_137 = forms.FileField(label='School Card', required=False)
    
    class Meta:
        model = STUDENT_INFO
        fields = [
            'school_year1',
            'school_year2',
            'wlrn',
            'returning',
            'grade_level_to_enroll',
            'last_grade_level_com',
            'last_school_year_com',
            'last_school_attended',
            'school_id',
            'school_address',
            'school_type',
            'school_to_enroll_in',
            'school_id_to_enroll',
            'school_address_to_enroll',
            'semester',
            'track',
            'strand',

            'psa_cer_no',
            'lrn',
            'last_name',
            'first_name',
            'middle_name',
            'extension_name',
            'birthdate',
            'age',
            'sex',
            'ip',
            'ip_specify',
            'mother_tongue',
            'religion',
            'special_ed_needs',
            'speed_needs_specify',
            'technology_devices',
            'technology_devices_specify',
            'house_number_and_street',
            'barangay',
            'city_municipality',
            'province',
            'region',
            
            'father_full_name',
            'father_educ_attainment',
            'father_employment_status',
            'father_working_from_home_due_to_ecq',
            'father_contact',
            'mother_full_name',
            'mother_educ_attainment',
            'mother_employment_status',
            'mother_working_from_home_due_to_ecq',
            'mother_contact',
            'guardian_full_name',
            'guardian_educ_attainment',
            'guardian_employment_status',
            'guardian_working_from_home_due_to_ecq',
            'guardian_contact',

            'image',
            'form_137',
            'birth_certificate',
        ]