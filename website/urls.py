from django.urls import path
from .views import JobsListView, JobDetailView, JobCreateView, JobUpdateView, JobDeleteView, CompanyJobsListView
from . import views

urlpatterns = [
    path('', JobsListView.as_view(), name='website-home'),
    path('job/<int:pk>', JobDetailView.as_view(), name='jobs-detail'),
    path('job/new/', JobCreateView.as_view(), name='jobs-create'),
    path('job/<int:pk>/update/', JobUpdateView.as_view(), name='jobs-update'),
    path('job/<int:pk>/delete/', JobDeleteView.as_view(), name='jobs-delete'),
    path('company/<str:username>', CompanyJobsListView.as_view(), name='company-jobs'),
    path('about/', views.about, name='website-about'),
]
