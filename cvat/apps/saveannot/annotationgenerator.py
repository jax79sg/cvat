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
basepath='/home/django/data/'

def generateannotations(taskList=None, annotFormat='voc'):
   print("[AnnotaionGen] Tasklist: {}, Format:{}".format(taskList, annotFormat))
   for task in taskList:
      #Getting annotation xml and details
      taskannotationxmlobj,xmlstring=webapis.getTaskAnnotationXML(task)
      mode = taskannotationxmlobj.getElementsByTagName('mode')[0].firstChild.nodeValue.lower()   
      print("[AnnotaionGen] Mode: {}".format(mode))
      if mode=='annotation':
         taskannotationxmlobj,xmlstring=webapis.getTaskAnnotationXMLforImages(task)
      
      folderpath=basepath+task+'/.upload/'
      print("[AnnotaionGen] folderpath: {}".format(folderpath))
      #Creating the xml file
      xmlfile=folderpath+task+".xml"
      f=open(xmlfile, "w")
      f.write(xmlstring)
      f.close()
      
      if mode=='interpolation':
         sourcevideo = taskannotationxmlobj.getElementsByTagName('source')[0].firstChild.nodeValue
         print("[AnnotaionGen] Soucevideo: {}".format(sourcevideo))
         
         framesFolder=folderpath+'JPEGImages'
         if (os.path.isdir(framesFolder)) == False:
            print("[AnnotaionGen] Folder does not exist, creating now")
            subprocess.call(['mkdir', framesFolder])
            videopath=folderpath+sourcevideo
            subprocess.call(['ffmpeg', '-i', videopath, '-vsync','0','-start_number','0', framesFolder+'/'+task+'_%08d.jpg'])
      elif mode=='annotation':
         framesFolder=folderpath+'JPEGImages'
         if (os.path.isdir(framesFolder)) == False:
            print("[AnnotaionGen] Folder does not exist, creating now")
            subprocess.call(['mkdir', framesFolder])
         imgfolder=folderpath+'*.jpg'
         print("[Annot] cp -v "+imgfolder+ " " + framesFolder)
         subprocess.call("cp -v "+imgfolder+ " " + framesFolder, shell=True)
         imgfolder=folderpath+'*.png'
         print("[Annot] cp -v "+imgfolder+ " " + framesFolder)
         subprocess.call("cp -v "+imgfolder+ " " + framesFolder, shell=True)
      taskupdateddate = taskannotationxmlobj.getElementsByTagName('updated')[0].firstChild.nodeValue
      taskupdateddate=dateutils.converttolocalzone(taskupdateddate)
      
      
      
      
      
      #foldername=sourcevideo.split("/")[-1].split(".")[0]
      #print("[AnnotaionGen] foldername: {}".format(foldername))
      
      

	  
      
      #Generating the frames from video
      
      #Calling converter
      if (annotFormat=='1'):
         #voc
         vocxml=folderpath+'Annotations'
         vocjpeg=folderpath+'JPEGImages'
         subprocess.call(['rm','-r', vocxml])
         subprocess.call(['python3', '/home/django/cvat/utils/voc/converter.py', '--cvat-xml',xmlfile,'--image-dir',framesFolder,'--output-dir',vocxml])                  
         subprocess.call(['zip', '-r','-0', folderpath+task+'_'+taskupdateddate+'_VOC.zip', vocxml,vocjpeg])
        
      
      
      