import streamlit as st
from uas.pages import home, data_uploud, data_visualization, model_training
from uas.utils import set_page_config, load_css

def main():
    #set page configuration
    set_page_config()
    #load custom css
    load_css()
    #sidebar navigation
    st.sidebar.title("navigation")
page = st.sidebar.radio("go to", ["home", "data uploud", "data visualization", "model training"])
    if page == "home":
        home.app()
    elif page == "data_uploud":
        data_uploud.app()
    elif page == "data_visualization":
        data_visualization.app()
    elif page == "model_training":
        model_training.app()
    
if __name__ == "__main__":
    main()
    st.sidebar.title("navigation")
    page = st.sidebar.radio("go to", ["home", "data uploud", "data visualization", "model training"])
    if page == "home":
        home.app()
    elif page == "data_uploud":
        data_uploud.app()
    elif page == "data_visualization":
        data_visualization.app()
    elif page == "model_training":
        model_training.app()
    st.sidebar.title("navigation")
    page = st.sidebar.radio("go to", ["home", "data uploud", "data visualization", "model training"])
    if page == "home":
        home.app()
    elif page == "data_uploud":
        data_uploud.app()
    elif page == "data_visualization":
        data_visualization.app()
    elif page == "model_training":
        model_training.app()

    st.sidebar.title("navigation")
    page = st.sidebar.radio("go to", ["home", "data uploud", "data visualization", "model training"])
    if page == "home":
        home.app()      
    elif page == "data_uploud":
        data_uploud.app()
    elif page == "data_visualization":
        data_visualization.app()
    elif page == "model_training":
        model_training.app()
    


    