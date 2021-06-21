# car-damage-detecting-MaskRCNN
Car damage detection using Mask Regional Convolution Neural Network

# Project Introduction
- In this project I develop a software that will be able to detect four types of vehicle damages namely, Scratch, Dent, Dislocation and Scatter. Also I will provide a tentative repair cost for the type of damage detected. We will develop a website using Flask framework. Front end of the website is built using Bootstrap software.
- Automation is the next step in the automobile industry, and a software able to detect and localize damage in the car has various real world application. In the software I have used Mask Regional Convolutional Network which is at the pinnacle of image detection techniques. Due to the complexity of the task we have used transfer learning to develop the software in three stages. Each stage adds a new layer of complexity to the task, this helps the software prioritize learning the current task. We have also used Image Augmentation, which helps the model to not over fit the training data.  We have also used various hyperparameter values which helps in finding their ideal values.

# Dataset
- Stage 1: https://www.kaggle.com/eashankaushik/car-damage-detectionstage1
- Stage 2: https://www.kaggle.com/eashankaushik/car-damage-detectionstage2
- Stage 3: https://www.kaggle.com/eashankaushik/car-damage-detection

# Image Annotation
<br>![image](https://user-images.githubusercontent.com/50113394/122675966-8302e900-d1f9-11eb-8623-3a94ac231d7a.png)
- ![image](https://user-images.githubusercontent.com/50113394/122676009-9dd55d80-d1f9-11eb-99aa-7525630aa98b.png)

# Annotated File
- ![image](https://user-images.githubusercontent.com/50113394/122676016-a168e480-d1f9-11eb-97f4-dbde52f7821f.png)

# Hyper Parameter Values
- You can use the following hyper parameter values to train your model. I found these values to give the best results.
- ![image](https://user-images.githubusercontent.com/50113394/122676039-bd6c8600-d1f9-11eb-88df-3e730925708a.png)
- ![image](https://user-images.githubusercontent.com/50113394/122676047-c78e8480-d1f9-11eb-8d4e-72e526cd1719.png)

# Model Output
- ![image](https://user-images.githubusercontent.com/50113394/122676087-fa387d00-d1f9-11eb-9bd1-bf52dfc40932.png)
- ![image](https://user-images.githubusercontent.com/50113394/122676106-13412e00-d1fa-11eb-852c-b96c5d0e57c1.png)

# Deployment
- ![image](https://user-images.githubusercontent.com/50113394/122676067-e12fcc00-d1f9-11eb-8ec7-4e704a47f83d.png)
- ![image](https://user-images.githubusercontent.com/50113394/122676093-04f31200-d1fa-11eb-853e-202102a1b8e7.png)

# Damage Localization
- ![image](https://user-images.githubusercontent.com/50113394/122676130-27852b00-d1fa-11eb-8e92-2dfdcabd6457.png)

# Training loss vs Validation loss
- ![image](https://user-images.githubusercontent.com/50113394/122676186-82b71d80-d1fa-11eb-88cc-708786320ba3.png)

# Steps Model Training
 1) Go in model-training directory, in the master file you will be able to find the code for all three stages. 
 2) requirements.txt
 3) You can train the model on just stage-1, stage-2 and stage-3. Dataset for each stage is provided.
 4) download the maskrcnn coco weights from https://github.com/matterport/Mask_RCNN, and train the model on these weights. 
 5) Put the weights after getting desired reults in model directory. 
 6) Change line # in to name of the weights.
 7) Run app.py file

# Reference
- For more detains on Mask RCNN check out the following link:
- matterport/Mask_RCNN. (2021). Retrieved 1 January 2021, from https://github.com/matterport/Mask_RCNN

Connect with me on linkedin if you have some doubts regarding the training and deployment of the project.
- https://www.linkedin.com/in/eashan-kaushik-7b4454168/

I will soon be writing an article on medium regarding training of MaskRCNN model. 
