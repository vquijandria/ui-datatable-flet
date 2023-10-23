import flet as ft
from flet import *

#this class will generate a new instance of textfield and insert it into the data table

class FormHelper(UserControl):
    def __init__(self, user_input):
        self.user_input = user_input
        super().__init__()


    def save_value(self, e):
        self.controls[0].read_only = True
        self.controls[0].update()

    def build(self):
        return TextField(
            value=self.user_input,
            border_color="transparent",
            height=20,
            text_size=13,
            content_padding=0,
            cursor_color="black",
            cursor_width=1,
            color="black",
            read_only=True, #so user cant change it
            on_blur=lambda e: self.save_value(e),
        )

