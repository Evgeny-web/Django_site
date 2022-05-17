import datetime
from django.utils.translation import gettext_lazy
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import *


# class AddTypeRoom(forms.Form):
#     type = forms.CharField(max_length=150, widget=forms.Textarea(attrs={'cols': 50, 'rows': 1}), label='Тип')


class RentRoom(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['reservation_room'].empty_label = "Комната не выбрана"
        self.fields['pay_method'].empty_label = "Способ оплаты не выбран"

    def clean_date_of_departure(self):
        data = self.cleaned_data['date_of_departure']
        data2 = self.cleaned_data['arrival_date']

        if (data <= data2) and (data2 < datetime.date.today()):
            raise ValidationError(['Invalid date - arrival in past!',
                                   'date_of_departure cant be smaller or equal arrival_date'])

        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(gettext_lazy('Invalid date - arrival more than 4 weeks ahead!'))

        if data <= data2:
            raise forms.ValidationError('Invalid date - date_of_departure cant be smaller or equal arrival_date')

        if data2 < datetime.date.today():
            raise ValidationError(gettext_lazy('Invalid date - arrival in past!'))

        return data

    # def clean_arrival_date(self):
    #     data = self.cleaned_data['arrival_date']
    #
    #     if data < datetime.date.today():
    #         raise ValidationError(gettext_lazy('Invalid date - arrival in past!'))
    #
    #     return data

    class Meta:
        model = Reservation
        fields = ['first_name', 'surname', 'birthday',
                  'reservation_room', 'arrival_date',
                  'date_of_departure', 'phone_number',
                  'email', 'pay_method']
        widgets = {
            'first_name': forms.TextInput(attrs={'cols': 40, 'rows': 1}),
            'surname': forms.TextInput(attrs={'cols': 40, 'rows': 1}),
            'birthday': forms.DateInput(format='%d/%m/%Y'),
            'arrival_date': forms.DateInput(format='%d/%m/%Y'),
            'date_of_departure': forms.DateInput(format='%d/%m/%Y'),
        }
        help_texts = {'birthday': 'Example: 2022-05-05',
                      'arrival_date': 'Example: 2022-05-05',
                      'date_of_departure': 'Example: 2022-05-05'}


# Вариант использования форм связанных с моделями
class AddTypeRoom(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].empty_label = "Комната не выбрана"

    class Meta:
        model = Type
        fields = ['type']
        widgets = {
            'type': forms.Textarea(attrs={'cols': 50, 'rows': 1})
        }


class AddRoom(forms.ModelForm):
    """ Вариант ручного составления формы
    type = forms.ModelChoiceField(queryset=Type.objects.all(), label="Тип комнаты", empty_label="Тип не выбран")
    slug = forms.SlugField(max_length=150, label="URL")
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}))
    area = forms.IntegerField()
    price = forms.IntegerField()
    capacity = forms.IntegerField()
    """

    # Вариант использования форм связанных с моделями
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].empty_label = "Комната не выбрана"

    class Meta:
        model = Room
        fields = ['type', 'slug', 'photo', 'description', 'area', 'price', 'capacity']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 50, 'rows': 5})
        }

    '''
    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) > 100:
            raise ValidationError('Длина превышает 100 символов')

        return description
    '''


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    email = forms.EmailField(label='Email', widget=forms.EmailInput())
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class AddReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Review
        fields = ['first_name', 'surname', 'text', 'grade']
        widgets = {
            'first_name': forms.Textarea(attrs={'cols': 50, 'rows': 1}),
            'surname': forms.Textarea(attrs={'cols': 50, 'rows': 1}),
            'text': forms.Textarea(attrs={'cols': 50, 'rows': 7})
        }
        help_texts = {
            'first_name': 'Enter your name',
            'surname': gettext_lazy('Enter your second name'),
            'text': gettext_lazy('Enter your comment')
        }
