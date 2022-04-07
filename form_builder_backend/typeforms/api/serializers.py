from rest_framework import serializers
from form_builder_backend.typeforms.models import Form, Field, FieldOption, FormSubmission, FieldSubmission


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldOption
        fields = ('id', 'text', 'order')


class FieldSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Field
        fields = ('id', 'label', 'type', 'kind', 'order', 'options', 'multiple', 'required')


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ('id', 'name', 'description')


class FormWithFieldsSerializer(serializers.ModelSerializer):
    fields = FieldSerializer(many=True)

    class Meta:
        model = Form
        fields = ('id', 'name', 'description', 'fields')


class SubmissionFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldSubmission
        fields = ('id', 'field', 'value')


class FormSubmissionSerializer(serializers.ModelSerializer):
    fields = SubmissionFieldSerializer(many=True)

    class Meta:
        model = FormSubmission
        fields = ('id', 'fields')
