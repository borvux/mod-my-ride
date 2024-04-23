import logging
import flet as ft
logging.basicConfig(level=logging.DEBUG)

def alert(page, alert_title, alert_content, action, on_click_action):
    actions = []
    if page.platform in ['ios', 'macos']:
        actions = [
            ft.CupertinoDialogAction(action, on_click= lambda _: close_adaptive_dialog()),
        ]
    else:
        actions = [
            ft.TextButton(action, on_click = lambda _: close_adaptive_dialog()),
        ]
        
    adaptive_alert_dialog = ft.AlertDialog(
        adaptive = True,
        title = ft.Text(alert_title),
        content= ft.Text(alert_content),
        actions=actions,
    )
    
    # to close the dialog alert and go back to the another page
    def close_adaptive_dialog():
        adaptive_alert_dialog.open = False
        page.go(on_click_action)
        page.update()
    
    # to open the dialog alert
    def open_adaptive_dialog(e):
        page.dialog = adaptive_alert_dialog
        adaptive_alert_dialog.open = True
        page.update()
        
    return open_adaptive_dialog

def alert_with_actions(page, alert_title, alert_content, first_action, second_action, on_click_second_action):
    # just to close the dailog
    def close_dialog():
        adaptive_alert_dialog.open = False
        page.update()
        
    # to close the dialog alert and go back to the another page
    def close_adaptive_dialog():
        adaptive_alert_dialog.open = False
        page.go(on_click_second_action)
        page.update()
        
    actions = []
    if page.platform in ['ios', 'macos']:
        actions = [
            ft.CupertinoDialogAction(first_action, on_click = lambda _: close_dialog()),
            ft.CupertinoDialogAction(second_action, is_destructive_action=True, on_click = lambda _: close_adaptive_dialog()),
        ]
    else:
        actions = [
            ft.TextButton(first_action, on_click = lambda _: close_dialog()),
            ft.TextButton(second_action, is_destructive_action=True, on_click = lambda _: close_adaptive_dialog()),
        ]
        
    adaptive_alert_dialog = ft.AlertDialog(
        adaptive = True,
        title = ft.Text(alert_title),
        content= ft.Text(alert_content),
        actions=actions,
    )
    
    # to open the dialog alert
    def open_adaptive_dialog(e):
        page.dialog = adaptive_alert_dialog
        adaptive_alert_dialog.open = True
        page.update()
        
    return open_adaptive_dialog