import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

# Generate QR code 
myqr = qrcode.make("https://www.linkedin.com/in/tshegofatsoamandankutshweu/")
myqrcode = qrcode.make("https://za.linkedin.com/")

# Create and save the png file naming "myqr.png" 
myqr.save("myqr.png", scale = 8)

#decode qr code
var = decode(Image.open("myqr.png"))
print(var[0].data.decode("ascii"))

