import base64
from PIL import Image
from io import BytesIO

output_filename = 'ats_image'

base64_string = "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAASABIAAD..."
base64_string = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASwA..."
str = base64_string.split('base64')[1]

ext = 'jpeg' if 'jpeg' in base64_string else 'png'
ext2 = ext.replace('e', '')

image_data = base64.b64decode(str)
image = Image.open(BytesIO(image_data))
out_file = output_filename+'.'+ext2
image.save(out_file, ext)

print(f"Success: {out_file}")
