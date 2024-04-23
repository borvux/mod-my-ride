import flet as ft
from flet import *
from flet_route import Params, Basket
from functions.adaptive_alert import *
from functions.mysql import execute_query

def home(page: ft.Page, params: Params, basket: Basket):    
    # get the car makes from the MySQL db
    makes = execute_query("select * from makes", "")
    make_options = [ft.dropdown.Option(option[0]) for option in makes]
    
    def make_selected(e):
        check_dropdown()
        models = execute_query(f"select model_name from models where make_name = %s", (make.value,))
        model.options = [ft.dropdown.Option(option[0]) for option in models]
        page.update()
 
    def model_selected(e):
        check_dropdown()
        years = execute_query(f"select year from years where make_name = %s and model_name = %s order by year desc", (make.value, model.value,))
        year.options = [ft.dropdown.Option(option[0]) for option in years]
        page.update()
        check_dropdown()
    
    def year_selected(e):
        check_dropdown()
        page.update()
        basket.car_data = {"make": str(make.value), "model": str(model.value), "year": str(year.value)}
        year.value = None
        
    def check_dropdown():
        if all([make.value, model.value, year.value]):
            search_button.disabled = False
        else:
            search_button.disabled = True
    
    make = ft.Dropdown(
        expand=True,
        label='Make',
        on_change=make_selected,
        options=make_options,
    )
    
    model = ft.Dropdown(
        expand=True,
        label='Model',
        on_change=model_selected,
        options=[], # empty since make_change will change this 
    )
    
    year = ft.Dropdown(
        expand=True,
        label='Year',
        on_change=year_selected,
        options=[],
    )
        
    search_button = ft.ElevatedButton(
        text='Search',
        height= 45,
        disabled=True,
        style = ft.ButtonStyle(
            color = {
                    ft.MaterialState.DEFAULT: ft.colors.WHITE,
                },
                bgcolor= {
                    ft.MaterialState.DEFAULT: ft.colors.PRIMARY,
                },
                overlay_color=ft.colors.LIGHT_BLUE_800,
        ),
        on_click= lambda _: page.go('/car'),
    )

    return ft.View(
        '/home',
        scroll=True,
        bgcolor=ft.colors.GREY_300,
        controls=[
            ft.AppBar(
                title=ft.Text(
                    'Mod My Ride',
                    color=ft.colors.WHITE,
                    size=25,
                    weight=ft.FontWeight.BOLD,
                ),
                center_title=True,
                bgcolor=ft.colors.PRIMARY,
                actions=[
                    ft.PopupMenuButton( # settings button
                        ft.Icon(
                            name=ft.icons.DEHAZE_ROUNDED,
                            color=ft.colors.WHITE,
                        ),
                        items=[
                            ft.PopupMenuItem(
                                content=ft.Row(
                                    [
                                        ft.Icon(
                                            ft.icons.PERSON,
                                        ),
                                        ft.Text(
                                            'Profile'
                                        ),
                                    ]
                                ),
                                on_click= lambda _: page.go('/profile'),
                            ),
                            ft.PopupMenuItem(
                                content=ft.Row(
                                    [
                                        ft.Icon(
                                            ft.icons.FAVORITE_SHARP,
                                        ),
                                        ft.Text(
                                            'Saves',
                                        ),
                                    ]
                                ),
                                on_click=alert(page, 'In Progress', 'We\'re diligently working on the feature', 'Okay', '/home'),
                            ),
                            ft.PopupMenuItem(), # diviider
                            
                            ft.PopupMenuItem(
                                content=ft.Row(
                                    [
                                        ft.Icon(
                                            ft.icons.LOGOUT,
                                            color=ft.colors.RED,
                                        ),
                                        ft.Text(
                                            'Logout',
                                            color=ft.colors.RED,
                                        )
                                    ]
                                ),
                                on_click= alert_with_actions(page, 'Logout?', 'Are you sure you want to logout?', 'Cancel', 'Logout', '/'),
                            ),
                        ]
                    ),
                    # to add a space to the next of the setting icon
                    ft.Row(
                        width=5,
                    ),
                ]
            ),# end of appbar
            
            ft.Container(
                
                ft.Stack(
                    [
                        ft.Image(
                        src=f'/Users/bennyjoram/Desktop/MMR - github/Capstone/mod_my_ride/assets/home_page.png',
                        height=500,
                        fit=ft.ImageFit.FIT_HEIGHT,
                        ),
                        ft.Column(
                            [   
                                ft.Container(
                                    height=30,
                                ),
                                ft.Card(
                                    ft.Container(
                                        bgcolor=ft.colors.WHITE,
                                        border_radius=20,
                                        content = ft.Text(
                                            'Search your car',
                                            size=20,
                                        ),
                                        padding = 10,
                                    ),
                                ),
                                
                                ft.Card(
                                    ft.Container(
                                        bgcolor=ft.colors.WHITE,
                                        border_radius=20,
                                        content=ft.Column(
                                            controls=[
                                                ft.Row(
                                                    controls=[
                                                        make,
                                                        model,
                                                        year
                                                    ],
                                                ),
                                            ],
                                        ),
                                        padding=20,
                                    ),
                                ),
                                
                                search_button, 
                                
                                ft.Container( # to add some space on top
                                    height=215,
                                ),
                                
                                ft.Text(
                                    "IMPORTANT NOTE: Please use this app for checking out modifications for your vehicle. " +
                                    "When you enter your vehicle information, some styles may come up, that will not be an exact fit, in all sizes and widths. " +
                                    "This app should be used for style ideas only, not as a fitment guide. If your vehicle does not appear in the menu, " +
                                    "it does not mean that we don't offer modifications for it. " +
                                    "Please contact your local dealer for proper application and availability or call for fitment.",
                                    text_align='center',
                                    color=ft.colors.BLACK,
                                ),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ],
                ),
                #border_radius=5,
                padding = 0,
                height = 500,
                width= 880,
                alignment=ft.alignment.center,
            ),
        ],
        horizontal_alignment='center',
        padding=0,
    )