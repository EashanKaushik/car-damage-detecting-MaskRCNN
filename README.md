# car-damage-detecting-MaskRCNN
Car damage detection using Mask Regional Convolution Neural Network

# Project Introduction
- In this project I have developed a software that was able to detect four types of vehicle damages namely, Scratch, Dent, Dislocation and Shatter. Also I have provided a tentative repair cost for the type of damage detected. I have developed a website using Flask framework. Front end of the website is built using Bootstrap software.
- Automation is the next step in the automobile industry, and a software which is able to detect and localize damage in the car has various real world applications. In the software I have used Mask Regional Convolutional Network which is at the pinnacle of image detection techniques. Due to the complexity of the task I have used transfer learning to develop the software in three stages. Each stage added a new layer of complexity to the task, this helped the software prioritize learning the current task. I had also used Image Augmentation, which helped the model to not over fit the training data.

# Dataset
- Stage 1: https://www.kaggle.com/eashankaushik/car-damage-detectionstage1
- Stage 2: https://www.kaggle.com/eashankaushik/car-damage-detectionstage2
- Stage 3: https://www.kaggle.com/eashankaushik/car-damage-detection

# Model Training
For model training check out my medium post https://medium.com/analytics-vidhya/implement-your-own-mask-rcnn-model-65c994a0175d

# Image Annotation

<p align="center">
  <img src="https://user-images.githubusercontent.com/50113394/122675966-8302e900-d1f9-11eb-8623-3a94ac231d7a.png" />
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/50113394/122676009-9dd55d80-d1f9-11eb-99aa-7525630aa98b.png" />
</p>

# Annotated File

<p align="center">
  <img src="https://user-images.githubusercontent.com/50113394/122676016-a168e480-d1f9-11eb-97f4-dbde52f7821f.png" />
</p>

# Stages

1) Stage 1- In stage 1, I trained the model on 'Damage' class and, used images annotated with bounding boxes.
2) Stage 2- In this stage training was done using four classes: damage-1 (scratch), damage-2 (dent), damage-3 (shatter) and damage-4(dislocation), in this stage I used images annotated with bounding boxes as well.
3) Stage 3- Stage 3 used images annotated with polygons, and four classes namely Scratch, Dent, Shatter and Dislocation. 

# Hyper Parameter Values
- You can use the following hyper parameter values to train your model. I found these values to give the best results.

<p align="center">
  <img src="https://user-images.githubusercontent.com/50113394/122676039-bd6c8600-d1f9-11eb-88df-3e730925708a.png" />
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/50113394/122676047-c78e8480-d1f9-11eb-8d4e-72e526cd1719.png" />
</p>

# Model Output

<p align="center">
  <img src="https://user-images.githubusercontent.com/50113394/122676087-fa387d00-d1f9-11eb-9bd1-bf52dfc40932.png" />
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/50113394/122676106-13412e00-d1fa-11eb-852c-b96c5d0e57c1.png" />
</p>

# Deployment

<p align="center">
  <img src="https://user-images.githubusercontent.com/50113394/122676067-e12fcc00-d1f9-11eb-8ec7-4e704a47f83d.png" />
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/50113394/122676093-04f31200-d1fa-11eb-853e-202102a1b8e7.png" />
</p>

# Damage Localization

<p align="center">
  <img src="https://user-images.githubusercontent.com/50113394/122676130-27852b00-d1fa-11eb-8e92-2dfdcabd6457.png" />
</p>

# Training loss vs Validation loss

<p align="center">
  <img src="https://user-images.githubusercontent.com/50113394/122676186-82b71d80-d1fa-11eb-88cc-708786320ba3.png" />
</p>

# Steps to Implement the Project
1) Put your_trained_weights.m5 file in the model directory.
2) Change line #22 in app/utils.py to the name of the weights of your model.
3) Run main.py file and the website will be hosted on http://127.0.0.1:5000/. Following are the URL rules I developed, you can add or delete these rules according to your preference.
 ```python
app.add_url_rule('/base','base',views.base)
app.add_url_rule('/','index',views.index)
app.add_url_rule('/damageapp','damageapp',views.damageapp)
app.add_url_rule('/damageapp/damage','damage',views.damage,methods=['GET','POST'])
```
If you don’t want to use cost assessment functionality, just change cost_for_damage variable on line #45 of app/views.py to False. Cost assessment functionality is just for visual purposes and computes cost based on size of mask to size of image ratio.

# Reference

[1] matterport/Mask_RCNN. (2021). Retrieved 1 January 2021, from https://github.com/matterport/Mask_RCNN

# Connect 

Connect with me on linkedin if you have some doubts regarding the training and deployment of the project.
- https://www.linkedin.com/in/eashan-kaushik-7b4454168/
