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

def generateannotations(taskList=None, annotFormat='voc'):
   print("[AnnotaionGen] Tasklist: {}, Format:{}".format(taskList, annotFormat))
   for task in taskList:
      #Getting annotation xml and details
      taskannotationxmlobj,xmlstring=webapis.getTaskAnnotationXML(task)
      sourcevideo = taskannotationxmlobj.getElementsByTagName('source')[0].firstChild.nodeValue
      print("[AnnotaionGen] Soucevideo: {}".format(sourcevideo))
      foldername=sourcevideo.split("/")[-1].split(".")[0]
      print("[AnnotaionGen] foldername: {}".format(foldername))
      folderpath=sourcevideo.split(foldername)[0]
      print("[AnnotaionGen] folderpath: {}".format(folderpath))
      
      #Generating the frames from video
      framesFolder=folderpath+foldername
      if (os.path.isdir(framesFolder)) == False:
         print("[AnnotaionGen] Folder does not exist, creating now")
         subprocess.call(['mkdir', framesFolder])
         subprocess.call(['ffmpeg', '-i', sourcevideo, '-vsync','0','-start_number','0', framesFolder+'/myxml_%08d.jpg'])
      
      
      
      
      
      