# steg_tool.py
from PIL import Image
import stepic

# Hide data
img = Image.open("original.jpg")
secret = stepic.encode(img, b"super secret message")
secret.save("encoded.png")

# Reveal data
decoded_img = Image.open("encoded.png")
hidden = stepic.decode(decoded_img)
print("Hidden message:", hidden.decode())
