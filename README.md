# Object_Detection_in_an_Urban_Environment

## Project overview
This section should contain a brief description of the project and what we are trying to achieve. Why is object detection such an important component of self driving car systems?

The goal of the project is to detect objects like pedestrians, vehicles and cyclists in the Waymo Open dataset. The base of the assignment is a neural network called Segnet. The first step is to explore the several images of the dataset and split them for training, validation and testing. Additionlly it is necessary to adopt different strategies to improve the model and get better results.
Object detection is a really important component of a self driving car system. You have to understand your environment, otherwise the system is not able to locate and navigate through it. Especially for safety reasons you need to know which of the objects are human beings or which are static or dynamic objects to make predictions.

## Set up
This section should contain a brief description of the steps to follow to run the code for this repository.

I used the Udacity workspace to run the code for this repository. To reproduce the results copy the files into the workspace and follow the introduction which is given in the README.md of the project.

## Dataset
### Dataset analysis
This section should contain a quantitative and qualitative description of the dataset. It should include images, charts and other visualizations.

With the Exploratory Data Analysis.ipynb jupyter notebook it is possible to look at several images from the Waymo Open dataset. Vehicles are drawn with red, pedestrians with blue and cyclists with green rectangles. As you can see in the following images the dataset contains images with perfect weather conditions like a clear blue sky, blurred images because of rainy or foggy weather, wet streets, really dark or light images, occlusion due raindrops or other objects and a high amount of objects like cars or pedestrians crossing the street.

![image](../master/images/Dataset_1.png)

The following chart shows the class distribution of 2000 images. You can see that the most objects of the dataset are vehicles. The number of pedestrians is one third of the vehicles while the dataset contains only a few cyclists.

![image](../master/images/Numberobjects.png)

### Cross validation
This section should detail the cross validation strategy and justify your approach.

For the cross validation the dataset is split into training, validation and testing. To train the neural network with only a subset of the dataset and test it with unknown images you can evaluate the model very efficiently and pretend overfitting. For that 87 sequences (80-90% of the available date) were used for training, 10 (10-20% of the available date) for validation and 3 for testing purpose.

## Training
### Reference experiment
This section should detail the results of the reference experiment. It should includes training metrics and a detailed explanation of the algorithm's performances.

The loss course of the given model is shown in the following image of Tensorboard. With that results it is not possible to detect and display any objects during the test stage. In that case it is crucial to improve the performance.
![image](../master/images/Reference.png)

### Improve on the reference
This section should highlight the different strategies you adopted to improve your model. It should contain relevant figures and details of your findings.

#### Experiment 1
To improve the model I added in the first experiment gray, brightness and contrast as augmentation options.
![image](../master/images/Augmentation.png) ![image](../master/images/Augmentation2.png)

Differently than thought the loss of the model was worse then the reference.
![image](../master/images/Loss.png)


#### Experiment 2
In that case I added saturation as another augmentation option. With that change the loss decline, but in the test stage no objects could be detected.
![image](../master/images/Loss2.png)


#### Experiment 3
In the last eperiment I changed the optimizer from momentum to adam and added a stepwise annealing strategy. With those changes the loss of the model would be approaching to zero with further epochs.
![image](../master/images/Loss3.png)

The results of the model are visualized in the following image. Now it is possible to detect and display the objects of an image in the test stage.
![image](../master/images/Animation2.png)

