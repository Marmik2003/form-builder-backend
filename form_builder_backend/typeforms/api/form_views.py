from rest_framework import permissions, status, viewsets, response

from form_builder_backend.typeforms.api.serializers import FormSerializer, FormWithFieldsSerializer, FieldSerializer, \
    OptionSerializer, FormSubmissionSerializer, GetSubmissionSerializer
from form_builder_backend.typeforms.models import Form, Field, FieldOption, FormSubmission
from form_builder_backend.typeforms.api.mixins import GetSerializerClassMixin


class FormViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows typeforms to be viewed or edited.
    """

    serializer_class = FormWithFieldsSerializer
    serializer_action_classes = {
        'list': FormSerializer,
        'create': FormSerializer,
        'retrieve': FormWithFieldsSerializer,
        'update': FormSerializer,
    }

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Form.objects.filter(user=self.request.user)
        else:
            return Form.objects.filter(is_public=True)

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


class FormSubmissionViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows form submissions to be viewed, created or edited.
    """

    serializer_class = FormSubmissionSerializer
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'post']
    serializer_action_classes = {
        'list': GetSubmissionSerializer,
        'create': FormSubmissionSerializer,
        'retrieve': GetSubmissionSerializer,
    }

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return FormSubmission.objects.filter(form_id=self.kwargs['form_pk'], user=self.request.user)
        else:
            return FormSubmission.objects.filter(form_id=self.kwargs['form_pk'], is_public=True)

