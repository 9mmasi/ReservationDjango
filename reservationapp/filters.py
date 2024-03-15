import django_filters
from . models import *

class ReservationFilter(django_filters.FilterSet):
    class Meta:
        fields='__all__'
        models=Reservation
