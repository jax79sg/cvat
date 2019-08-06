from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Download
from .tables import DownloadTable
from django.http import HttpResponse, Http404
from . import generatedownloadlist
import os

def download(request):
    #return render(request, 'downloadlist/downloadlist.html', {'download': Download.objects.all()})
    if request.GET.get('task', '')=='':
        Download.objects.all().delete()
        downloads=generatedownloadlist.getDownloadList()
        Download.objects.bulk_create(downloads)
        table = DownloadTable(Download.objects.all())
        table.paginate(page=request.GET.get('page', 1), per_page=15)

        return render(request, 'downloadlist/downloadlist.html', {
            'table': table
        })
    else:
        filetodownload=request.GET.get('task', '')
        taskid=filetodownload.split("_")[0]
        file_path = '/home/django/data/'+taskid+"/.upload/"+filetodownload+'.zip'
        print("Attempt to download: {}".format(file_path))
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/zip")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response
        raise Http404
