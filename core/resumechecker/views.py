from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response  # Corrected import
from .serializer import JobDescriptionSerializer, JobDescription, ResumeSerializer, Resume
from .analyzer import process_resume  

class JobDescriptionAPI(APIView):
    def get(self, request):
        queryset = JobDescription.objects.all()
        serializer = JobDescriptionSerializer(queryset, many=True)
        return Response({
            'status': True,
            'data': serializer.data
        })

class AnalyzeResumeAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            if not data.get('job_description'):
                return Response({
                    'status': False,
                    'message': 'Job Description is required',
                    'data': {}
                })
            
            serializer = ResumeSerializer(data=data)
            if not serializer.is_valid():
                return Response({
                    'status': False,
                    'message': 'Validation errors',
                    'data': serializer.errors
                })

            resume_instance = serializer.save()  # Save the resume first
            resume_path = resume_instance.resume.path  # Get resume file path
            data = process_resume(resume_path,
    JobDescription.objects.get(id=data.get('job_description')).job_description)


            return Response({
                'status': True,
                'message': 'Resume analyzed successfully',
                'data': data
            })
        except Exception as e:
            return Response({
                'status': False,
                'message': str(e),
                'data': {}
            })
