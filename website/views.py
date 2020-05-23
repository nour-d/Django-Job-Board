from django.shortcuts import render, get_object_or_404
from .models import Jobs
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    context = {
        'jobs': Jobs.objects.all()
    }
    return render(request, 'website/home.html', context)


class JobsListView(ListView):
    model = Jobs
    template_name = 'website/home.html'
    context_object_name = 'jobs'
    ordering = ['-date_posted']
    paginate_by = 10


class CompanyJobsListView(ListView):
    model = Jobs
    template_name = 'website/company_jobs.html'
    context_object_name = 'jobs'
    ordering = ['-date_posted']
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Jobs.objects.filter(company=user).order_by('-date_posted')


class JobDetailView(DetailView):
    model = Jobs


class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Jobs
    success_url = '/'

    def test_func(self):
        job = self.get_object()
        if self.request.user == job.company:
            return True
        return False


class JobCreateView(LoginRequiredMixin, CreateView):
    model = Jobs
    fields = ['position', 'requirement', 'location', 'apply_link']

    def form_valid(self, form):
        form.instance.company = self.request.user
        return super().form_valid(form)


class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Jobs
    fields = ['position', 'requirement', 'location', 'apply_link']

    def form_valid(self, form):
        form.instance.company = self.request.user
        return super().form_valid(form)

    def test_func(self):
        job = self.get_object()
        if self.request.user == job.company:
            return True
        return False


def about(request):
    return render(request, 'website/about.html', {'title': 'About'})