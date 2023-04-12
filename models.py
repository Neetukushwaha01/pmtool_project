from django.db import models
# from user.models import User

# from django.contrib.auth.models import  User
# Create your models here.
from user.models import User


class ProjectDetails(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.TextField(null=False,blank=False)
    start_date = models.DateField(null=False,blank=False)
    due_date = models.DateField(null=False,blank=False)
    request_type = models.TextField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    loom_links = models.TextField(null=True,blank=True)
    no_of_pages = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class ProjectAttachment(models.Model):
    project = models.ForeignKey(ProjectDetails,on_delete=models.CASCADE,related_name = 'product_attachment')
    attachment = models.FileField(upload_to = 'attachment',null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)


class ProjectMember(models.Model):
    project = models.ForeignKey(ProjectDetails,on_delete=models.CASCADE,related_name = 'project_members')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=200,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


 # this code for viedo aad  start
class Loom_linkAdd(models.Model):
    Loom_videolink=models.URLField(max_length = 200)
    def __str__(self):
        return str(self.Loom_videolink)

class Attachment_viedoAdd(models.Model):
    Attachment_viedo=models.FileField(upload_to='files/upload')
    def __str__(self):
        return str(self.Attachment_viedo)



class ViedoProject(models.Model):
    TYPE_REQ=[
        ('Content Repurposing',"Content Repurposing"),
        ('Simple Video Edit',"Simple Video Edit"),
        ('Motion Graphics',"Motion Graphics"),
        ('Social Media Video Ad',"Social Media Video Ad"),
    ]

    project_title = models.TextField( null=False, blank=False )
    type_request=models.CharField(choices=TYPE_REQ, max_length=200)
    project_description=models.TextField( null=False, blank=False )
    Loom_linkAdd = models.ForeignKey(Loom_linkAdd, on_delete=models.CASCADE, related_name='Viedo_Project')
    Attachment_viedoAdd = models.ForeignKey(Attachment_viedoAdd, on_delete=models.CASCADE, related_name='Viedo_Project')


#this code for viedo aad  end