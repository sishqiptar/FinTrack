"""
URL configuration for fintrack_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from finance_app.views import (
    ExpenseViewSet,
    InvestmentViewSet,
    BudgetViewSet,
    SuggestionViewSet,
)

router = routers.DefaultRouter()
router.register(r'expenses', ExpenseViewSet, basename='expense')
router.register(r'investments', InvestmentViewSet, basename='investment')
router.register(r'budgets', BudgetViewSet, basename='budget')
router.register(r'suggestions', SuggestionViewSet, basename='suggestion')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]