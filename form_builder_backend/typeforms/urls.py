from rest_framework_nested import routers

from form_builder_backend.typeforms.api.form_views import FormViewSet, FieldViewSet, OptionViewSet, \
    FormSubmissionViewSet

app_name = "typeforms"

router = routers.DefaultRouter()
router.register(r"", FormViewSet, basename="typeforms")
router.register(r"(?P<form_pk>[0-9]+)/fields", FieldViewSet, basename="fields")
router.register(r"(?P<form_pk>[0-9]+)/fields/(?P<field_pk>[0-9]+)/options", OptionViewSet, basename="options")
router.register(r"(?P<form_pk>[0-9]+)/submissions", FormSubmissionViewSet, basename="submissions")

urlpatterns = router.urls
