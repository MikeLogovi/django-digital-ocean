from django.contrib import admin
from django.urls import include, path
from leads.views import home_page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_page),
    path('leads/', include("leads.urls",namespace="leads"))
]

