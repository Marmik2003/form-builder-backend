from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_at',)


class Field(models.Model):
    FORM_TYPE = (
        ('text', 'Text'),
        ('textarea', 'Textarea'),
        ('number', 'Number'),
        ('date', 'Date'),
        ('time', 'Time'),
        ('email', 'Email'),
        ('url', 'Url'),
        ('password', 'Password'),
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.label

    class Meta:
        ordering = ('order', '-created_at',)


class FieldOption(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='options')
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('order', '-created_at',)


class FormSubmission(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.form.name

    class Meta:
        ordering = ('-created_at',)


class FieldSubmission(models.Model):
    submission = models.ForeignKey(FormSubmission, on_delete=models.CASCADE, related_name='fields')
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    value = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.field.name

    class Meta:
        ordering = ('-created_at',)
