import streamlit
from streamlit_option_menu import option_menu

streamlit.title('HealthApp')

with stremlit.sidebar:
  selected = option_menu(
    menu_title = "Main Menu",
    options =["Home", "Projects","Contact"],
  )

if selected == "Home":
  streamlit.title(f"You have selected{selected}")
if selected == "Projeccts":
  streamlit.title(f"You have selected{selected}")  
if selected == "Conatcts":
  streamlit.title(f"You have selected{selected}")  
  
