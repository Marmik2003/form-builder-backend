from rest_framework_nested import routers

from form_builder_backend.typeforms.api.form_views import FormViewSet, FormWithFieldsViewSet, FieldViewSet, OptionViewSet

app_name = "typeforms"

router = routers.DefaultRouter()
router.register(r"", FormViewSet, basename="typeforms")
router.register(r"(?P<form_id>[0-9]+)/form_with_fields", FormWithFieldsViewSet, basename="form_with_fields")
router.register(r"(?P<form_id>[0-9]+)/fields", FieldViewSet, basename="fields")
router.register(r"(?P<form_id>[0-9]+)/fields/(?P<field_id>[0-9]+)/options", OptionViewSet, basename="options")

urlpatterns = router.urls
