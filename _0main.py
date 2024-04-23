import flet as ft
from flet_route import Routing, path
from views._0login import login
from views._1forgot import forgot
from views._1signup import signup
from views._2home import home 
from views._3profile import profile
from views._4car import car

def main(page: ft.Page):
    page.theme_mode = "light"
    
    # routes for each views 
    routes = [
        path(url = '/', clear = True, view = login),
        path(url = '/signup', clear = True, view = signup),
        path(url = '/forgot', clear = True, view = forgot),
        path(url = '/home', clear = True, view = home),
        path(url = '/profile' , clear = True, view = profile),
        path(url = '/car', clear = True, view = car),
    ]

    Routing(page = page, app_routes = routes)
    page.go(page.route)

ft.app(target=main, assets_dir="mod_my_ride/assets") #, view=ft.AppView.WEB_BROWSER
#ft.app(target=main, view=ft.AppView.WEB_BROWSER, assets_dir='mod_my_ride/assets')

