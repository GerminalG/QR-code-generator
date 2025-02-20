import qrcode
import qrcode.image.svg
# URL or text you want to encode
website_url = "https://docs.google.com/forms/d/e/1FAIpQLSdpfNR7Y4tdPBGEEVNPyNGybCytXH9BYIXSp0Cqw5uhjvpeBw/viewform?usp=sharing"

# Create QR Code
qr = qrcode.QRCode(
    version=1,  # Size of the QR code (1 is the smallest, 40 is the largest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Low error correction
    box_size=10,  # Size of each square in the QR code
    border=4,  # Border thickness
)

qr.add_data(website_url)
qr.make(fit=True)

# Generate the QR code image
img = qr.make_image(fill="black", back_color="white")

# Save the QR code as a PNG file
img.save("qr_code.png")

#img = qr.make_image(image_factory=qrcode.image.svg.SvgImage)
#img.save("qr_code.svg")
#print("✅ QR Code (SVG) generated successfully! Check qr_code.svg")
print("✅ QR Code generated successfully! Check qr_code.png")


