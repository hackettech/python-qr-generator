import pyqrcode
import png
from pyqrcode import QRCode
link=input("Type website link:")
url=pyqrcode.create(link)
url.svg("myqr.svg",scale=8)
url.png("myqr.png",scale=6)

