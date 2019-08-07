# Computer Vision Annotation Tool (CVAT)

[![Build Status](https://travis-ci.org/opencv/cvat.svg?branch=develop)](https://travis-ci.org/opencv/cvat)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/840351da141e4eaeac6476fd19ec0a33)](https://app.codacy.com/app/nmanovic/cvat?utm_source=github.com&utm_medium=referral&utm_content=opencv/cvat&utm_campaign=Badge_Grade_Settings)
[![Gitter chat](https://badges.gitter.im/opencv-cvat/gitter.png)](https://gitter.im/opencv-cvat)
[![Coverage Status](https://coveralls.io/repos/github/opencv/cvat/badge.svg?branch=)](https://coveralls.io/github/opencv/cvat?branch=develop)

CVAT is free, online, interactive video and image annotation tool for computer vision. It is being used by our team to annotate million of objects with different properties. Many UI and UX decisions are based on feedbacks from professional data annotation team.

![CVAT screenshot](cvat/apps/documentation/static/documentation/images/cvat.jpg)

## DH Documentation
This is a fork of [opencv/cvat](https://github.com/opencv/cvat). This fork is on parallel maintanence with the original master, with exception to use cases that's particular to our requirements. All documentation outside of this section belongs to the master repository.  
A demo is available at http://jax79sg.hopto.org:8080.  
Download of annotations in VOC format available in http://jax79sg.hopto.org:8080/downloadlist

### Installation with Internet access
1. Download docker-compose.internet.yml from https://raw.githubusercontent.com/jax79sg/cvat/develop/docker-compose.internet.yml  
2. Run following commands
```
docker-compose -f docker-compose.internet.yml up --force-recreate -d
docker-compose exec cvat python3 manage.py makemigrations downloadlist
docker-compose exec cvat python3 manage.py migrate downloadlist

## Create a super user
docker exec -it cvat bash -ic 'python3 ~/manage.py createsuperuser'
```
4. Access http://youripaddress:8080 on your Chrome browser.  


### Installation without Internet
You will need to perform some steps on an internet connected machine before you transfer it to the standalone machine.    


On the Internet machine
1. Pull the pre-made images
```
docker pull quay.io/jax79sg/cvat
docker pull quay.io/jax79sg/redis
docker pull quay.io/jax79sg/postgres
```
2. Tag the images to local version
```
docker tag quay.io/jax79sg/cvat cvat:dh
docker tag quay.io/jax79sg/redis redis:dh
docker tag quay.io/jax79sg/postgres postgres:dh
```
3. Tar the images 
```
docker save cvat:dh -o cvat.tar
docker save redis:dh -o redis.tar
docker save postgres:dh -o postgres.tar
```
4. Download docker-compose.standalone.yml from https://raw.githubusercontent.com/jax79sg/cvat/develop/docker-compose.standalone.yml  
5. Copy the following files into a portable HDD and transfer them to the standalone machine. 
```
cvat.tar
redis.tar
postgres.tar
docker-compose.standalone.yml
```

On standalone machine
1. Copy the 4 files in step 5 into a empty folder. 
2. Load the images into Docker, then check if they are loaded 
```
docker load -i postgres.tar
docker load -i redis.tar
docker load -i cvat.tar

docker images
```
3. Install and run CVAT
```
docker-compose -f docker-compose.standalone.yml up --force-recreate -d
docker-compose exec cvat python3 manage.py makemigrations downloadlist
docker-compose exec cvat python3 manage.py migrate downloadlist

## Create a super user
docker exec -it cvat bash -ic 'python3 ~/manage.py createsuperuser'
```
4. Access http://localhost:8080 on your Chrome browser.  

## Documentation

- [Installation guide](cvat/apps/documentation/installation.md)
- [User's guide](cvat/apps/documentation/user_guide.md)
- [XML annotation format](cvat/apps/documentation/xml_format.md)
- [AWS Deployment Guide](cvat/apps/documentation/AWS-Deployment-Guide.md)
- [Questions](#questions)

## Screencasts

- [Introduction](https://youtu.be/L9_IvUIHGwM)
- [Annotation mode](https://youtu.be/6h7HxGL6Ct4)
- [Interpolation mode](https://youtu.be/U3MYDhESHo4)
- [Attribute mode](https://youtu.be/UPNfWl8Egd8)
- [Segmentation mode](https://youtu.be/Fh8oKuSUIPs)
- [Tutorial for polygons](https://www.youtube.com/watch?v=XTwfXDh4clI)
- [Semi-automatic segmentation](https://www.youtube.com/watch?v=vnqXZ-Z-VTQ)

## Supported annotation formats

Format selection is possible after clicking on the Upload annotation / Dump annotation button.

| Annotation format         | Dumper | Loader |
| ------------------------- | ------ | ------ |
| CVAT XML v1.1 for images  | X      | X      |
| CVAT XML v1.1 for a video | X      | X      |
| Pascal VOC                | X      | X      |
| YOLO                      | X      | X      |

## Links
- [Intel AI blog: New Computer Vision Tool Accelerates Annotation of Digital Images and Video](https://www.intel.ai/introducing-cvat)
- [Intel Software: Computer Vision Annotation Tool: A Universal Approach to Data Annotation](https://software.intel.com/en-us/articles/computer-vision-annotation-tool-a-universal-approach-to-data-annotation)
- [VentureBeat: Intel open-sources CVAT, a toolkit for data labeling](https://venturebeat.com/2019/03/05/intel-open-sources-cvat-a-toolkit-for-data-labeling/)

## Online Demo

[Onepanel](https://www.onepanel.io/) has added CVAT as an environment into their platform and a running demo of CVAT can be accessed at [CVAT Public Demo](https://c.onepanel.io/onepanel-demo/projects/cvat-public-demo/workspaces).

After you click the link above:

- Click on "GO TO WORKSPACE" and the CVAT environment will load up
- The environment is backed by a K80 GPU

If you have any questions, please contact Onepanel directly at support@onepanel.io. If you are in the Onepanel application, you can also use the chat icon in the bottom right corner.

## LICENSE

Code released under the [MIT License](https://opensource.org/licenses/MIT).

## Questions

CVAT usage related questions or unclear concepts can be posted in our
[Gitter chat](https://gitter.im/opencv-cvat) for **quick replies** from
contributors and other users.

However, if you have a feature request or a bug report that can reproduced,
feel free to open an issue (with steps to reproduce the bug if it's a bug
report).

If you are not sure or just want to browse other users common questions,
[Gitter chat](https://gitter.im/opencv-cvat) is the way to go.
