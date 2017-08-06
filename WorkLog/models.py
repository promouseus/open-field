from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Customer(models.Model):
    name = models.CharField(
        _('name'),
        unique=True,
        help_text=_('The full name of the customer'),
        max_length=40,
    )

    class Meta:
        verbose_name = _('customer')
        verbose_name_plural = _('customers')

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(
        _('name'),
        unique=True,
        help_text=_('The full name of the task'),
        max_length=40,
    )

    class Meta:
        verbose_name = _('task')
        verbose_name_plural = _('tasks')

    def __str__(self):
        return self.name


class Logbook(models.Model):
    employee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='employees',
        verbose_name=_('employee'),
    )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='customers',
        verbose_name=_('customer'),
    )

    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name=_('task'),
    )

    date = models.DateField(
        _('date'),
        help_text=_('The date the task is done'),

    )

    minutes = models.PositiveSmallIntegerField(
        _('minutes'),
        help_text=_('Total minutes spend on task'),
    )

    description = models.CharField(
        _('description'),
        help_text=_('Description of the work done'),
        max_length=200,
    )

    billable = models.BooleanField(
        _('billable'),
        help_text=_('Time is billable to customer'),
        default=False,
    )

    invoiced = models.BooleanField(
        _('invoiced'),
        help_text=_('Time is billed to customer'),
        default=False,
    )

    class Meta:
        verbose_name = _('logbook')
        verbose_name_plural = _('logbooks')

    def __str__(self):
        return str(self.minutes) + ' minutes on ' + str(self.date) + ' for ' + str(self.customer.name) + ' on ' + str(self.description)
