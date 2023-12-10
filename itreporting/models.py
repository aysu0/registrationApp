from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group, Permission
from django.urls import reverse 
from django.contrib.contenttypes.models import ContentType



                                                                                                   


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


    def __str__(self):
        return f'{self.name}'
    def get_absolute_url(self):
        return reverse('itreprting:module-form', kwargs = {'pk' : self.pk})
    
    
class Course(models.Model):
    name = models.CharField(max_length = 50)       
    modules = models.ManyToManyField(Module)


    def __str__(self):
        return f'{self.name}'
    def get_absolute_url(self):
        return reverse('itreprting:course-form', kwargs = {'pk' : self.pk})

class CourseGroup(Group):
    description = models.TextField(blank=True)


# content_type = ContentType.objects.get_for_model(MyModel)
# permission = Permission.objects.create(
#     codename='custom_permission',
#     name='Can access custom feature',
#     content_type=content_type
# )

# group = Group.objects.create(name='My Group')
# group.permissions.add(permission)

# user = User.objects.get(username='john')
# user.groups.add(group)