from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api.views import ExpensesViewset

router = DefaultRouter()
router.register(r'expenses', ExpensesViewset)

urlpatterns = [
    path(r'', include(router.urls)),
]
