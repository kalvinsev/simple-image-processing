# Kalvin Sevillano
# Program inverts the color sheme of image described and must be contianed within same working directory.
# This program also doubles the size of your inverted image once processed. 
# Make sure to click through the image to continue the programs processes.
# Enjoy!


import image

def changeColor(img):
    original_image = image.FileImage(img)

    width = original_image.get_width()
    height = original_image.get_height()

    win = image.ImageWin(width, height, "Inverted Image")
    
    
    original_image.draw(win)
    my_image = original_image.copy()

    

    for row in range(height):
        for col in range(width):
            v = my_image.get_pixel(col,row)
            v.red = 255 - v.red
            v.green = 255 - v.green
            v.blue = 255 - v.blue
            my_image.set_pixel(col,row,v)


    my_image.draw(win)
    my_image.save("new-image.jpeg")
    win.exit_on_click()

def resize(img):
    original_image = image.FileImage(img)
    oldWidth = original_image.get_width()
    oldHeight = original_image.get_height()
    
    newImage = image.EmptyImage(oldWidth*2, oldHeight*2)

    win = image.ImageWin(oldWidth*2, oldHeight*2, "Resized Inverted Image")
    for row in range(oldHeight):
        for col in range(oldWidth):
            oldPixel = original_image.get_pixel(col, row)

            newImage.set_pixel(2*col, 2*row, oldPixel)
            newImage.setPixel(2 * col + 1, 2 * row, oldPixel)
            newImage.setPixel(2 * col, 2 * row + 1, oldPixel)
            newImage.setPixel(2 * col + 1, 2 * row + 1, oldPixel)

    newImage.draw(win)
    win.exit_on_click()

    
def main():
    myImage = "butterfly.jpeg"
    changeColor(myImage)
    newImage = "new-image.jpeg"
    resize(newImage)
    
    
if __name__ == '__main__':
    # This code won't run if this file is imported.
    main()