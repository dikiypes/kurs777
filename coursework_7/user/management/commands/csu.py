from django.core.management import BaseCommand
from user.models import User


# Команда создания суперюзера. Так как мы сделали вход по почте,
# при этом отменили по логину, который должен быть обязательно в методе созданию СЮ
class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='djangoproject1639@yandex.ru',
            first_name='Django',
            last_name='Djangarov',
            is_staff=True,
            is_superuser=True,
        )

        user.set_password('0001qwerty1000')
        user.save()
