from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.core.paginator import Paginator

from .forms import *
from .models import *
from .utils import *


# def Login(request):
#     return HttpResponse("Страница авторизации!!!")


class AddTypeRoom(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddTypeRoom
    template_name = 'Hotel/addtyperoom.html'
    login_url = reverse_lazy('login')

    # raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление типа комнаты')
        # context['menu'] = menu
        # context['title'] = 'Добавление типа комнаты'
        return dict(list(context.items()) + list(c_def.items()))


class AddRentRoom(DataMixin, CreateView):
    form_class = RentRoom
    template_name = 'Hotel/addrentroom.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Бронирование комнаты',
                                      )
        # context['menu'] = menu
        # context['title'] = 'Добавление комнаты'
        return dict(list(context.items()) + list(c_def.items()))


class UpdateRentRoom(DataMixin, DeleteView):
    model = Reservation
    context_object_name = 'form'
    success_url = 'RoomsList'
    template_name = 'Hotel/addrentroom.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Бронирование комнаты')
        # context['menu'] = menu
        # context['title'] = 'Добавление комнаты'
        return dict(list(context.items()) + list(c_def.items()))


class RentRoomDelete(DataMixin, DeleteView):
    model = Reservation
    template_name = 'Hotel/rentroomdelete.html'
    success_url = reverse_lazy('RoomsList')


class AddRoom(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddRoom
    template_name = 'Hotel/addroom.html'
    # success_url = reverse_lazy('RoomsList')
    login_url = reverse_lazy('login')

    # raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление комнаты')
        # context['menu'] = menu
        # context['title'] = 'Добавление комнаты'
        return dict(list(context.items()) + list(c_def.items()))


# def addroom(request):
#     if request.method == 'POST':
#         form = AddRoom(request.POST, request.FILES)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             '''try:
#                 Room.objects.create(**form.cleaned_data)
#                 return redirect('RoomsList')
#             except:
#                 form.add_error(None, 'Ошибка добавления поста')
#                 '''
#             form.save()
#             return redirect('RoomsList')
#     else:
#         form = AddRoom()
#
#     context = {
#         'form': form,
#         'menu': menu,
#         'title': 'Добавление типа комнаты'
#     }
#     return render(request, 'Hotel/addroom.html', context=context)


def index(request):
    context = {
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'Hotel/index.html', context=context)


def SearchReservation(request):
    search_query = request.GET.get('search', '')

    if search_query:
        resev = Reservation.objects.filter(phone_number=search_query)
    else:
        resev = None

    context = {
        'resev': resev,
        'menu': menu,
        'title': 'Отмена бронирования'
    }
    return render(request, 'Hotel/searchresev.html', context=context)


def about(request):
    rooms = Type.objects.all()

    context = {
        'rooms': rooms,
        'menu': menu,
        'title': 'О сайте'
    }
    return render(request, 'Hotel/about.html', context=context)


class Reviews(DataMixin, ListView):
    model = Review
    template_name = 'Hotel/reviews.html'
    context_object_name = 'rev'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Отзывы')
        return dict(list(context.items()) + list(c_def.items()))


class AddReview(DataMixin, CreateView):
    form_class = AddReviewForm
    template_name = 'Hotel/addreview.html'
    success_url = reverse_lazy('reviews')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Отзыв')
        return dict(list(context.items()) + list(c_def.items()))


# def Reviews(request):
#     context = {
#         'menu': menu,
#         'title': 'Отзывы'
#     }
#     return render(request, 'Hotel/reviews.html', context=context)


class RoomsList(DataMixin, ListView):
    model = Room
    template_name = 'Hotel/rooms.html'
    context_object_name = 'rooms'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Номера')
        # context['menu'] = menu
        # context['title'] = 'Номера'
        return dict(list(context.items()) + list(c_def.items()))



    # def get_queryset(self):
    #     #search_query = request.GET.get('search', '')

# class SearchRoomList(DataMixin, ListView):
#     model = Room
#     template_name = 'Hotel/rooms.html'
#     context_object_name = 'rooms'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='Номера',
#                                       search=f'search={self.request.Get.get("search")}&')
#         # context['menu'] = menu
#         # context['title'] = 'Номера'
#         return dict(list(context.items()) + list(c_def.items()))
#
#     def get_queryset(self):
#         return Room.objects.filter(Q(type__icontains=self.request.Get.get('search')) |
#                                    Q(capacity=self.request.Get.get('search')))

def SearchRoomList(request):
    search_query = request.GET.get('s', '')

    if search_query:
        try :
            #int(search_query)
            rooms = Room.objects.filter(capacity=search_query)
        except:
            rooms = Room.objects.filter(type__type__icontains=search_query)
        # rooms = Room.objects.filter(Q(type__type=search_query) |
        #                             Q(capacity=search_query))
        #else:


    context = {
        'rooms': rooms,
        'menu': menu,
        'title': 'Результат поиска'
    }
    return render(request, 'Hotel/rooms.html', context=context)

# def Rooms(request):
#     rooms = Room.objects.all()
#     context = {
#         'rooms': rooms,
#         'menu': menu,
#         'title': 'Номера'
#     }
#     return render(request, 'Hotel/rooms.html', context=context)


class ShowRoom(DataMixin, DetailView):
    model = Room
    template_name = 'Hotel/RoomDetail.html'
    slug_url_kwarg = 'room_slug'
    context_object_name = 'room'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['room'],
                                      )
        # context['menu'] = menu
        # context['title'] = context['room']
        return dict(list(context.items()) + list(c_def.items()))


# def Show_Room(request, room_slug):
#     room = get_object_or_404(Room, slug=room_slug)
#     context = {
#         'room': room,
#         'menu': menu,
#         'title': room.type,
#         'room_id': room
#     }
#     return render(request, 'Hotel/RoomDetail.html', context=context)


def test_category(request, cat_id):
    rooms = Type.objects.all()
    context = {
        'rooms': rooms,
        'menu': menu,
        'title': 'Номера',
        'category': cat_id
    }
    return render(request, 'Hotel/test.html', context=context)


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'Hotel/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'Hotel/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
