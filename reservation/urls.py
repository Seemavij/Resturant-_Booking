from django.urls import path
from . import views


app_name = 'reservation'

urlpatterns = [
    path('', views.table_reservation, name='table_reservation'),
    path('manage_reservation/',
         views.ReservationList.as_view(), name='manage_reservation'),
    path('edit_reservation/<reservation_id>/', views.edit_reservation,
         name='edit_reservation'),
    path('delete_reservation/<reservation_id>/', views.delete_reservation,
         name='delete_reservation')
]
 






  