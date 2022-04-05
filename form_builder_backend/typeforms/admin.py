from django.contrib import admin
from .models import Form, Field, FieldOption, FormSubmission, FieldSubmission

# Register your models here.
admin.site.register(Form)
admin.site.register(Field)
admin.site.register(FieldOption)
admin.site.register(FormSubmission)
admin.site.register(FieldSubmission)
