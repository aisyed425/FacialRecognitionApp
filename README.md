# Facial Recognition App 
The core of the application involves training a Siamese neural network

## Install Dependencies
1. Install Dependencies around Tensorflow
3. Importing Tensorflow Functional API
4. Setting up to Limit your GPU growth 
5. Create Data Folders and Structures

## Import Dependencies
1. Import both standard libraries
2. TensorFlow's deep learning components 

## Configure GPU Growth
If using a GPU, set memory growth to True using tf.config.experimental.set_memory_growth to prevent out-of-memory errors

## Create Folder Structure
Set up a main folder with three subfolders: anchor, positive, and negative, to organize images for the facial verification mode
