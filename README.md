# YOLOV4 Custom Object Detector Google Colab 

In this article, I will describe how to train our own object detection model.
I chose Boston Dynamics' Spot robot as my object.

git clone https://github.com/AlexeyAB/darknet.git

You need to make GPU, CUDNN and OPENCV = 1 in Darknet Makefile folder .

![Alt text](https://miro.medium.com/max/730/1*6V3QMS8ftqDrXItXk2GHmg.jpeg "img0")

Save and close the folder.

Since we will use the transfer learning method during the training phase, we will download some files:


yolov4.conv.137 https://drive.google.com/file/d/1JKF-bdIklxOOVy-2Cr5qdvjgGpmGfcbp/view
and  
yolov4.weights https://drive.google.com/file/d/1cewMfusmPjYWbrnuJRuKhPMwRe_b9PaT/view

You need to add both files inside Darknet.

 spot_yolov4.cfg --> add this file inside darknet
 
 
 Collect Images and rename as 1.jpg, 2.jpg.....
 
 I will save 400 photos. If you can't find enough photos in Google images, you can take a frame-by-frame screenshot by opening a video about the object you want to detect.
 
 Now I edit the extensions of the images I found and convert them to jpg format. (code is in tojpg file)
 
 
PICTURE LABELING

From here I go to the site. https://www.makesense.ai/
I click on get started. I select the folder with the images I will upload, click on one of the photos and press CTRL+A to select all the photos and upload them.

![Alt text](https://miro.medium.com/max/831/1*tE4y87nrW84e5lB2LjsGbA.jpeg "img1")


![Alt text](https://miro.medium.com/max/581/1*u8HEZENymmoaV2AbTTgaTg.jpeg "img2")

![Alt text](https://miro.medium.com/max/624/1*oQq4KR1WO_Bp-ppcDVcYHw.jpeg "img3")





RESULTS:
https://www.youtube.com/watch?v=XPbgrsLuC9Q&t=2s

<img src="https://j.gifs.com/lRMwx1.gif" width="600" height="400" />

