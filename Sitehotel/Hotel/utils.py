from .models import *


menu = [{'title': 'Главная страница', 'urlname': 'home'},
        {'title': 'О сайте', 'urlname': 'about'},
        {'title': 'Номера', 'urlname': 'RoomsList'},
        {'title': 'Отзывы', 'urlname': 'reviews'},
        {'title': 'Добавить тип комнаты', 'urlname': 'add_type_room'},
        {'title': 'Добавить комнату', 'urlname': 'add_room'},
        {'title': 'Отменить бронирование', 'urlname': 'searchresev'}
        ]


class DataMixin:
    paginate_by = 5

    def get_user_context(self, **kwargs):
        context = kwargs
        # rooms = Room.objects.all()
        # type = Type.objects.all()

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(4)
            user_menu.pop(4)

        context['menu'] = user_menu
        # context['rooms'] = rooms
        # context['type'] = type
        return context
