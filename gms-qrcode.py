# import modules
import qrcode
from PIL import Image

Logo_link = 'book-read-white-bg.png'
text = 'https://greenmountschool.org'

# +
logo = Image.open(Logo_link)

# taking base width
basewidth = 100

# adjust image size
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.LANCZOS)
QRcode = qrcode.QRCode(
	error_correction=qrcode.constants.ERROR_CORRECT_H
)

# adding URL or text to QRcode
QRcode.add_data(text)

# generating QR code
QRcode.make()

# taking color name from user
QRcolors = ['Green', 'Black', 'Purple']

for QRcolor in QRcolors:
    # adding color to QR code
    QRimg = QRcode.make_image(
	fill_color=QRcolor, back_color="white").convert('RGB')

    # set size of QR code
    pos = ((QRimg.size[0] - logo.size[0]) // 2,
	   (QRimg.size[1] - logo.size[1]) // 2)

    # save QR code w/o logo
    QRimg.save('QRcode-no-logo-'+QRcolor+'.png')

    # add logo to QR code
    QRimg.paste(logo, pos)

    # save the QR code w/ logo
    QRimg.save('QRcode-logo-'+QRcolor+'.png')
    QRimg.close()

    print('QR codes generated!')
# -


