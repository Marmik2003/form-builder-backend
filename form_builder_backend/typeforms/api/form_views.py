from rest_framework import permissions, status, viewsets, response

from form_builder_backend.typeforms.api.serializers import FormSerializer, FormWithFieldsSerializer, FieldSerializer, \
    OptionSerializer, FormSubmissionSerializer
from form_builder_backend.typeforms.models import Form, Field, FieldOption, FormSubmission
from form_builder_backend.typeforms.api.mixins import GetSerializerClassMixin


class FormViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows typeforms to be viewed or edited.
    """

    serializer_class = FormWithFieldsSerializer
    permission_classes = (permissions.IsAuthenticated,)
    serializer_action_classes = {
        'list': FormSerializer,
        'create': FormSerializer,
        'retrieve': FormWithFieldsSerializer,
        'update': FormSerializer,
    }

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Form.objects.filter(user=self.request.user, deleted=False)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted = True
        instance.save()
        return response.Response(status=status.HTTP_204_NO_CONTENT)


class FieldViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows form fields to be viewed or edited.
    """

    serializer_class = FieldSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, form_id=self.kwargs['form_pk'])

    def get_queryset(self):
        return Field.objects.filter(user=self.request.user, form_id=self.kwargs['form_pk'], deleted=False)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted = True
        instance.save()
        return response.Response(status=status.HTTP_204_NO_CONTENT)


class OptionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows field options to be viewed or edited.
    """

    serializer_class = OptionSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, field_id=self.kwargs['field_pk'])

    def get_queryset(self):
        return FieldOption.objects.filter(user=self.request.user, field_id=self.kwargs['field_pk'], deleted=False)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted = True
        instance.save()
        return response.Response(status=status.HTTP_204_NO_CONTENT)


class FormSubmissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows form submissions to be viewed, created or edited.
    """

    serializer_class = FormSubmissionSerializer
    permission_classes = (permissions.IsAuthenticated,)
    http_method_names = ['get', 'post']

    def get_queryset(self):
        return FormSubmission.objects.filter(user=self.request.user, form_id=self.kwargs['form_pk'], deleted=False)

