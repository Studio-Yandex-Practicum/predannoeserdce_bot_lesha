from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from api.views import (APILogoutView, FrequentlyAskedQuestionView,
                       NotificationViewSet, TelegramNewsletterViewSet,
                       TelegramUsersViewSet, UniqueQuestionView)

app_name = 'api'
router_v1 = DefaultRouter()

router_v1.register(r'users', TelegramUsersViewSet)
router_v1.register(r'faq', FrequentlyAskedQuestionView)
router_v1.register(r'unique_question', UniqueQuestionView)
router_v1.register(r'newsletter', TelegramNewsletterViewSet)
router_v1.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path(
        'v1/',
        include(router_v1.urls),
        name='api-root'
    ),
    path(
        'v1/obtain_token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        'v1/logout_token/',
        APILogoutView.as_view(),
        name='logout_token'
    ),
]
