from PIL import Image
import PIL

image1 = Image.open("car1.jpg")
image2 = Image.open("car2.jpg")
image3 = Image.open("car3.jpg")

blender_image = Image.blend(image1,image2,0.3)

blender_image.save("blender_image.jpg")

imgbl = Image.blend(image3,blender_image,0.3)

img = Image.blend(imgbl,imgbl,00)

img.save("image.jpg")
