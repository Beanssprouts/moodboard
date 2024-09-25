# moodboard
hello! 
This is how the code works: 
the first 129 lines of the code establishes what objects are in the room, their sizes and position. I should have it labeled 
via comments of which code deals with what object

lines 135 - 154 deals with the buttons, the visual button you see on the web page and you press. They should also be labeled. 
They are linked to lines 992 - 1039 which actually tell the buttons what to do (i will get into those later) 

lines 162 - 735 contains the image links to all the images that are used in the webpage. They are public image urls that can be accessed 
from any computer. These images have been downloaded, processed to remove the background, then had the links created. Next to the image links are numbers, these numbers represent the prices of each of the items. This will become important in the code later as the numbers eventually all add up to display the final price of all the items present in the room. 

lines 738 - 962 contains the actual links to the images present. This is where the code links to when the user double clicks on the object. 
It will take the user to the link associated with the image in a different window 

lines 938 - 948 deals with the adjusting of the room size. When the user inputs a certain number into the length and width boxes, the code 
will take the number and multiply it by 4, then adject the room length accordingly to the amount of pixels resulting. 

lines 980 - 1056 splits the images up into categories to assign to different parts of the room. (sofas, tables, chairs, etc.) 

lines 1088 - 1213 takes the categories made in lines 980 - 1056 and tells the computer how to present them. So category 1 in this case is sofas, all the images split into category one will have the same specified size and location in the room based on what was inputted for size and location of category 1 in this section of the code. This applies to the rest of the categories and items 

The function "createFlippedImage(src)" is for the chairs. In order to create the effect of two chairs on either sides of the sofa, I had taken one chair, and had the code take this image, duplicate it, flip it, then position it on the other side of the sofa. 

lines 1190 - 1197 is the code for the pricing that is being displayed. Each image link, as stated above has the price of the object next to it. These lines of code takes all the numbers and adds them together, then displays the number

lines 1200 - 1203 is randomization, this is what creates the random generation of each item in each category into the room. 

The rest of the code is somewhat self explanitory from the comments and name of functions. They are all code that displays the images into the room 
