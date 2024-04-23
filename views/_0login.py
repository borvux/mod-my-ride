import flet as ft
from flet import *
from flet_route import Params, Basket
import pyrebase
from functions.adaptive_alert import alert # import alert function
from functions.mysql import execute_query # import db connection and query
from config import firebase

# things to install to make this app works 
# pip install flet
# pip install flet-routing
# pip install python-dotenv
# pip install pyrebase4
# pip install setuptools

# initilize firebase for authentication
firebase = pyrebase.initialize_app(firebase())
# set up authentication manager for firebase 
auth = firebase.auth()

# login method 
def login(page: ft.Page, params: Params, basket: Basket):
    
    
    # validate sign-in textfields 
    def signin_validate(e):
        # if there are values in the email and password textfield
        if all([email.value, password.value]):
            # then the sign-in button will be enable
            button_signin.disabled = False
        else: # else the sign-in button will be disable
            button_signin.disabled = True
        page.update()
        
    
    # email and password textfields 
    email = ft.TextField(label='Email', hint_text="@email.com")
    password = ft.TextField(label='Password',password=True, can_reveal_password=True)
    
    
    # to see if there are text in the textfields
    email.on_change = signin_validate
    password.on_change = signin_validate
    
    
    # when a user try to sign-in, this method will be called 
    def sign_in(e):
        try:
            # using the email and password textfield values 
            # check with the firebase authentication
            auth.sign_in_with_email_and_password(email.value, password.value)
            
            # connect to the MySQL db and get the user informations
            data = execute_query(f"select * from users where email = %s", (email.value,))
            user_email = data[0][0]
            first_name = data[0][1]
            last_name = data[0][2]
            
            # put the user information into basket cookies
            basket.data = {"email": user_email, "first_name": first_name, "last_name": last_name}
            
            # if the sign-in is authenticated, then go to the home page
            page.go('/home')
            page.update()
            
        except:
            # if the autentication failed, then alert the user
            open_dialog = alert(page, "Login Failed", "Invalid Email or Password", "Okay", "/")
            open_dialog(None) # this is to make the alert go away once clicked on 
          
          
    # continue as guest method 
    def guest(e):   
        # put guest profile in the basket cookies   
        basket.data = {"email": "Guest Profile", "first_name": " ", "last_name": " "}
        page.go('/home')
        page.update()
        
        
    # elevated button for sign-in
    button_signin = ft.ElevatedButton(
                        text='Login',
                        width=250, height=45,
                        disabled=True,
                        style=ft.ButtonStyle(
                            color = {
                                ft.MaterialState.DEFAULT: ft.colors.WHITE,
                            },
                            bgcolor= {
                                ft.MaterialState.DEFAULT: ft.colors.PRIMARY,
                            },
                            overlay_color=ft.colors.LIGHT_BLUE_800,
                        ),
                        # using the sign_in method above onced clicked
                        on_click=sign_in)
    
    '''
    test user credientals saved in the firebase and MySQL
    test@gmail.com
    test1234
    '''
    
    # login card 
    login = ft.Card(
        ft.Container(
            width=600,
            bgcolor=ft.colors.WHITE,
            border_radius= 20,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls= [
                    email, # call the email textfields
                    password, # call the password textfields 
                    
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls= [
                            ft.Checkbox( # this checkbox is not complete yet
                                label = 'Remember Me',
                                adaptive=True, 
                                value=False,
                            ),
                            ft.TextButton(
                                text='Forgot Password?',
                                on_click= lambda _: page.go('/forgot')
                            ),
                        ]
                    ),
                    
                    ft.Column(
                        controls = [
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    button_signin, # sign-in button
                                ]
                            ),
                            
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.ElevatedButton(
                                        text = 'Continue as Guest',
                                        style = ft.ButtonStyle(
                                            color = {
                                                ft.MaterialState.DEFAULT: ft.colors.WHITE,
                                            },
                                            bgcolor= {
                                                ft.MaterialState.DEFAULT: ft.colors.PRIMARY,
                                            },
                                            overlay_color=ft.colors.LIGHT_BLUE_800,
                                        ),
                                        width=250,
                                        height=45,
                                        on_click= guest # using the guest method above
                                    )
                                ]
                            ),
                        ]
                    ),
                    
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                'Don\'t have an account?',
                                size = 13
                            ),
                            ft.TextButton(
                                text = 'Create an account',
                                on_click= lambda _: page.go('/signup')
                            )
                        ]
                    )
                ],
            ),
            padding = 20
        )
    )
    
    
    # return the view when its called from other views 
    return ft.View(
        '/', # root view
        bgcolor=ft.colors.GREY_300,
        scroll=True,
        controls = [
            ft.Container( # to add some space on top
                height=20,
            ),
            ft.Image(
                src=f'/Users/bennyjoram/Desktop/mod_my_ride/assets/MMR_logo.png',
                width=150,
                height=150,
            ),
            ft.Text(
                'Mod My Ride',
                font_family = 'Consolas',
                text_align=ft.TextAlign.CENTER,
                color = ft.colors.PRIMARY,
                size=60,
                weight=ft.FontWeight.W_700,
            ),
            login, # call the login UI section
        ],
        vertical_alignment='center',
        horizontal_alignment='center',
    )
