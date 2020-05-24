from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import StudentRegisterForm
from .models import STUDENT_INFO
from django.views.generic import (DetailView, ListView, CreateView, TemplateView)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .filter_mixin import ListFilteredMixin
from .filters import StudentFilter

# Create your views here.
"""
def home(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        formset = ImageFormset(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            lrn = form.cleaned_data.get('lrn')
            messages.success(request, f'Submit Success')
            return redirect('stem:home')
    else:
        form = StudentRegisterForm()
    context={
        'form' : form,
    }
    return render(request, 'stem/enrol.html', context)"""



class StudentCreateView(SuccessMessageMixin, CreateView):
    model = STUDENT_INFO
    form_class = StudentRegisterForm
    success_message = "Thank you!"


class StudentListView(LoginRequiredMixin, ListFilteredMixin, ListView):
    model = STUDENT_INFO
    template_name = 'stem/list_student.html'
    context_object_name = 'students'
    paginate_by = 1
    filter_set = StudentFilter
    def get_queryset(self):
        qs = self.model.objects.all().order_by('last_name')
        student_filter = StudentFilter(self.request.GET, queryset=qs)
        return student_filter.qs


class StudentDetailView(LoginRequiredMixin, DetailView):
    model = STUDENT_INFO
    template_name = 'stem/student_info_detail.html'