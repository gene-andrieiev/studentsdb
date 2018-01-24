# -*- coding: utf-8 -*-

from django.db import models


# Create your models here.
class Student(models.Model):
    # Student Model

    class Meta(object):
        verbose_name = u"Student"
        verbose_name_plural = u"Students"

    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Name"
    )

    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Surname"
    )

    middle_name = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u"Middle",
        default=''
    )

    birthday = models.DateField(
        blank=False,
        verbose_name=u"Birthdate",
        null=True
    )

    photo = models.ImageField(
        blank=True,
        verbose_name=u"Photo",
        null=True
    )

    ticket = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Ticket"
    )

    notes = models.TextField(
        blank=True,
        verbose_name=u"Additional Notes"
    )

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)



