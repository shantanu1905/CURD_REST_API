from django.urls import path
from main import views



from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)




urlpatterns = [
    path("",views.ListAPIView.as_view(),name="todo_list"),
    path("create/", views.CreateAPIView.as_view(),name="todo_create"),
    path("update/<int:pk>/",views.UpdateAPIView.as_view(),name="update_todo"),
    path("delete/<int:pk>/",views.DeleteAPIView.as_view(),name="delete_todo"),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]