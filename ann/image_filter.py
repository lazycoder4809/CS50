from PIL import Image, ImageFilter
import sys
import os

print(os.getcwd())
print(os.path.exists("cat.jpg")) 

img = Image.open("Miku summer.jpg")
print("Image opened successfully.") 
edge_kernel = ImageFilter.Kernel(
    size=(3,3),
    kernel=[
        -1,-1,-1,
        -1, 8,-1,
        -1,-1,-1
    ],
    scale=1
)

result = img.filter(edge_kernel)
result.show()
print("Image sharpened successfully.")