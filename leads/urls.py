from django.urls import path
from leads.views import *

app_name="leads"

urlpatterns =[
    path('',LeadListView.as_view(),name="leads.index"),
    path('create',LeadCreateView.as_view(),name="leads.create"),
    path('show/<int:pk>/',LeadDetailView.as_view(), name="leads.show"),
    path('update/<int:pk>/',LeadUpdateView.as_view(), name="leads.update"),
    path('delete/<int:pk>/',LeadDeleteView.as_view(), name="leads.delete"),
]