from django.contrib import admin
from django.urls import path
from resumechecker.views import JobDescriptionAPI, AnalyzeResumeAPI

urlpatterns = [
    path('api/jobs', JobDescriptionAPI.as_view()),
    path ('api/resume/', AnalyzeResumeAPI.as_view()),
    path('admin/', admin.site.urls),
]
