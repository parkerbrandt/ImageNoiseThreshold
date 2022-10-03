# ImageNoiseThreshold

A script that determines if 3D images are noisy or not based on the number of non-zero pixels in the image.
Reads in the images from their locations given in a text file, then outputs if each image is clean/not noisy (True) or noisy (False) in an output text file.


# How to Run

To run the script, the expected format of the command is 

```
python noise.py [input text file] [threshold*] [output text file]
```

The input text file holds the paths to all the images to check for noise.

The threshold is the cutoff between a clean/not noisy image and a noisy one. We've have used 1.2 x 10^8, but 1.4 or 1.6 would work as well.

The output text file will hold the output for each image in the input text file.


* NOTE: The threshold input is implicitly multiplied by 10^8 (or 100 million)


# Input Format

In the input text file, the script expects the format to have one image file path per line. For example, 

```
folder1/image_file_1.tiff
folder2/image_file_2.tiff
```


# Output Format

The output file will be written as 

```
[image file name],True or False
```

True indicates a clean image and False indicates a noisy image


# TODO
 - Add in the ability to choose between using the non-zero count method or the sum of pixel intensity method to determine the cutoffs
 - If wanted, add print statements or a debug mode to show what the script is doing
 - See if there are ways to make the script run faster