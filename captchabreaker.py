from io import BytesIO
from requests import get
from PIL import Image
from pytesseract import image_to_string

bimg = get('https://i.imgur.com/29FLrpe.png')

image = Image.open(BytesIO(bimg.content))

t = image_to_string(image)

if t[1]=='+':
    print (t[0], t[1], t[2], ' = ', int(t[0])+int(t[2]))
elif t[1]=='-':
    print (t[0], t[1], t[2], ' = ', int(t[0])-int(t[2]))
elif t[1]=='*':
    print (t[0], t[1], t[2], ' = ', int(t[0])*int(t[2]))
elif t[1]=='/':
    print (t[0], t[1], t[2], ' = ', int(int(t[0])/int(t[2])))
