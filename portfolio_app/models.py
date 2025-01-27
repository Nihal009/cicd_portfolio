from django.db import models

# Create your models here.
class bio(models.Model):
    profile_pic=models.ImageField(upload_to='profile_pics/',null=True,blank=True)
    description=models.TextField(max_length=1000,null=True,blank=True)

    def __str__(self):
        return "Profile Bio"
    
class projects(models.Model):
    project_thumbnail=models.ImageField(upload_to='project_thumbnails/')
    Title=models.CharField(max_length=255)
    url=models.URLField()
    project_description=models.TextField()
    # tools=models.JSONField(default=list,null=True)

    def __str__(self):
        return self.Title