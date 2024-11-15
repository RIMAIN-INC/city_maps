#Author: Richmond Nartey Kwalah Tettey
#Course: CS1
#Date: 11/07/2024
#Purpose: To sort cities and to display on map

from cs1lib import draw_circle, set_fill_color, draw_text, set_font, set_font_size, set_stroke_color, set_font_bold

class Container:
    def __init__(self, cx,cy,size,info, hue, hue2):
        self.cx = cx
        self.cy = cy
        self.size = size
        self.info = info
        (r,g,b) = hue
        (r2,g2,b2) = hue2
        self.r = r
        self.g = g
        self.b = b
        self.r2 = r2
        self.g2 = g2
        self.b2 = b2

    def draw(self):
        #shape of outline of circle container
        set_fill_color(self.r,self.g,self.b)
        draw_circle(self.cx,self.cy,self.size)

        #shape of inner-line of inner circle container
        set_fill_color(self.r2,self.g2,self.b2)
        draw_circle(self.cx,self.cy,int(self.size/1.18))

        #display name of city
        set_font("Verdana")
        set_font_size(10)
        set_font_bold()
        draw_text(self.info,self.cx-len(self.info)*3,self.cy+5)

    def update_info(self):
        pass