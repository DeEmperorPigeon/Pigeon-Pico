from random import *
import time
import picodisplay as dis
width = dis.get_width()
height = dis.get_height()
dis_buffer = bytearray(width * height * 2)  # 2-bytes per pixel (RGB565)
dis.init(dis_buffer)
dis.set_backlight(1)

current_menu = "main_menu"
start_time = time.time()
scenes = {}
tick = 0
tick_count = 0
fps = 0

class Scene:
    def __init__(self, scenename, pen, size):
        self.scene_name = scenename
        self.pointer_pen = pen
        self.pointer_size = size
        self.items = []
        self.current_button = 0
        scenes[self.scene_name] = self
    
    def draw_scene(self):
        for item in self.items:
            if item["item_type"] = "text":
                pass
            
    def change_menu(self, menuname):
        global current_menu
        current_menu = menuname
    
    def start_game(self):
        pass
    
    def add_item(self, name, item_type, x, y, pen, size, text = "none"):
        if item_type == "text":
            self.items.append(name = {
              "text":text,
              "x":x,
              "y":y,
              "pen":pen,
              "type":item_type
            })

def screen_update(pen):
    dis.update()
    dis.set_pen(pen)
    dis.clear()
    scenes[current_menu].draw_scene() 

def show_fps(pen, limiter):
    dis.set_pen(pen)
    global start_time
    global tick
    global fps
    try:
        if not(float(time.time() - start_time) == 0):
            start_time = time.time()
            fps = tick - fps
        else:
            tick += 1
    except:
        start_time = time.time()
        tick = 0
        
    dis.text(str(fps), width-22,0, False, 2)
    if limiter == True:
        time.sleep(0.018)

def rect(x=0,y=0,w=3,h=3,p=dis.create_pen(255,255,255)):
    dis.set_pen(p)
    for a in range(0, h):
        for b in range(0, w):
            dis.pixel(x+b, y+a)

def sqre(x,y,p,s):
    dis.set_pen(p)
    for i in range(0,s):
        for j in range(0,s):
            dis.pixel(x+i,y+j)

def left_pointer(x,y,p,s):
    dis.set_pen(p)
    sqre(x+s,y,p,s)
    sqre(x,y+s,p,s)
    sqre(x+s,y+s+s,p,s)
    
def ticks_passed(num):
    global tick_count
    global tick
    if tick - tick_count >= num:
        new_count = tick
        return True
    else:
        return False
