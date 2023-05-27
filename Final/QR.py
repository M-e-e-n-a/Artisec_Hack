import qrcode
import cv2

class qr():
    def __init__(self):
        self.code = None

    def generate(self, url):
        data = url
        img_path = "./static/qrcode.png"
        img = qrcode.make(data)
        img.save(img_path) 
        with open("./static/qrcode.png", "rb") as image:
            f = image.read()
            b = bytearray(f)
            self.code = b

class basic_data():
    def __init__(self):
        self.usn = None
        self.dob = None
    def add(self, usn, dob):
        self.usn = usn
        self.dpb = dob
    def get(self):
        return self.usn