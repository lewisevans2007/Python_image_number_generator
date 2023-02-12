import PIL
import random
from PIL import Image
from PIL import ImageDraw
import matplotlib.pyplot as plt
import os
for i in os.listdir("images"):
    img = PIL.Image.open("images/"+i)
    b = img.height/256
    x = random.randint(0,1)
    y = random.randint(0,1)
    x_points = []
    y_points = []
    for z in range(random.randint(1,100)):
        x = x+random.randint(0,10)
        if x > img.height:
            x = x/ 2
            if x > img.height:
                x = x/ 5
                if x > img.height:
                    x = x/ 100    
        y = y+random.randint(0,10)
        if y > img.width:
            y = y/ 2
            if y > img.width:
                y = y/ 5
                if y > img.width:
                    y = y/ 100    
        x = round(x)
        y = round(y)
        x_points.append(x)
        y_points.append(y)
        try:
            rgb_pixel_value = img.getpixel((x,y))[1]
        except:
            x = x/2
            y = y/2
            rgb_pixel_value = img.getpixel((x,y))[1]
        x = x*rgb_pixel_value
        y = y*rgb_pixel_value

    img = plt.imread("images/"+i)
    fig, ax = plt.subplots()
    plt.scatter(x_points, y_points, label = "label_name" )
    ax.imshow(img)
    plt.savefig("plots-"+i)
    print(rgb_pixel_value)
