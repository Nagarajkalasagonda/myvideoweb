from django.db import models
from django.contrib.auth.models import User

# Create your models here.

video_category=(
('Animation','Animation'),
('English','English'),
('Hindi','Hindi'),    
('Kannada','Kannada'),    
)
#User Registeration Model
class UserReg(models.Model):
    #user = models.OneToOneField(User,null=True,on_delete=models.PROTECT)
    user = models.OneToOneField(User,null=True,on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    def __str__(self):
        return self.name

#Video Creation model
class Videos(models.Model):
    title = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=500,null=True,blank=True)
    tag = models.CharField(max_length=100,null=True,blank=True)
    owner = models.ForeignKey(UserReg,on_delete=models.PROTECT,null=True,blank=True)
    referenceid = models.CharField(max_length=50,null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    lastdate=models.DateTimeField(null=True,blank=True)
    video = models.FileField(null=True,blank=True,upload_to='v_files')
    category = models.CharField(max_length=20,choices=video_category,null=True,blank=True)
    def __str__(self):
        return self.title