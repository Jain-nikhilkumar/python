# credentialssss/urls.py
from django.shortcuts import render
from django.urls import path

urlpatterns = [
    path('', lambda request: render(request, 'credentialssss/issue_credential.html'), name='root'),
    path('issue-credential/', lambda request: render(request, 'credentialssss/issue_credential.html'), name='issue_credential'),
    # Add other URL patterns as needed
]
