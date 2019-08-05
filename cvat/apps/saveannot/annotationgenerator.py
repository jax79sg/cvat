'''
Receives list of tasks, and annotation format
For each task, 
	- pull the video source
	- extract the frames
	- Run the convertor for format
	- zip the output into task_lastupdate.zip
	- put into shared folder
	- redirect to download page
'''
from . import webapis
from xml.dom import minidom
import os
import subprocess
from . import dateutils

def generateannotations(taskList=None, annotFormat='voc'):
   print("[AnnotaionGen] Tasklist: {}, Format:{}".format(taskList, annotFormat))
   for task in taskList:
      #Getting annotation xml and details
      taskannotationxmlobj,xmlstring=webapis.getTaskAnnotationXML(task)
      sourcevideo = taskannotationxmlobj.getElementsByTagName('source')[0].firstChild.nodeValue
      taskupdateddate = taskannotationxmlobj.getElementsByTagName('updated')[0].firstChild.nodeValue
      deleteme=taskupdateddate
      taskupdateddate=dateutils.converttolocalzone(taskupdateddate)
      print("[AnnotaionGen] Soucevideo: {}".format(sourcevideo))
      foldername=sourcevideo.split("/")[-1].split(".")[0]
      print("[AnnotaionGen] foldername: {}".format(foldername))
      folderpath=sourcevideo.split(foldername)[0]
      print("[AnnotaionGen] folderpath: {}".format(folderpath))

	  #Creating the xml file
      xmlfile=folderpath+task+".xml"
      f=open(xmlfile, "w")
      f.write(xmlstring)
      f.close()
      
      #Generating the frames from video
      framesFolder=folderpath+'JPEGImages'
      if (os.path.isdir(framesFolder)) == False:
         print("[AnnotaionGen] Folder does not exist, creating now")
         subprocess.call(['mkdir', framesFolder])
         subprocess.call(['ffmpeg', '-i', sourcevideo, '-vsync','0','-start_number','0', framesFolder+'/'+task+'_%08d.jpg'])
      
      #Calling converter
      if (annotFormat=='1'):
         #voc
         vocxml=folderpath+'Annotations'
         vocjpeg=folderpath+'JPEGImages'
         subprocess.call(['rm','-r', vocxml])
         subprocess.call(['python3', '/home/django/cvat/utils/voc/converter.py', '--cvat-xml',xmlfile,'--image-dir',framesFolder,'--output-dir',vocxml])                  
         subprocess.call(['zip', '-r','-0', folderpath+task+'_'+taskupdateddate+'_VOC.zip', vocxml,vocjpeg])
         
      print(deleteme)
      
      
      