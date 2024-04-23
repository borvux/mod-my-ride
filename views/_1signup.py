import flet as ft
from flet import *
from flet_route import Params, Basket
import json
import pyrebase
from config import firebase
from functions.mysql import execute_query
from functions.adaptive_alert import alert # get the dialog module

# initilize firebase
firebase = pyrebase.initialize_app(firebase())
# set up authentication manager for firebase 
auth = firebase.auth()

# sign up view function
def signup(page: ft.Page, params: Params, basket: Basket):
    
    # labels for email, fname, lname, password, repeat password textfields
    email = ft.TextField(label='Enter email', hint_text="@email.com")
    first_name = ft.TextField(label='First Name')
    last_name = ft.TextField(label='Last Name')
    password = ft.TextField(label='Password', password=True, can_reveal_password=True)
    repeat_password = ft.TextField(label='Repeat password', password=True, can_reveal_password=True)
    
    
    # to register user
    def register_user(e):
        try:
            # if the user type in the same password and repeated the same password,
            # then create the account with the email and password
            # if the password and repeat password 
            if password.value == repeat_password.value:
                # store the email and password into the firebase and MySQL
                auth.create_user_with_email_and_password(email.value, password.value)
                execute_query(f"insert into users values (%s, %s, %s)", (email.value, first_name.value, last_name.value,), is_insert=True)
                
                # store the email, fname, lname into the basket cookies
                basket.data = {"email": email.value, "first_name": first_name.value, "last_name": last_name.value}
                # open the alert to show that the user sucessfully registered 
                open_dialog = alert(page, "Registration Successful", "You have successfully registered", "Okay", "/home")
                open_dialog(None)
            else:
                # alert the user if the password is not the match
                open_dialog = alert(page, "ERROR", "Make sure the password are matching", "Okay", "/signup")
                open_dialog(None)
        
        # if the firebase authentication raises errors
        except Exception as e:
            # parse the Json HTTPError and get the message only
            error_message = json.loads(e.strerror)
            error = error_message['error']['message']
            
            # if the error is 'email exists'
            if error == "EMAIL_EXISTS":
                # alert the user about email exists error
                open_dialog = alert(page, "ERROR", "The email already exists", "Okay", "/signup")
                open_dialog(None)
            
            # if the error is 'weak password'
            elif error == "WEAK_PASSWORD : Password should be at least 6 characters":
                # alert the user about weark password
                open_dialog = alert(page, "ERROR", "Password should be at least 6 characters", "Okay", "/signup")
                open_dialog(None)
            
            # if the error is another other than that 
            else:
                # still alert the user 
                open_dialog = alert(page, "ERROR", "Something went wrong", "Okay", "/signup")
                open_dialog(None)
    
    
    # return the view
    return ft.View(
        '/signup', # this is the signup view
        scroll=True,
        bgcolor=ft.colors.GREY_300,
        controls = [
            ft.AppBar(
                leading = ft.IconButton( # go back to login view button
                    ft.icons.ARROW_BACK,
                    on_click= lambda _: page.go('/'),
                    icon_color= ft.colors.WHITE,
                    tooltip='back',
                ),
                title=ft.Text(
                    'CREATE YOUR ACCOUNT',
                    color=ft.colors.WHITE,
                    size=25,
                    weight=ft.FontWeight.BOLD,
                ),
                center_title=True,
                bgcolor=ft.colors.PRIMARY,
            ),
            
            ft.Icon(
                ft.icons.PERSON,
                size=100,
                color=ft.colors.PRIMARY,
            ),
            
            ft.Card(
                ft.Container(
                    width=600,
                    bgcolor=ft.colors.WHITE,
                    border_radius= 20,
                    content=ft.Column(
                        controls=[
                            email,              # email textfield
                            first_name,         # first name textfield
                            last_name,          # last name textfield
                            password,           # password textfield
                            repeat_password,    # repeat password textfield
                            
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls= [
                                    ft.ElevatedButton(
                                        'Create Account',
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
                                        on_click = register_user # call the register_user method 
                                    ),
                                ]
                            ),
                        ],
                        spacing=25,
                    ),
                    padding=20,
                )
            ),
        ],
        vertical_alignment='center',
        horizontal_alignment='center',
    )