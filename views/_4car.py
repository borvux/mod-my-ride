import flet as ft
from flet import *
from flet_route import Params, Basket
from functions.mysql import execute_query
import os
from functions.mods import *

def car(page: ft.Page, params: Params, basket: Basket):
    data = basket.get('car_data')
    make = data['make'] 
    model = data['model']
    year = data['year'] 
    
    car_info_parse = execute_query(f"select model_info from models where model_name = %s", (model,))
    print(car_info_parse)
    car_info = car_info_parse[0][0]
    
    # # for debugging
    # make = ''
    # model = 'mustang'
    # year = '2024'
    # car_info = ''
    
    path = f'/Users/bennyjoram/Desktop/MMR - github/Capstone/mod_my_ride/assets/cars/{model.lower()}_{year}'
    
    # get the image files
    image_files = [file for file in os.listdir(path) if file.endswith('.webp')]
    
    # sort the images in order
    image_files.sort()
    
    images = ft.Row(expand=1, wrap=False, scroll='always')
    for image in image_files:
        images.controls.append(
            ft.Image(
                src=os.path.join(path, image),
                width=350,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
            )
        )
        
    def button_click(e, icon, mods, mods_controls):
        # Change the icon when the button is clicked
        if icon.name == ft.icons.KEYBOARD_ARROW_RIGHT:
            icon.name = ft.icons.KEYBOARD_ARROW_DOWN
            mods_controls.controls.append(add_mods(mods))
        else:
            icon.name = ft.icons.KEYBOARD_ARROW_RIGHT
            mods_controls.controls = None
        page.update()
        
    def wheels_button(e, icon):
        button_click(e, icon, wheels, wheels_mods)
        
    def decals_button(e, icon):
        button_click(e, icon, decals, decals_mods)
        
    def wraps_button(e, icon):
        button_click(e, icon, wraps, wraps_mods)
        
    def lights_button(e, icon):
        button_click(e, icon, led, lighting_mods)
    
    def more_mods_button(e, icon):
        button_click(e, icon, more, more_mods)
          
    def custom_button(image_path, text, on_click_func, icon):
        arrow_icon = ft.Icon(
            name=icon,
        )
        return ft.ElevatedButton(
            content=ft.Row(
                [
                    ft.Image(
                    src=f'{image_path}',
                    width=50,
                    height=60,
                    fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        f"{text}",
                    ),
                    arrow_icon,
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            on_click=lambda e: on_click_func(e, arrow_icon),
        )
        
    wheels_mods = ft.Row([], scroll='always')
    decals_mods = ft.Row([], scroll='always')
    wraps_mods = ft.Row([], scroll='always')
    lighting_mods = ft.Row([], scroll='always')
    more_mods = ft.Row([], scroll='always')
        
    def add_mods(mod):
        mod_menu = Row()
        
        for item in mod:
            mod_menu.controls.append(
                Card(
                    elevation=20,
                    content=Container(
                        width=150,
                        border_radius=8,
                        bgcolor=ft.colors.WHITE,
                        content=Column(
                            [
                                ft.Image(
                                    src=item['image'],
                                    border_radius=8,
                                    width=150,
                                    height=100,
                                    fit=ImageFit.CONTAIN,
                                ),
                                Container(
                                    padding=8,
                                    content=Column(
                                        [
                                            ft.Text(
                                                item['name'],
                                                text_align=ft.TextAlign.CENTER,
                                                height=50,
                                            )
                                        ],
                                    ),
                                    alignment=ft.alignment.center,
                                ),
                            ],
                        )
                    )
                )
            )
        
        return mod_menu
    
    return ft.View(
        '/car',
        scroll=True,
        bgcolor=ft.colors.GREY_300,
        controls=[
            ft.AppBar(
                center_title=True,
                bgcolor=ft.colors.PRIMARY,
                
                leading = ft.IconButton( # back button
                    ft.icons.ARROW_BACK,
                    on_click= lambda _: page.go('/home'),
                    icon_color= ft.colors.WHITE,
                    tooltip='back',
                ),
                
                title=ft.Text(
                    'View Car',
                    color=ft.colors.WHITE,
                    size=25,
                    weight=ft.FontWeight.BOLD,
                ),
            ),
            
            ft.Card(
                ft.Container(
                    bgcolor=ft.colors.WHITE,
                    content=ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Text(
                                        year,
                                        size=20,
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                    ft.Text(
                                        make,
                                        size=20,
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                    ft.Text(
                                        model,
                                        size=20,
                                        weight=ft.FontWeight.BOLD,
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                        ],
                    ),
                    border_radius=20,
                    padding=10,
                    width=300,
                ),
            ),
            
            ft.Card(
                ft.Container(
                    bgcolor=ft.colors.WHITE,
                    content=ft.Column(
                        [
                            images,
                        ],
                    ),
                    border_radius=20,
                    padding=10,
                    height=300,
                    width=1000,
                ),
            ),
            
            ft.Card(
                ft.Container(
                    bgcolor=ft.colors.WHITE,
                    content=ft.Column(
                        [
                            ft.Text(
                                car_info,
                                text_align=ft.TextAlign.CENTER,
                            )
                        ],
                    ),
                    border_radius=20,
                    padding=10,
                    width=1000,
                ),
            ),
            
            ft.Card(
                ft.Container(
                    bgcolor=ft.colors.WHITE,
                    content=ft.Column(
                        [
                            ft.Text(
                                'Modifications',
                                size=20,
                                weight=ft.FontWeight.BOLD,
                            )
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    border_radius=20,
                    padding=10,
                    width=300,
                ),
            ),
            
            ft.Card(
                ft.Container(
                    bgcolor=ft.colors.WHITE,
                    content=ft.Column(
                        [
                            custom_button(
                                '/Users/bennyjoram/Desktop/MMR - github/Capstone/mod_my_ride/assets/wheel.png',
                                'Wheels',
                                wheels_button,
                                ft.icons.KEYBOARD_ARROW_RIGHT,
                            ),
                            
                            ft.Container(
                                content=Column(
                                    [
                                        wheels_mods,
                                    ]
                                )
                            ),
                            
                            custom_button(
                                '/Users/bennyjoram/Desktop/MMR - github/Capstone/mod_my_ride/assets/decal.png',
                                'Decals',
                                decals_button,
                                ft.icons.KEYBOARD_ARROW_RIGHT,
                            ),
                            
                            ft.Container(
                                content=Column(
                                    [
                                        decals_mods
                                    ]
                                )
                            ),
                            
                            
                            custom_button(
                                '/Users/bennyjoram/Desktop/MMR - github/Capstone/mod_my_ride/assets/wrap.jpg',
                                'Wraps',
                                wraps_button,
                                ft.icons.KEYBOARD_ARROW_RIGHT,
                            ),
                            
                            ft.Container(
                                content=Column(
                                    [
                                        wraps_mods,
                                    ]
                                )
                            ),
                            
                            
                            custom_button(
                                '/Users/bennyjoram/Desktop/MMR - github/Capstone/mod_my_ride/assets/rgb.webp',
                                'Lighting',
                                lights_button,
                                ft.icons.KEYBOARD_ARROW_RIGHT,
                            ),
                            
                            ft.Container(
                                content=Column(
                                    [
                                        lighting_mods,
                                    ]
                                )
                            ),
                            
                            
                            custom_button(
                                '/Users/bennyjoram/Desktop/MMR - github/Capstone/mod_my_ride/assets/more.png',
                                'More Mods',
                                more_mods_button,
                                ft.icons.KEYBOARD_ARROW_RIGHT,
                            ),
                            
                            ft.Container(
                                content=Column(
                                    [
                                        more_mods,
                                    ]
                                )
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    border_radius=20,
                    padding=10,
                    width=500,
                ),
            ),
        ],
        horizontal_alignment='center',
        spacing=2,
    )
