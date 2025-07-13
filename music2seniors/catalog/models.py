from django.db import models

# Create your models here.
from django.urls import reverse 


class performer(models.Model):
    """Model representing a musician."""
    first_name = models.CharField(
        max_length=100,
        unique=False,
        help_text="performer first name"
    )
    last_name = models.CharField(max_length=100)

    email = models.CharField(max_length=100)

    instrument = models.CharField(
        max_length=100,
        unique=False,
        null = True)

    des = models.TextField(max_length= 2000, null = True, default='')

    def __str__(self):
        """String for representing the Model object."""
        return self.first_name + ' ' + self.last_name
    
    def get_absolute_url(self):
        """Returns the url to access a particular performer."""
        return reverse('performer-detail', args=[str(self.id)])
    

class senior_home(models.Model):
    """Model representing a senior home."""
    name = models.CharField(max_length=200)

    email = models.CharField(max_length=200)

    phone = models.CharField(max_length=50, null = True)

    contact = models.CharField(max_length=200, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
    def get_absolute_url(self):
        """ Returns the url to access a particular senior home."""
        return reverse('senior_home-detail', args=[str(self.id)])
    
import datetime

class enquiry(models.Model):
    """ Model representing a enquiry."""
    about = models.CharField(
        max_length=100,
        unique=False,
        help_text="performer or senior home"
    )
    first_name = models.CharField(
        max_length=100,
        unique=False,
        default='',
        help_text="first name"
    )
    last_name = models.CharField(
        max_length=100,
        unique = False,
        default = '',
        help_text="Last Name"
                                )

    email = models.CharField(max_length=100)
    
    inquiry = models.TextField(
        max_length= 2000, 
        null = False, 
        default=''
        )
    
    submitted = models.DateTimeField(auto_now_add=True)
      
    def __str__(self):
        """String for representing the Model object."""
        return self.about
    
    def get_absolute_url(self):
        """ Returns the url to access a particular enquiry."""
        return reverse('enquiry-detail', args=[str(self.id)])
    