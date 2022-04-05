from django.db import models
from django.contrib.auth import get_user_model

from form_builder_backend.utils.models import BaseModel

User = get_user_model()


# Create your models here.
class Form(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created_at',)


class Field(BaseModel):
    FORM_TYPE = (
        ('text', 'Text'),
        ('textarea', 'Textarea'),
        ('number', 'Number'),
        ('date', 'Date'),
        ('time', 'Time'),
        ('email', 'Email'),
        ('url', 'Url'),
        ('password', 'Password'),
        ('select', 'Select'),
        ('radio', 'Radio'),
    )
    FORM_KIND = (
        ('text', 'Text'),
        ('dropdown', 'Dropdown'),
        ('radio', 'Radio'),
        ('checkbox', 'Checkbox'),
    )
    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name='fields')
    label = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=FORM_TYPE)
    kind = models.CharField(max_length=100, choices=FORM_KIND)
    order = models.IntegerField(default=0, blank=True)
    required = models.BooleanField(default=False, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.label

    class Meta:
        ordering = ('order', 'created_at',)


class FieldOption(BaseModel):
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=100, blank=True)
    order = models.IntegerField(default=0, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ('order', 'created_at',)


class FormSubmission(BaseModel):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.form.name

    class Meta:
        ordering = ('-created_at',)


class FieldSubmission(BaseModel):
    submission = models.ForeignKey(FormSubmission, on_delete=models.CASCADE, related_name='fields')
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    value = models.TextField(blank=True)

    def __str__(self):
        return self.field.label

    class Meta:
        ordering = ('-created_at',)
