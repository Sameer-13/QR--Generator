import qrcode

# The link you want to encode
url = "smth
# Generate QR code
qr = qrcode.QRCode(
    version=1,  # controls size (1 = 21x21, higher = larger QR)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # error correction level
    box_size=10,  # size of each box
    border=4,  # border thickness
)
qr.add_data(url)
qr.make(fit=True)

# Create an image
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code as PNG
img.save("colab_qr.png")

print("✅ QR code generated and saved as colab_qr.png")
