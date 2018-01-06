# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


def journal_list(request):

    journal = (
        {'id': 1,
         'name': u'Yevhenii'},
        {'id': 2,
         'name': u'Andrieiev Yevhenii'},
        {'id': 3,
         'name': u'Andrieiev'},
    )
    return render(request, 'students/journal_list.html', {'journal': journal})
