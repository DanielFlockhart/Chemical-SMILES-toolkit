# import tkinter as tk
# from tkinter import ttk
# colour_codes = {
#     "btn" : {"text" : "#000000", "inactive" : "#4BBF60","active" : "#7bd18b"},
#     "lbl" : "#FFFFFF",
#     "title": {"text": "#000000"},
#     "background" : "#202940"
# }


# def create_button_style():
#     button_style = ttk.Style()

#     # Define button style
#     button_style.configure("Button.TButton",
#                             foreground=colour_codes["btn"]["text"],
#                             # Set the button color to a green color
#                             activebackground=colour_codes["btn"]["inactive"],
#                             font=("Arial", 12, "bold"),
#                             padding=10,
#                             relief="raised")

#     # Define button hover style
#     button_style.map("Button.TButton",
#                         background=[("pressed", "!disabled", "#008000"),  # Green when pressed
#                           ("active", "#00FF00")])
                        
#                         #relief=[("active", "sunken")])
#     return button_style

# def create_title_style():
#     title_style = ttk.Style()
    
#     # Define label style
#     # Define label style
#     title_style.configure("Title.TLabel", background=colour_codes["background"],
#                             foreground=colour_codes["title"]["text"],  # Change text color to black
#                             font=("Arial", 24, "bold"),
#                             padding=10)
#     return title_style

# def create_label_style():
#     label_style = ttk.Style()
    
#     # Define label style
#     label_style.configure("Label.TLabel",
#                             background=colour_codes["background"],
#                             foreground=colour_codes["lbl"],  # Change text color to black
#                             font=("Arial", 12, "bold"),
#                             padding=10)
#     return label_style
