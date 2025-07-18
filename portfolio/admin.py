from django.contrib import admin
from .models import Portfolio, Project


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user', 'portfolio_title', 'project')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'created_at', 'updated_at')
