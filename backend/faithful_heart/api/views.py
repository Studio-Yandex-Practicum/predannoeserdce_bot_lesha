from django.db.models.functions import Now

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.mixins import (
    CreateModelMixin,
    UpdateModelMixin,
    ListModelMixin,
)
from rest_framework_simplejwt.token_blacklist.models import (
    BlacklistedToken,
    OutstandingToken,
)
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import (
    TelegramUserSerializer,
    UniqueQuestionSerializer,
    FrequentlyAskedQuestionSerializer,
    NewsletterSerializer,
    NotificationSerializer
)
from users.models import TelegramUser
from questions.models import UniqueQuestion, FrequentlyAskedQuestion
from notifications.models import TelegramNewsletter, Notification
from .api_service import export_users_excel
from http import HTTPStatus


class TelegramUsersViewSet(
    CreateModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    """
    Добавление и обновление пользователей.
    """
    serializer_class = TelegramUserSerializer
    queryset = TelegramUser.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = get_object_or_404(TelegramUser, chat_id=self.kwargs.get("pk"))
        return user

    @action(
        methods=[
            "get",
        ],
        detail=True,
        permission_classes=(IsAuthenticated,),
    )
    def get_state(self, request, pk):
        tg_user = TelegramUser.objects.get(chat_id=pk)
        return Response(
            status=HTTPStatus.OK,
            data={"is_fully_filled": tg_user.is_fully_filled},
        )


class DownloadUserInformationView(GenericViewSet):
    """
    Эндпоинт для выгрузки информации пользователей в Excel.
    """

    queryset = TelegramUser.objects.all()
    serializer_class = TelegramUserSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = TelegramUserSerializer(queryset, many=True)
        export_users_excel(queryset)
        return Response(serializer.data)


class FrequentlyAskedQuestionView(ListModelMixin, GenericViewSet):
    """
    Запрос на получение списка вопросов.
    Получение ответа на вопрос.
    Фильтрация по категории позволяет получить вопросы
    для двух категорий - Часто задаваемые вопросы и Информация о приюте
    """

    queryset = FrequentlyAskedQuestion.objects.filter(is_relevant=True)
    serializer_class = FrequentlyAskedQuestionSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("category",)
    permission_classes = [IsAuthenticated]


class UniqueQuestionView(CreateAPIView, GenericViewSet):
    """
    Создание пользователем уникального вопроса.
    Уведомление администратора по email и в Telegram.
    """

    queryset = UniqueQuestion.objects.all()
    serializer_class = UniqueQuestionSerializer
    permission_classes = [IsAuthenticated]


class APILogoutView(APIView):
    """
    Эндпоинт для выхода из системы (удаление токена).
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        if self.request.data.get("all"):
            token: OutstandingToken
            for token in OutstandingToken.objects.filter(user=request.user):
                _, _ = BlacklistedToken.objects.get_or_create(token=token)
            return Response({"status": "Вы вышли из системы"})
        refresh_token = self.request.data.get("refresh_token")
        token = RefreshToken(token=refresh_token)
        token.blacklist()
        return Response({"status": "Вы вышли из системы"})


class TelegramNewsletterViewSet(
    ListModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    queryset = TelegramNewsletter.objects.filter(
        is_finished=False,
        sending_date__gt=Now()
    )
    serializer_class = NewsletterSerializer
    pagination_class = None
    permission_classes = [IsAuthenticated]


class NotificationViewSet(
    ListModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    queryset = Notification.objects.filter(
        is_finished=False
    )
    serializer_class = NotificationSerializer
    pagination_class = None
    permission_classes = [IsAuthenticated]
