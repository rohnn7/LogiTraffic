from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model() #This brings whole usermodel to the variable defined

# Create your models here.
#this is basically the extended version of User class
#some of fields were already there in User Model but to overwrite them i used them again
#like first_name, last_name, email and is_active
class UserExtended(models.Model):
    user = models.OneToOneField(User, default=1, related_name='user', on_delete=models.CASCADE)
    user_image = models.ImageField(upload_to='UserProfilePic')
    email = models.EmailField(blank=False, null=False)
    first_name = models.CharField(blank=False, max_length=150)
    last_name = models.CharField(blank=False, max_length=150)
    mobile = models.CharField(blank=False, max_length=15)
    is_active = models.BooleanField(default=True) #instead of deleting the column we will turn is_active=False      
    def __str__(self):
       return self.user.username

    #function to make is_active false
    def delete_user(self):
       self.is_active = False
       self.save()

   # def delete_user_pk(self):
   #    self.user.Active = False
   #    self.save()





