# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

def groups_list(request):
    groups = (
        {'id': 1,
         'name': u'G-1',
         'leader': {'id': 1, 'name': u'Yevhenii Andrieiev'}},
        {'id': 2,
         'name': u'G-2',
         'leader': {'id': 2, 'name': u'Yevhenii Andrieiev'}},
        {'id': 3,
         'name': u'G-3',
         'leader': {'id': 3, 'name': u'Yevhenii Andrieiev'}},
    )
    return render(request, 'students/groups_list.html', {'groups': groups})


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
