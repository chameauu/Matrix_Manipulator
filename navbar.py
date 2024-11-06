import streamlit as st
from streamlit_navigation_bar import st_navbar
import os


def navbar():
    pages = ["Home", "User Guide", "API", "Examples", "GitHub","Account"]
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(parent_dir, "assets/logo/logo.svg")
    urls = {"GitHub": "https://github.com/MohamedAliJmal/Matrix_Manipulator"}
    styles = {
        
        "nav": {
            "background-color": "#4169e1",
            
            
        },
        "img": {
            "padding-right": "14px",
        },
        "span": {
            "color": "white",
            "padding": "14px",
            
        },
        "active": {
            "background-color": "white",
            "color": "black",
            "font-weight": "normal",
            "padding": "14px",
        }
    }


    
    return st_navbar(
        pages,
        logo_path=logo_path,
        urls=urls,
        styles=styles, 
    )
