from PIL import Image, ImageDraw, ImageFont
import sys
import os
import locale

font = '~/Library/Fonts/Fura Code Medium Nerd Font Complete Mono.ttf'

names = [
    u"ПОЛОВИНКИН", 
    u"ИВАНОВА", 
    u"ЛУНИНА",
    u"КОНСТАНТИНОВ",
    u"АРУТЮНОВ",
    u"РЕЗНИЧЕНКО",
    u"БЕСОВ",
    u"КАРАСЕВ",
    u"ЖДАНОВСКИЙ",
    u"БУРЦЕВ",
    u"БУРСКИЙ",
    u"ПОДЛИПСКИЙ",
    u"КАРЛОВ",
    u"УМНОВ СТ",
    u"УМНОВ МЛ",
    u"КОЛЕСНИКОВА",
    u"АГАХАНОВА",
    u"ГОЛУБЕВ",
    u"ГОЛОВАНОВ",
    u"КАЛИНИЧЕНКО",
    u"ГОРОДЕЦКИЙ",
    u"ШАНЬКОВ",
    u"ШАНЬКОВ",
    u"ШАНЬКОВ",
    u"ШАНЬКОВ"
    ]

def create_img(name):
    (w,h) = (220, 220)
    img = Image.new('RGB', (w, h), color = 'white')
    
    fnt = ImageFont.truetype(font, 28)
    (x,y) = (w/2 - len(name)/2*16.8, h/2-19)
    
    d = ImageDraw.Draw(img)
    d.text((x,y), name, "black", font=fnt)

    img.save('images/{}.png'.format(name))

def create_folder():
    path = os.path.join(os.getcwd(), 'images')
    os.mkdir(path)

if __name__ == "__main__":
    create_folder()
    for name in names:
        create_img(name)