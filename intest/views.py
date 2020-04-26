import random
import string
from itertools import groupby

import numpy as np
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.shortcuts import render, get_object_or_404
from django.utils.datetime_safe import date
from django.views import generic
from django.views.generic import ListView, CreateView
from intest.models import Person, Department
from intest.filters import PersonFilter

from . import filters

#dep = Department.objects.all()

def index(request):
    # p = Person(firstname=''.join((random.choice(string.ascii_letters) for i in range(10))),
    #            surname=''.join((random.choice(string.ascii_letters) for i in range(10))),
    #            otch=''.join((random.choice(string.ascii_letters) for i in range(10))),
    #            borndate=date.fromtimestamp(random.uniform(9557815, 956329015)),
    #            email=''.join((random.choice(string.ascii_letters) for i in range(10))),
    #            phonenum=random.randint(11111111111, 99999999999),
    #            startworkdate=date.fromtimestamp(random.uniform(956329015, 1463290150)),
    #            endworkdate=date.fromtimestamp(random.uniform(1463290150, 1587481015)),
    #            jobtitle=''.join((random.choice(string.ascii_letters) for i in range(10))),
    #            department=dep[random.randint(1, 8)]
    #            )
    # p.save()

    return render(request, "index.html")


def peoples(request):

    filter = PersonFilter(request.GET, queryset=Person.objects.all())
    filter_qs = filters.PersonFilter(
        request.GET,
        queryset=Person.objects.all()
    ).qs


    paginator = Paginator(filter_qs, 7)  # Num people in each page
    page = request.GET.get('page')

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



# Create your views here.
class PersonList(ListView):
    model = Person
    paginate_by = 7
    def getparts(self):
        pers = self.model.objects.all().order_by("surname")
        schar = []
        d = {}
        for onepers in pers:
            schar += [str(onepers.surname)[0]]
            a = []
            if d.get(str((onepers.surname)[0])) != None:
                d[str((onepers.surname)[0])].append(onepers.id)
            else:
                d[str((onepers.surname)[0])] = a
                a.append(onepers.id)
        paglist = [a for a, _ in groupby(schar)]
        part = np.array_split(paglist, 7)
        return part, d

    def get_queryset(self):
        symbol = self.request.GET.get('symbol')
        pers = self.model.objects.all().order_by("surname")
        if symbol != None and str(symbol) != '':
            s = int(str(symbol))
            query = []
            part, d = self.getparts()
            for i in part[s]:
                query = query + d[i]

            pers = Person.objects.filter(id__in=query).order_by("surname")
        return pers
    def get_context_data(self, **kwargs):

        context = super(PersonList, self).get_context_data(**kwargs)
        paglistall_d  =self.getparts()
        paglistall= paglistall_d[0]
        context['pagination_seven'] = {i:(str(paglistall[i][0]) +'-' + str(paglistall[i][len(paglistall[i])-1])) for i in range(7)}
        return context


class PersonDetailView(generic.DetailView):
    model = Person
