from django.urls import path
from . views import create_reservation,reservation_list,reservation_detail


urlpatterns=[
    path("",create_reservation,name="created"),
    path("reservations",reservation_list,name='viewlist'),
    path('reservations/<int:pk>/', reservation_detail, name='reservation_detail'),
]
