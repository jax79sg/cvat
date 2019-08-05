from django.db import models

# Create your models here.
class Download(models.Model):
   taskid = models.CharField(max_length=100, verbose_name='Task ID')
   #taskName = models.CharField(max_length=100, verbose_name='Task Name')
   annotFormat = models.CharField(max_length=100, verbose_name='Annotation Format')
   lastUpdate = models.CharField(max_length=100, verbose_name='Task last updated')
   download = models.CharField(max_length=1000, verbose_name='Download link')
   def get_absolute_url(self):
       filename=self.taskid+'_'+self.lastUpdate+'_'+self.annotFormat
       return "/downloadlist/?task="+filename
