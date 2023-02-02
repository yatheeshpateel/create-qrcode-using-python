import qrcode as qr
img = qr.make("https://www.linkedin.com/in/yatheesh-pateel-k-g-510b5921a/")
img.save("linkedin.jpg")

qrcode.make