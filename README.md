# Traffic Sign Segmentation
 UCCD2513 Mini Project

# Contents
1. 100 traffic sign test images in "test" folder
2. Traffic Sign Segmentation.ipynb: All codings from read image, preprocessing, color segmentation to the performance metrics evaluation. 
3. TsignRecgTrain4170Annotation.txt: Contains the dimensions and the bounding box x1,y1,x2,y2, as well as the class of each image. 
   - Format of annotation answers: filename; width; height; x1; y1; x2; y2; type;
4. segment.py: A simplified Python script to segment the traffic sign.
   - Input: an image file
   - Output: A window displaying the segmented image (original image with bounding box)
   - Refer below for syntax.
6. accuracy.csv: Output from ipynb notebook that contains the pixel accuracy of each segmented image. 

## The syntax of segment.py in Command Prompt/PowerShell
python3 segment.py --input "123_4567.png"

# ipynb Notebook functions
1. read(x)
    - Input: A folder path "x". e.g. 'C:/Users/fict/uccd2513-image processing/traffic sign images/'
    - Function: Reads all images and its filenames in the input folder
    - Output 1: An array containing all images read
    - Output 2: An array containing the filenames of the images read
2. display(arr)
    - Input: An array containing images
    - Function: Display all images in the input array
3. display20(arr)
    - Input: An array containing images
    - Function: Display first 20 images in the input array
4. color_segment(img)
    - Input: A BGR image read using cv.imread() function
    - Function: Applies color segmentation & draws bounding box to the image. Also appends the bounding box information into an array.
    - Output: The same image with bounding box
5. area(img)
    - Input: A BGR image read using cv.imread() function
    - Function: Returns the area of the input image. (int)
6. perf(results)
    - Input: An array containing bounding box information (segmentation results)
    - Function: Calculate the accuracy, precision, recall and F1 score of each image and print the Average accuracy, precision, recall and F1 score.
    - Output: An array containing the filename and accuracy of each segmented image
