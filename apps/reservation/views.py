from django.core.mail import send_mail
from django.conf import settings
from rest_framework.generics import CreateAPIView

from .serializers import ReservationSerializer

from apps.base.auth import UnsafeSessionAuthentication


class ReservationAPIView(CreateAPIView):
    serializer_class = ReservationSerializer
    authentication_classes = (UnsafeSessionAuthentication,)

    # def perform_create(self, serializer):
    #     instance = serializer.save()
    #
    #     created_at = instance.created_at.strftime("%Y-%m-%d %H:%M:%S")
    #     title = "Новая бронь: {0}".format(created_at)
    #     body = """
    #     Имя: {name};
    #     Телефон: {phone};
    #     Дата: {date};
    #     Время с: {time_start};
    #     Время до: {time_end};
    #     Количество человек: {people};
    #     Комментарий: {comment}
    #     """.format(
    #         name=instance.name,
    #         phone=instance.phone_number,
    #         date=instance.date,
    #         time_start=instance.time_start,
    #         time_end=instance.time_end,
    #         people=instance.count_people,
    #         comment=instance.comment,
    #     )
    #
    #     send_mail(
    #         title,
    #         body,
    #         settings.EMAIL_HOST_USER,
    #         ['reservation@borisbar.ru'],
    #         fail_silently=False
    #     )
