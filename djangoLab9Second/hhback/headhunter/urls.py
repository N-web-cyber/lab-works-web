from django.urls import path, re_path
from headhunter.models import Company, Vacancy
from headhunter.views import companies_list, show_a_company, vacancies_of_company,vacancies_list,show_a_vacancy,top_ten

urlpatterns = [
    path('companies/', companies_list),
    path('companies/<int:company_id>/', show_a_company),
    path('companies/<int:company_id>/vacancies/', vacancies_of_company),
    path('vacancies/', vacancies_list),
    path('vacancies/<int:vacancy_id>/', show_a_vacancy),
    path('vacancies/top_ten/', top_ten)
]