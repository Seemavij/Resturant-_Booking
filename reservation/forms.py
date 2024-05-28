from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    """
    Table Reservation form
    """

    number_of_guests = forms.IntegerField(required=True,
                                          widget=forms.TextInput(
                                              attrs={
                                                  'pattern': '[1-4]+',
                                                  'title': 'Enter a number between 1 and 4.'
                                              }

                                          ))
    date = forms.DateField(input_formats=['%d/%m/%Y'],
                           widget=forms.DateInput(attrs={
                               'placeholder': 'dd/mm/yyyy'
                           }))

    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'pattern': '[A-Za-z ]+', 'title': 'Enter characters only.'}))

    phone = forms.IntegerField(required=True,
                               widget=forms.TextInput(
                                   attrs={
                                       'placeholder': '0123456789',
                                       'pattern': '[0123456789]+',
                                       'title': 'Enter digits only.'
                                   }
                               )
                               )

    class Meta:
        model = Reservation
        fields = '__all__'