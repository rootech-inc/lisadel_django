from django.core.mail import send_mail
from django.shortcuts import render
from django.template import loader
from django.shortcuts import render
from django.http import Http404
import datetime

# Create your views here.
from django.http import HttpResponse
from .models import *
from .forms import *


def h_test(text):
    return HttpResponse("<h1>" + str(text) + "</h1>")


def home(request):
    all_services = services.objects.all()
    team_members = team.objects.all()
    home_events = tours.objects.all()[:6]
    page_description = 'Lisadel Travel & Tours is a well-established travel Agency that’s specializes in Tour ' \
                       'packages all over the world, Hotel Reservation, Airline Ticketing With experienced staff ' \
                       'members in handling inbound and outbound holidays and reservations. '
    context = {
        'home_events': home_events,
        'all_services': all_services,
        'team_members': team_members,
        'page_description': page_description[0:300]
    }
    return render(request, 'home/index.html', context)


def all_services(request):
    all_services = services.objects.all()
    page_description = ""

    for x_ser in all_services:
        page_description += " | " + str(x_ser.title)
    if len(page_description) < 100:
        page_description = 'Best Travel and Tour in Ghana, Appointment Booking, Assistance in filling the application ' \
                           'form, Vetting of supporting documents. '
    context = {
        'services': all_services, 'title': 'Services',
        'page_description': 'Best Travelling Services including ' + str(page_description),
    }
    return render(request, 'home/services.html', context)


def service(request, value):
    try:
        single_service = services.objects.get(url_parse=value)

    except tours.DoesNotExist:
        return Http404("Event Does Nt Exist")
    all_services = services.objects.all()
    if len(single_service.description) < 100:
        page_description = 'Best Travel and Tour in Ghana, Appointment Booking, Assistance in filling the application ' \
                           'form, Vetting of supporting documents. '
    else:
        page_description = single_service.description[0:320]
    context = {
        'title': "Services | " + str(single_service.title[0:20]),
        'service': single_service,
        'all_services': all_services,
        'page_description': str(page_description),
    }

    return render(request, 'home/service.html', context)


def events(request):
    home_events = tours.objects.all()[:6]
    context = {
        'title': 'Events',
        'home_events': home_events
    }
    return render(request, 'home/events.html', context)


def single_event(request, value):
    try:
        event = tours.objects.get(url_parse=value)
    except tours.DoesNotExist:
        return Http404("Event Does Nt Exist")
    # get packages
    event_title = event.title
    from home.forms import EventBookingForm

    packages = TourPackage.objects.filter(event=event.tour_uni)
    schedules = TourSchedule.objects.filter(event=event.tour_uni)
    event_days = event.start_date - datetime.date.today()
    gall = TourGallery.objects.filter(event=event.tour_uni)
    form = EventBooking()

    if len(event.overview) < 100:
        page_description = 'Best Travel and Tour in Ghana, Appointment Booking, Assistance in filling the application ' \
                           'form, Vetting of supporting documents. '
    else:
        page_description = event.overview[0:320]

    context = {'event': event,
               'packages': packages,
               'schedules': schedules,
               'event_days': event_days,
               'event_images': gall,
               'title': " Events | " + str(event.title),
               'page_description': page_description,
               'form': form
               }
    # todo get proper event date
    return render(request, 'home/single_event.html', context)


# bookings form
def event_booking(request):
    fullname = 'none'
    from home.forms import EventBookingForm
    if request.method == 'POST':
        # get for dat
        booking_form = EventBooking(request.POST)
        if booking_form.is_valid():
            fullname = booking_form.fullName

    else:
        booking_form = EventBooking()

    return render(request, 'home/process_booking.html', {'fullname': fullname})


def robot(request):
    return render(request, 'home/robots.txt')


# contact us form
def contactUs(request):
    if request.method == 'POST':
        form = contactUsForm(request.POST)
        if form.is_valid():
            # get data
            full_name = form.cleaned_data['full_name']
            email_address = form.cleaned_data['email_address']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']

            combined_message = "There is a message from " + str(full_name) + "\n" + "Sender : " + str(full_name) + \
                               "\nEmail Address : " + str(email_address) + "\n" + "Phone Number : " + str(
                phone_number) + "\n" + "Message : " + str(message)

            ## send data to db
            contact = contact_us(client_name=full_name, email_address=email_address, phone_number=phone_number,
                                 message=message)

            subject = 'Contact From Website'
            sender = 'robot'
            recipients = ['rootbackup10@gmail.com']

            if send_mail(subject, combined_message, sender, recipients, fail_silently=False):
                contact.save()
                return render(request, 'booking_successful.html')
            else:
                return Http404


        else:
            return Http404


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        from django.core.mail import send_mail
        # create a form instance and populate it with data from the request:
        form = EventBookingForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            package = form.cleaned_data['package']
            fullName = form.cleaned_data['fullName']
            emailAddress = form.cleaned_data['emailAddress']
            phoneNumber = form.cleaned_data['phoneNumber']
            event = form.cleaned_data['event']
            eventTitle = form.cleaned_data['eventTitle']

            booking_details = "Event : " + str(eventTitle) + "\nCustomer : " + str(
                fullName) + "\nEmail Address : " + str(emailAddress) + "\nPhone Number : " + str(
                phoneNumber) + "\nPackage : " + str(package)

            loc = 'none'

            subject = 'Event Booking'
            message = str(booking_details)
            sender = 'bramadusah@gmail.com'
            recipients = ['rootbackup10@gmail.com']

            if emailAddress:
                recipients.append(emailAddress)

            # if send_mail(subject, message, sender, recipients, fail_silently=False):
            if 10 > 1:
                # insert into database
                thisBook = bookings(client_name=fullName, event=event, phone_number=phoneNumber,
                                    email_address=emailAddress, booking_package=package, city=loc, country=loc,
                                    region=loc, loc=loc)
                thisBook.save()
                return render(request, 'booking_successful.html', {'event': eventTitle})
            else:
                return HttpResponse('Count not send email to ' + str(recipients))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
