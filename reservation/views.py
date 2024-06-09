from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic, View
from django.contrib import messages
from .models import Reservation
from .forms import ReservationForm

def table_reservation(request):
    """
    Lets user create a Reservation
    """
    reservation_form = ReservationForm () 

    if request.method == 'POST':
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            reservation_form.instance.name = request.user
            reservation_form.save()
            messages.success(request, 'Reservation successful.')
            return redirect(reverse('reservation:manage_reservation'))
        else:
            messages.error(request, 'Reservation unsuccessful. Please try again.')
    else:
        reservation_form = ReservationForm()

    context = {
        'form': reservation_form
    }
    return render(request, '../templates/reservation.html', context)



class ReservationList(generic.View):
    """
    Customer will be able to view their reservation/s
    """
    model = Reservation
    queryset = Reservation.objects.all()
    template_name = 'manage_reservation.html'
    paginate_by = 3

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            reservation = Reservation.objects.filter(name=request.user)
 
            
            context = {
                'reservation': reservation,
            }

            return render(request, '../templates/manage_reservation.html', context)



def edit_reservation(request, reservation_id):
    """
    Lets user updated their reservation
    """
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        reservation_form = ReservationForm(request.POST, instance=reservation)
        if reservation_form.is_valid():
            reservation_form.save()
            messages.success(request, 'Reservation updated successfully.')
            return redirect('reservation:manage_reservation')
        else:
            messages.error(request, 'Update unsuccessful. Please try again.')

    reservation_form = ReservationForm(instance=reservation)

    return render(request, 'edit_reservation.html', {'form': reservation_form})


def delete_reservation(request, reservation_id):
    """
    Lets user delete their reservation
    """
    reservation = get_object_or_404(Reservation, id=reservation_id)
    reservation.delete()
    messages.success(request, 'Reservation deleted successfully.')
    return redirect('reservation:manage_reservation')