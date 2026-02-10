from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, IngredientViewSet

router = DefaultRouter()
router.register(r"recipes", RecipeViewSet)
router.register(r"Ingredients", IngredientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]