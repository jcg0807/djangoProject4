from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Portfolio


def applicant_list_view(request):
    applicants = User.objects.filter(portfolio__isnull=False).order_by('first_name')
    context = {
        'applicants': applicants,
        'position': 'Junior Developer'
    }
    return render(request, 'applicant_list.html', context)


class ApplicantDetailView(DetailView):
    model = User
    template_name = 'applicant_detail.html'
    context_object_name = 'applicant'
    slug_field = 'username'
    slug_url_kwarg = 'username'


class ApplicantDeleteView(DeleteView):
    model = User
    template_name = 'applicant_confirm_delete.html'
    success_url = reverse_lazy('applicant_list')
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def form_valid(self, form):
        return super().form_valid(form)
