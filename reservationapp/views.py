from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login,logout
from . forms import ReservationForm,ReservationUpdateForm
from django.contrib import messages
from . models import Reservation
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
        # User is logged in, allow access to the reservation list
        reservations = Reservation.objects.all()

        # Create a Paginator instance with the reservations and set the number of items per page
        paginator = Paginator(reservations, 10)  # Show 10 reservations per page

        page = request.GET.get('page')
        try:
            reservations = paginator.page(page)
        except PageNotAnInteger:
            # If the page is not an integer, deliver the first page.
            reservations = paginator.page(1)
        except EmptyPage:
            # If the page is out of range (e.g., 9999), deliver the last page.
            reservations = paginator.page(paginator.num_pages)

        context = {
            'reservations': reservations,
        }
        return render(request, 'showList.html', context)
    else:
        # User is not logged in, handle accordingly
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
        reservation = get_object_or_404(Reservation, id=pk)

        if request.method == 'POST':
            form = ReservationUpdateForm(request.POST, instance=reservation)

            if form.is_valid():
                form.save()
                messages.success(request, "Your details have been successfully updated.")
                return redirect('viewlist')
            else:
                messages.error(request, "Please correct the errors below.")

        else:
            form = ReservationUpdateForm(instance=reservation)

        context = {
            'form': form,
        }

        return render(request, 'update_reservation.html', context)
    else:
        # Handle the case where the user is not authenticated, e.g., redirect to a login page or show an error message
        messages.error(request, "Please log in to access this page.")
        return redirect('login')  # Replace 'login' with your actual login view name

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

