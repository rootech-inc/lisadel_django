from django.db import models


# makemigrations app_name
# sqlmigrate app_name migration_number
# migrate

# Create your models here.
class tours(models.Model):
    tour_uni = models.CharField(max_length=250)
    title = models.TextField()
    overview = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    owner = models.TextField()
    eob = models.TextField()
    country = models.TextField()
    type = models.TextField()
    group_size = models.TextField()
    date_created = models.DateField()
    views = models.TextField()
    url_parse = models.TextField(default='none')

    def __str__(self):
        return self.title + ' - ' + self.tour_uni


class EventBooking(models.Model):
    client_name = models.TextField()
    event = models.TextField()
    phone_number = models.TextField()
    email_address = models.TextField()
    booking_package = models.TextField()
    payment = models.TextField()
    sits = models.TextField()
    special_request = models.TextField()
    country = models.TextField()
    region = models.TextField()
    city = models.TextField()
    loc = models.TextField()


class TourPackage(models.Model):
    event = models.TextField()
    description = models.TextField()
    cost = models.TextField()

    def __str__(self):
        return self.event + ' - ' + self.cost


class TourSchedule(models.Model):
    event = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.TextField()
    title = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.event + ' - ' + self.description


class TourGallery(models.Model):
    event = models.TextField()
    media_type = models.TextField()
    media_name = models.TextField()
    title = models.TextField()
    description = models.TextField()
    owner = models.TextField()
    date_added = models.DateField()

    def __str__(self):
        return self.title + ' - ' + self.media_name


class services(models.Model):
    title = models.TextField()
    description = models.TextField()
    img = models.TextField()
    owner = models.TextField()
    date_added = models.DateTimeField()
    url_parse = models.TextField(default='none')

    def __str__(self):
        return self.title + ' - ' + self.description


class team(models.Model):
    name = models.TextField()
    position = models.TextField()
    fb = models.TextField()
    twi = models.TextField()
    linked = models.TextField()
    img = models.TextField()
    date_added = models.DateTimeField()
    owner = models.TextField()

    def __str__(self):
        return self.name + ' - ' + self.position


class contact_us(models.Model):
    client_name = models.TextField()
    phone_number = models.TextField()
    email_address = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.client_name


class bookings(models.Model):
    client_name = models.TextField()
    event = models.TextField()
    phone_number = models.TextField()
    email_address = models.TextField()
    booking_package = models.TextField()
    country = models.TextField()
    region = models.TextField()
    city = models.TextField()
    loc = models.TextField()

    def __str__(self):
        return self.client_name + ' - ' + self.event
