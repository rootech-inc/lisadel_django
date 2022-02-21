from django import forms


class EventBookingForm(forms.Form):
    package = forms.CharField(max_length=100)
    fullName = forms.CharField(max_length=200)
    emailAddress = forms.CharField(max_length=200)
    phoneNumber = forms.CharField(max_length=200)
    event = forms.CharField(max_length=200)
    eventTitle = forms.CharField(max_length=200)


class contactUsForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email_address = forms.EmailField(max_length=100)
    phone_number = forms.CharField(max_length=20)
    message = forms.CharField()


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
