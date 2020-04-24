import random
import string

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.utils.datetime_safe import date
from django.views import generic
from django.views.generic import ListView, CreateView
from intest.models import Person, Department
from intest.forms import DepartmentForm
from intest.filters import PersonFilter

from . import filters

dep = Department.objects.all()


# print(dep[1])
# print(date.fromtimestamp(random.uniform(9557815, 1587481015)))
# sw=date.fromtimestamp(random.uniform(956329015, 1587481015))
# print (sw)
# sw2=date.fromtimestamp(random.uniform(9563, 15874))
# print((sw-sw2))

def index(request):
    p = Person(firstname=''.join((random.choice(string.ascii_letters) for i in range(10))),
               surname=''.join((random.choice(string.ascii_letters) for i in range(10))),
               otch=''.join((random.choice(string.ascii_letters) for i in range(10))),
               borndate=date.fromtimestamp(random.uniform(9557815, 956329015)),
               email=''.join((random.choice(string.ascii_letters) for i in range(10))),
               phonenum=random.randint(11111111111, 99999999999),
               startworkdate=date.fromtimestamp(random.uniform(956329015, 1463290150)),
               endworkdate=date.fromtimestamp(random.uniform(1463290150, 1587481015)),
               jobtitle=''.join((random.choice(string.ascii_letters) for i in range(10))),
               department=dep[random.randint(1, 8)]
               )
    p.save()

    return render(request, "index.html")


#
# class CreateDepartmentView(CreateView):
#     model = Department
#     form_class = DepartmentForm
#     template_name = 'peopleslist.html'
#     success_url = 'peopleslist.html'


def peoples(request):
    # object_list = Person.objects.filter().order_by('id')

    # paginator = Paginator(object_list, 10)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    # return render(request, 'peopleslist.html', {
    #     'persons': page_obj
    #                     })

    # if request.method == 'GET':
    #     # paginator = Paginator(object_list, 10)
    #     # page_number = request.GET.get('page')
    #     # page_obj = paginator.get_page(page_number)
    #     # return render(request, 'peopleslist.html', {
    #     #     'persons': page_obj
    #     #                     })
    # elif request.method == 'POST':
    #     print('метод POST')

    # Filters
    # object_list = Person.objects.filter().order_by('department')
    # object_list = Person.objects.filter(endworkdate=None).order_by('endworkdate')
    # if request.method == 'POST':
    #     depfiltr = request.POST.get('depfiltr')
    # else:
    #         depfiltr = ""

    # object_list = Person.objects.filter(department__departmentname=depfiltr).order_by('surname')

    # print(dep.filter(departmentname='АХО').values_list('id'))

    #  depfiltrnew = request.GET.get('depfiltr')

    # !!!!    object_list = Person.objects.filter(department__departmentname=depfiltr).order_by('surname')
    #     user_list = Person.objects.all()
    #     user_filter = PersonFilter(request.GET, queryset=user_list)
    #     user_list = user_filter.qs

    #####
    filter = PersonFilter(request.GET, queryset=Person.objects.all())
    filter_qs = filters.PersonFilter(
        request.GET,
        queryset=Person.objects.all()
    ).qs
    #######
    # filter = PersonFilter(request.GET, queryset=Person.objects.all())
    #   object_list = Person.objects.all().order_by('surname')

    paginator = Paginator(filter_qs, 7)  # Num people in each page
    page = request.GET.get('page')
    #print(filter.form)
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)
    return render(request,
                  'peopleslist.html',
                  {'is_paginated': True,
                   'page_obj': post_list,
                   'persons': post_list,
                   'filter': filter,
                   # 'grade_list': Department.objects.all()
                   })

    # return render(request, 'peopleslist.html', {
    #         # 'persons': Person.objects.all()
    #         'persons': object_list
    # })


def filterlist(request):
    filter = PersonFilter(request.GET, queryset=Person.objects.all())
    return render(request, 'peoplelistfilter.html', {'filter': filter})


# Create your views here.
class PersonList(ListView):
    model = Person
    paginate_by = 9
    # def get_queryset(self):
    #     return Person.objects.filter(department_id="1")


# def get_queryset(self):
#         qs = self.model.objects.all()
#         product_filtered_list = Person(self.request.GET, queryset=qs)
#         return product_filtered_list.qs

#  def get_queryset(self):
#      self.department = get_object_or_404(Person, department=self.kwargs['department'])
#      return Person.objects.filter(department=self.department)
# # paginate_by = 10

class PersonDetailView(generic.DetailView):
    model = Person
