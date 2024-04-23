import flet as ft
from flet import *
from flet_route import Params, Basket
from functions.adaptive_alert import *

def profile(page: ft.Page, params: Params, basket: Basket):
    data = basket.get('data')
    email = data['email']
    first_name = data['first_name']
    last_name = data['last_name']
    
    return ft.View(
        '/profile',
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
                    'Profile',
                    color=ft.colors.WHITE,
                    size=25,
                    weight=ft.FontWeight.BOLD,
                ),
            ),
            
            ft.Icon(
                ft.icons.PERSON,
                size=100,
            ),
            
            ft.Card(
                ft.Container(
                    bgcolor=ft.colors.WHITE,
                    content=ft.Column(
                        [
                            ft.Text(
                                f"{first_name} {last_name}",
                            ),
                            ft.Text(
                                f"{email}",
                            ),
                            ft.TextButton(
                                text="Change Info",
                                on_click=alert(page, 'In Progress', 'We\'re diligently working on the feature', 'Okay', '/profile'),
                            ),
                            ft.TextButton(
                                text='Change Password',
                                on_click=alert(page, 'In Progress', 'We\'re diligently working on the feature', 'Okay', '/profile'),
                            ),
                            ft.TextButton(
                                icon=ft.icons.LOGOUT,
                                icon_color=ft.colors.RED,
                                text='Logout',
                                style=ft.ButtonStyle(
                                    color=ft.colors.RED,
                                ),
                                on_click= alert_with_actions(page, 'Logout?', 'Are you sure you want to logout?', 'Cancel', 'Logout', '/'),
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    border_radius=20,
                    padding=10,
                    width=300,
                    alignment=ft.alignment.center,
                ),
            ),
        ],
        vertical_alignment='center',
        horizontal_alignment='center',
        spacing=10,
    )