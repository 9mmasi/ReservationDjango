from django.shortcuts import render,redirect, get_object_or_404
from . forms import ReservationForm
from django.contrib import messages
from . models import Reservation

# Create your views

def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Your Successful submit your detail")
            return redirect('created')
    else:
        form = ReservationForm()

    context = {
        'form': form,
        
    }

    return render(request, 'index.html', context)  


def reservation_list(request):
    reservations = Reservation.objects.all()

    context = {
        'reservations': reservations,
    }

    return render(request, 'showList.html', context)


def reservation_detail(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)

    context = {
        'reservation': reservation,
    }

    return render(request, 'reservationDetail.html', context)