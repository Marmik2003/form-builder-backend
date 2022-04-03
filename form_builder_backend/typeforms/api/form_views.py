from rest_framework import generics, authentication, permissions, status, viewsets, response

from form_builder_backend.typeforms.api.serializers import FormSerializer, FormWithFieldsSerializer, FieldSerializer, \
    OptionSerializer
from form_builder_backend.typeforms.models import Form, Field


class FormViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows typeforms to be viewed or edited.
    """

    serializer_class = FormSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Form.objects.filter(user=self.request.user, deleted=False)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted = True
        instance.save()
        return response.Response(status=status.HTTP_204_NO_CONTENT)


class FormWithFieldsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows typeforms with fields to be viewed only.
    """

    serializer_class = FormWithFieldsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Form.objects.filter(user=self.request.user, deleted=False)


class FieldViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows form fields to be viewed or edited.
    """

    serializer_class = FieldSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, form=self.kwargs['form_pk'])

    def get_queryset(self):
        return Field.objects.filter(user=self.request.user, form=self.kwargs['form_pk'], deleted=False)

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
        serializer.save(user=self.request.user, field=self.kwargs['field_pk'])

    def get_queryset(self):
        return Field.objects.filter(user=self.request.user, field=self.kwargs['field_pk'], deleted=False)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted = True
        instance.save()
        return response.Response(status=status.HTTP_204_NO_CONTENT)
