from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group, Permission
from django.urls import reverse 




class Module(models.Model):
    name = models.TextField(max_length = 100)
    code = models.CharField(max_length = 5)
    credit = models.CharField(max_length = 5)
    category = models.CharField(max_length = 100, choices = [('Humanities', 'Humanities'),
                                                            ('Social Sciences', 'Social Sciences'), 
                                                            ('Natural Sciences', 'Natural Sciences'), 
                                                            ('Mathematics and Satistics', 'Mathematics and Statistics'), 
                                                            ('Computer Science and Information Technology', 'Computer Science and Information Technology'),
                                                            ('Engineering', 'Engineering'),
                                                            ('Health Sciences', 'Health Sciences'), 
                                                            ('Business and Economics', 'Business and Economics'), 
                                                            ('Fine Arts', 'Fine Arts'), 
                                                            ('Law', 'Law'), 
                                                            ('Languages and Linguistics', 'Languages and Linguistics'), 
                                                            ('Architecture', 'Architecture')])
    description = models.TextField()
    availability = models.CharField(max_length = 100, choices = [('Open', 'Open'), ('Closed', 'Closed')])
    courses = models.ManyToManyField(Group)

    def __str__(self):
        return f'{self.name}'
    def get_absolute_url(self):
        return reverse('itreporting:module-detail', kwargs = {'pk' : self.pk})
    
    
class Registration(models.Model):
    student = models.ForeignKey(User, related_name = 'registrations', on_delete = models.CASCADE)
    module = models.ForeignKey(Module, related_name = 'registrations', on_delete = models.CASCADE)
    date_of_registration = models.DateField(default = timezone.now)

