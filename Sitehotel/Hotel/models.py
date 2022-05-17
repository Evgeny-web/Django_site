from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import User
from datetime import date


# Будет отвечать за тип комнаты
class Type(models.Model):
    type = models.TextField(max_length=50, help_text='Enter a type hotel room')

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('RoomDetail', kwargs={'room': self.pk})

    class Meta:
        verbose_name = "Тип комнаты"
        verbose_name_plural = "Типы комнат"
        ordering = ['id']


# Способ оплаты номера, выбираем при бронировании
class PayMethod(models.Model):
    pay_type = models.CharField(max_length=50)

    def __str__(self):
        return self.pay_type

    class Meta:
        verbose_name = 'Способ оплаты'
        verbose_name_plural = "Способы оплаты"


# Класс оценки для отзывов
class Grade(models.Model):
    grade = models.CharField(max_length=1, help_text="Choose grade")

    def __str__(self):
        return self.grade

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = "Оценки"


# Класс для отзывов
class Review(models.Model):
    first_name = models.TextField(max_length=30, help_text="Enter your name.")
    surname = models.TextField(max_length=35, help_text="Enter your surname.")
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    text = models.TextField(max_length=2000, help_text="Enter your comment about Hotel")
    create_review_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.surname}  {self.first_name}'

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = "Отзывы"


# Тип комнаты, включает: тип, фото, описание, площадь, цену и вместимость
class Room(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE, help_text='select a type for this hotel room')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(max_length=500, help_text='Enter a brief description of the hotel room')
    area = models.IntegerField(blank=True)
    price = models.IntegerField(blank=True)
    capacity = models.IntegerField(null=True) #Вместительность


    def __str__(self):
        return self.type.type

    def get_absolute_url(self):
        return reverse('RoomDetail', args=[str(self.slug)])

    class Meta:
        verbose_name = "Комната"
        verbose_name_plural = "Комнаты"
        ordering = ['-type']


class RoomInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this room')
    room = models.ForeignKey('Room', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Room availability'
    )

    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Экземпляр комнаты"
        verbose_name_plural = "Экземпляры комнат"

    def __str__(self):
        return f'{self.id} ({self.room.type})'

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False


# Создадим класс для бронирования номеров в отеле
class Reservation(models.Model):
    first_name = models.TextField(max_length=30, help_text="Enter your name.")
    surname = models.TextField(max_length=35, help_text="Enter your surname.")
    birthday = models.DateField()
    reservation_room = models.ForeignKey(Room, on_delete=models.CASCADE)
    arrival_date = models.DateField()
    date_of_departure = models.DateField()
    phone_number = models.IntegerField(help_text="Enter your number phone")
    email = models.EmailField(help_text="Enter your email")
    pay_method = models.ForeignKey(PayMethod, on_delete=models.CASCADE)

    def __str__(self):
        return f'Бронь: {self.first_name} {self.surname}'

    class Meta:
        ordering = ['arrival_date', 'date_of_departure', 'surname']
        verbose_name = 'Бронирование'
        verbose_name_plural = "Бронирования"
