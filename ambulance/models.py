from django.db import models
from PIL import Image

# Create your models here.
class Ambulance(models.Model):
  driver_name = models.CharField(max_length=255)
  driver_email = models.EmailField(max_length=50)
  driver_number = models.CharField(max_length=15)
  location = models.CharField(max_length=255)
  image = models.ImageField(upload_to='ambulances')

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
  number = models.CharField(max_length=15)
  location = models.CharField(max_length=255)

  def __str__(self):
    return self.name