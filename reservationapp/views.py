from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login,logout
from datetime import date,datetime
from . filters import *

from django.contrib import messages
from . models import Reservation
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect,HttpResponse 
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views
def to_camel_case(s):
    words = s.split('_')
    return ''.join(word.capitalize() for word in words)

def create_reservation(request):
   
    if request.method == 'POST':
        Firstname = to_camel_case(request.POST.get('Firstname'))
        Lastname = to_camel_case(request.POST.get('Lastname'))
        Email = to_camel_case(request.POST.get('Email'))
        State = to_camel_case(request.POST.get('State'))
        Phone = to_camel_case(request.POST.get('Phone'))
        Address = to_camel_case(request.POST.get('Address'))
        Address2 = to_camel_case(request.POST.get('Address2'))
        Zip_code = to_camel_case(request.POST.get('Zip_code'))
        Image = request.FILES.get('Image')
        Date_checkIn = to_camel_case(request.POST.get('Date_checkIn'))
        Date_checkOut = to_camel_case(request.POST.get('Date_checkOut'))
        Time_checkIn = to_camel_case(request.POST.get('Time_checkIn'))
        Time_checkOut = to_camel_case(request.POST.get('Time_checkOut'))

        Reservation.objects.create(
            Firstname=Firstname, Lastname=Lastname,
            Email=Email, State=State,
            Phone=Phone, Address=Address,
            Address2=Address2, Zip_code=Zip_code,
            Image=Image, Date_checkIn=Date_checkIn,
            Date_checkOut=Date_checkOut, Time_checkIn=Time_checkIn,
            Time_checkOut=Time_checkOut
        )

        messages.success(request, 'Registration successfully!')
        return redirect("created")

        
    

    return render(request, 'index.html')  


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('viewlist')
        else:
            # Login failed
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        # Display the login form
        return render(request, 'login.html')    








def reservation_list(request):
    if request.user.is_authenticated:
        reservations = Reservation.objects.all()

        # Filter reservations based on Date_checkIn and Date_checkOut range
        Date_checkIn = request.GET.get('Date_checkIn', '')
        Date_checkOut = request.GET.get('Date_checkOut', '')
        
        # Validate date format consistency
        date_format = "%m-%d-%Y"
        try:
            if Date_checkIn:
                datetime.strptime(Date_checkIn, date_format)
            if Date_checkOut:
                datetime.strptime(Date_checkOut, date_format)
        except ValueError:
            # Handle invalid date format
            # You can redirect the user to an error page or display a message
            return HttpResponse("Invalid date format. Date format should be MM-DD-YYYY.")

        if Date_checkIn and Date_checkOut:
            # Convert string inputs to datetime objects
            Date_checkIn = datetime.strptime(Date_checkIn, date_format)
            Date_checkOut = datetime.strptime(Date_checkOut, date_format)
            reservations = reservations.filter(Date_checkIn__range=[Date_checkIn, Date_checkOut])

        reservations = reservations.order_by('-Date_checkIn')    

        paginator = Paginator(reservations, 10)
        page = request.GET.get('page')

        try:
            reservations = paginator.page(page)
        except PageNotAnInteger:
            reservations = paginator.page(1)
        except EmptyPage:
            reservations = paginator.page(paginator.num_pages)

        context = {
            'reservations': reservations,
            'Date_checkIn': Date_checkIn,
            'Date_checkOut': Date_checkOut,
        }
        return render(request, 'showList.html', context)
    else:
        return redirect("login")




def reservation_detail(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)

    if request.user.is_authenticated:
        # User is logged in, allow access to the reservation details
        context = {
            'reservation': reservation,
        }
        return render(request, 'reservationDetail.html', context)
    else:
        # User is not logged in, handle accordingly
        return redirect("login")

def update_reservation(request, pk):
    if request.user.is_authenticated:
        # Get the reservation object you want to update
        instance = get_object_or_404(Reservation, id=pk)

        if request.method == 'POST':
            instance.Firstname = request.POST.get('Firstname')
            instance.Lastname = request.POST.get('Lastname')
            instance.Email = request.POST.get('Email')
            instance.Phone = request.POST.get('Phone')
            instance.State= request.POST.get('State')
            instance.Zip_code = request.POST.get('Zip_code')
            instance.Address = request.POST.get('Address')
            instance.Address2 = request.POST.get('Address2')
            new_image = request.FILES.get('Image')

            # Check if a new image is provided, if not, keep the current image
            if new_image:
                instance.Image = new_image
            
            instance.save()
            return HttpResponseRedirect(reverse('reservation_detail', args=[instance.id]))
        
        return render(request, 'update_reservation.html', {'instance': instance})
    else:
        # Handle the case where the user is not authenticated, e.g., redirect to a login page or show an error message
        return redirect('login')


def delete_reservation(request, pk):
    if request.user.is_authenticated:
        reservation = get_object_or_404(Reservation, id=pk)
        reservation.delete()
        messages.success(request,"Your Successful delete your detail")
        return redirect('viewlist')
    else:
        # Handle the case where the user is not authenticated, e.g., redirect to a login page or show an error message
        messages.error(request, "Please log in to access this page.")
        return redirect('login')  # Replace 'login' with your actual login view name

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')

