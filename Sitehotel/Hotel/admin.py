from django.contrib import admin
from .models import *


class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'price', 'capacity', 'photo')
    list_display_links = ('id', 'type', 'price')
    search_fields = ('type', 'capacity')



class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type')
    list_display_links = ('id', 'type')
    search_fields = ('type', )


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'surname', 'grade', 'create_review_date')
    list_display_links = ('first_name', 'surname', 'create_review_date')
    search_fields = ('first_name', 'surname', 'grade')


class GradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'grade')
    list_display_links = ('id', 'grade')
    search_fields = ('grade', )


class RoomInstanceAdmin(admin.ModelAdmin):
    list_display = ('room', 'id', 'due_back', 'status', 'borrower')
    list_display_links = ('room', 'due_back', 'borrower')
    search_fields = ('room', 'borrower')


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'surname', 'reservation_room', 'date_of_departure', 'phone_number')
    list_display_links = ('id', 'first_name', 'reservation_room')
    search_fields = ('first_name', 'surname', 'reservation_room')



class PayMethodAdmin(admin.ModelAdmin):
    list_display = ('id', 'pay_type')
    list_display_links = ('id', 'pay_type')
    search_fields = ('pay_type', )


admin.site.register(Room, RoomAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(RoomInstance, RoomInstanceAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(PayMethod, PayMethodAdmin)
