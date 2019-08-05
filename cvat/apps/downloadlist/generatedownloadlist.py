from .models import Download
import glob
def getDownloadList():
   downloadlist=[]
   for zipfile in glob.glob('/home/django/data/**/.upload/*.zip', recursive=True):
      filename=zipfile.split("/")[-1].split(".")[0]
      fileelements=filename.split("_")
      taskid=fileelements[0]
      datetime=fileelements[1]+'_'+fileelements[2]
      annotformat=fileelements[3]
      downloadlist.append(Download(taskid=taskid, annotFormat=annotformat,lastUpdate=datetime,download=filename))
      print("Processed {}".format(zipfile))
   return downloadlist