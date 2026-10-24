import qrcode

url = input("Enter the URL: ").strip()
file_path ="C:\\Users\\satej\\OneDrive\\Desktop\\QR Code\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR Code was generated Successfully!!")