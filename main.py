import streamlit as st

from streamlit_option_menu import option_menu
st.set_page_config(
        page_title="AI HELP",
)

import home,webcam,vision,translate,chat




class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='AI help ',
                options=['Home','Emergency Call','Complaints','Text Complaints','Chat'],
                icons=['house-fill','person-circle','trophy-fill','chat-fill','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        
        if app == "Home":
            home.app()
        if app == "Emergency Call":
            webcam.app()    
        if app == "Complaints":
            vision.app()        
        if app == 'Text Complaints':
            translate.app()
        if app == 'Chat':
            chat.app()    
             
          
             
    run()            
         


               
               
               
          
           



