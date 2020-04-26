"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from intest import views

from intest.views import PersonList

urlpatterns = [
    path('', views.index),
#    path('contacts/', views.contacts),
 #   path('publication/<int:number>', views.publication),
    path('peopleslist/', views.peoples),
    path('personlist/', PersonList.as_view(),name='article-list'),
    # path('peoplelistfilter/', views.filterlist,name='filter'),
  #  path('dep', views.CreateDepartmentView.as_view(),name = 'department'),
    path('personlist/filter/department/<department_id>', PersonList.as_view(),name='filter-article-list'),
    url(r'^person/(?P<pk>\d+)$', views.PersonDetailView.as_view(), name='person-detail'),
#    path('publish/', views.publish),
 #   path('feedback/', views.feedback),
]
