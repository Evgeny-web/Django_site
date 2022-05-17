from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('Rooms/', RoomsList.as_view(), name='RoomsList'),
    path('SearchRoom/', SearchRoomList, name='searchroom'),
    path('Room/<slug:room_slug>/', ShowRoom.as_view(), name='RoomDetail'), #'Room/<int:roomid>/' с численным отображением ссылки
    path('about/', about, name='about'),
    path('review/', Reviews.as_view(), name='reviews'),
    path('addreview', AddReview.as_view(), name='addreview'),
    path('category/<int:cat_id>/', test_category, name='category'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('add_type_room/', AddTypeRoom.as_view(), name='add_type_room'),
    path('add_room/', AddRoom.as_view(), name='add_room'),
    path('add_rent_room/<int:pk>/', AddRentRoom.as_view(), name='add_rent_room'),
    path('<int:pk>/rentroomupdate/', UpdateRentRoom.as_view(), name='update_rent_room'),
    path('<int:pk>/rentroomdelete/', RentRoomDelete.as_view(), name='rentroomdelete'),
    path('searchresev/', SearchReservation, name='searchresev'),
]