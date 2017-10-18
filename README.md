# **Image-Search-Engine**

The following project has been inspired by Adrian Rosebrock's series on Computer Vision.

Alright, the aim of the project is to create an **Image Search Engine**, such that given an image query the program is able to output a Top10 list of similar images. We proceed by breaking the task into four steps:

- Descriptor
- Indexing
- Features metrics
- Search

## **Descriptor**

The first step in our chained process is to find a description for the images in our dataset, first things first. The description, or better saying the features, that describe an image can be of many types, HSV, RGB, etc. We opt for a 3 channel colour space description using a 3D RGB histogram (a histogram is a metrics used in image analysis that represents the colour space of an image, exactly what we need :)). Opting for an 8 bins separation for each colour channel obtaining a 3x8 matrix, which we proceed to normalise to avoid a scale variance of the same image (basically getting different results for the same image due to a different scale). The result of the matrix computation for each image is flattened to obtain a vector of those features.

## **Indexing**

In the indexing step we quantify our data by giving them and index and process their feature vector and storing this value in a look-up table where the index is the **unique** filename of the image and the value is the *features** vector, which we talked about in the previous section. This all we do.

## **Feature Metrics**

Now, we have our nice dataset and its vector features. What is next ? The search part. Given an image query, what is out metric of comparison ? Well, it clearly has to do with the feature vector. How do we compare the closeness of the two images then ? We do use what is called a **distance function** which tells us how distant are the points in a set, exactly what we need to understand if two images are somehow similar.

Hence, the process consists in looping over the features of our dataset and computing the distance metrics of the image query against all dataset, and possibly storing these values in a lookup table where the key is the filename and the value the distance. The table, can than be sorted from lowest distance to the greatest one, giving us the ranking.

## **Search**

The search part is all about making good use of the results obtained and displaying the images.
