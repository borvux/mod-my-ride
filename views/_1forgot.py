import flet as ft
from flet import *
from flet_route import Params, Basket
from functions.adaptive_alert import alert

def forgot(page: ft.Page, params: Params, basket: Basket):
    
    # return the view of the forgot 
    return ft.View(
        '/forgot',
        scroll=True,
        bgcolor=ft.colors.GREY_300,
        controls=[
            ft.AppBar(
                leading = ft.IconButton( # back button to the login view
                    ft.icons.ARROW_BACK,
                    icon_color= ft.colors.WHITE,
                    on_click= lambda _: page.go('/'),
                    tooltip='back',
                ),
                title = ft.Text(
                    'FORGOT PASSWORD',
                    color=ft.colors.WHITE,
                    size=25,
                    weight=ft.FontWeight.BOLD,
                ), 
                center_title=True, 
                bgcolor = ft.colors.PRIMARY,
            ),
            
            ft.Container( # to add some space on top
                height=20,
            ),
            
            ft.Icon(
                ft.icons.LOCK_OUTLINE_ROUNDED,
                size=120,
                color=ft.colors.PRIMARY,
            ),
            
            ft.Card(
                ft.Container(
                    width=600,
                    bgcolor=ft.colors.WHITE,
                    border_radius= 20,
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Text(
                                        'Trouble Logging in?',
                                        size=30,
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                ]
                            ),
                            
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Text(
                                        'Enter your email and we\'ll send\nyou a link to reset your password.',
                                        size = 20,
                                        text_align= ft.TextAlign.CENTER,
                                    ),
                                ]
                            ),
                            
                            ft.TextField(
                                label='Enter email',
                                hint_text="@email.com",
                            ),
                            
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.ElevatedButton( # rest password button that is not complete
                                        text = 'Reset Password', 
                                        width=250,
                                        height=45,
                                        style = ft.ButtonStyle(
                                            color = {
                                                ft.MaterialState.DEFAULT: ft.colors.WHITE,
                                            },
                                            bgcolor= {
                                                ft.MaterialState.DEFAULT: ft.colors.PRIMARY,
                                            },
                                            overlay_color=ft.colors.LIGHT_BLUE_800,
                                        ),
                                        # open an alert when clicked 
                                        on_click = alert(page, 'Password Reset', 'Check your email to reset', 'Okay', '/'),
                                    ),
                                ]
                            )
                        ],
                        spacing=20,
                    ),
                    padding = 20,
                )
            ),
        ],
        vertical_alignment='center',
        horizontal_alignment='center',
    )