from django.db import models
from PIL import Image
from phonenumber_field.modelfields import PhoneNumber, PhoneNumberField
from .phone_number_validators import validate_possible_number


# Create your models here.
class PossiblePhoneNumberField(PhoneNumberField):
    default_validators = [validate_possible_number]


class Ambulance(models.Model):
    driver_name = models.CharField(max_length=255)
    driver_email = models.EmailField(max_length=50)
    driver_number = PossiblePhoneNumberField(blank=True, default="")
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='ambulances', null=True, blank=True)

    def __str__(self):
        return self.driver_name

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Ambulance_hire(models.Model):
    ambulance = models.ForeignKey(Ambulance, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    number = PossiblePhoneNumberField(blank=True, default="")
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name
