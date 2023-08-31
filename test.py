import settings as st

from tkinter import *
from PIL import Image, ImageTk
from customtkinter import *

set_appearance_mode('system')
set_defauLt_color_theme('dark-blue')

root = CTk()
root.geometry(f'{st.WIDTH}x{st.HEIGHT}')
root.bind('<Escape>', lambda e: root.quit())

landpage_img = Image.open(f"{st.PATHS[ 'media' ]}/Landpage_bg.png")
Landpage_img = ImageTk.PhotoImage(Landpage_img)

landpage = CTkLabel(root, image=Landpage_img, text = '')
Landpage.pack()

root.mainloop()