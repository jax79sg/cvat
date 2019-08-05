
from .models import Download
Download.objects.bulk_create([Download(taskid='1', annotFormat='VOC', taskName='First task',lastUpdate='1st Jun 2012',download='http://localhost/sd.zip"), Download(download='BBB')])


