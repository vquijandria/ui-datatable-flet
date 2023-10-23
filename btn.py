import flet as ft
from flet import *
from controls import return_control_reference
from form_helper import FormHelper


#Get global map dict
control_map = return_control_reference()

def update_text(e):
    e.control.content.controls[0].read_only = False
    e.control.content.controls[0].update()

#This method will handle the main data from the user
def get_input_data(e):
    for key, value in control_map.items():
        #the key AppForm is where the values are
        if key == "AppForm":
            #once we´re in the key, we create a DataRow
            data = DataRow(cells=[])

            #we can now loop over the textfields and get values
            for user_input in value.controls[0].content.controls[0].controls[:]:
                #we append the values into the cells list
                data.cells.append(
                    DataCell(
                        FormHelper(user_input.content.controls[1].value),
                        on_double_tap=lambda e: update_text(e),
                    )
                )
                
            for user_input in value.controls[0].content.controls[1].controls[:]:
                #we append the values into the cells list
                data.cells.append(
                    DataCell(
                        FormHelper(user_input.content.controls[1].value),
                        on_double_tap=lambda e: update_text(e),
                    )
                )

            
        if key == "AppDataTable":
            value.controls[0].controls[0].rows.append(data)
            value.controls[0].controls[0].update()


            

def return_form_button():
    return Container(
        alignment=alignment.center,
        content=ElevatedButton(
            on_click=lambda e:get_input_data(e),
            bgcolor="#081D33",
            color="white",
            content=Row(
                controls=[
                    Icon(
                        name=icons.ADD_ROUNDED,
                        size=12,
                    ),
                    Text(
                        "Add Input field to table",
                        size=11,
                        weight="bold",
                    ),
                ],
            ),
            style=ButtonStyle(
                shape={
                    "": RoundedRectangleBorder(radius=6),
                },
                color={
                    "": "white",
                },
            ),
            height=42,
            width=220,
        ),
    )