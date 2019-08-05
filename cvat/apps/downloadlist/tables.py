import django_tables2 as tables
from .models import Download
class DownloadTable(tables.Table):
        taskid = tables.Column(attrs={'tf': {'bgcolor': 'red'}})
        #taskName = tables.Column(attrs={'tf': {'bgcolor': 'red'}})
        annotFormat = tables.Column(attrs={'tf': {'bgcolor': 'red'}})
        lastUpdate = tables.Column(attrs={'tf': {'bgcolor': 'red'}})
        download = tables.Column(linkify=True,attrs={'tf': {'bgcolor': 'red'}})
        #class Meta:
        #    model = Download