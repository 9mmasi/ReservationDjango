from django.urls import path

from . views import create_reservation,reservation_list,reservation_detail,login_view,update_reservation


urlpatterns=[
    path("",create_reservation,name="created"),
    path("reservations",reservation_list,name='viewlist'),
    path('reservations/<int:pk>/', reservation_detail, name='reservation_detail'),
    path('reservation-update/<int:pk>/', update_reservation, name='update_reservation'),
    path('login/', login_view, name='login'),
]
