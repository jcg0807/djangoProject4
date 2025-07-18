from django.urls import path
from .views import applicant_list_view, ApplicantDetailView, ApplicantDeleteView

urlpatterns = [
    path('', applicant_list_view, name='applicant_list'),
    path('portfolio/<str:username>/', ApplicantDetailView.as_view(), name='applicant_detail'),
    path('delete/<str:username>/', ApplicantDeleteView.as_view(), name='applicant_delete'),
]
