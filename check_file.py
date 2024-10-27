from PIL import Image, ImageDraw, ImageFont

# Create a new image (for demonstration)
image_path = "whatsapp.png"  # Replace with your image file path
with Image.open(image_path) as img:
    width, height = img.size  # Get the dimensions
   
image_size = (width, height)
#image = Image.new("RGB", image_size, "white")
image = Image.open("whatsapp.png")

draw = ImageDraw.Draw(image)
height_2 = image_size[1]
# Sample text
text = "Whatsapp"
font = ImageFont.truetype("arial.ttf",30)
#     font = ImageFont.truetype("arial.ttf",50)

# Get bounding box of the text
bbox = draw.textbbox((0, 0), text, font)  # Get the bounding box
text_width = bbox[2] - bbox[0]  # Width is the difference in x-coordinates
text_height = bbox[3] - bbox[1]  # Height is the difference in y-coordinates

# Calculate position to center the text horizontally and place it at the bottom
x_position = (image_size[0] - text_width) / 2  # Center horizontally
y_position = height_2 -10 - text_height  # Position it just above the bottom row

# Draw the text
draw.text((x_position, y_position), text, fill="black", font=font)

# Save or show the image
image.save("output_Whatsapp.png")
image.show()  # Optional: to display the image immediately
