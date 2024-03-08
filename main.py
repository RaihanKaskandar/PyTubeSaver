import tkinter  
import customtkinter
from pytube import YouTube     

def main():

    # System Settings
    customtkinter.set_appearance_mode("Light")
    customtkinter.set_default_color_theme("blue")

    # Create the main window
    app = customtkinter.CTk()  # create CTk window like you do with the Tk window
    app.geometry("1280x720")
    app.title("PyTubeSaver") 

    # Adding UI elements
    title = customtkinter.CTkLabel(app, text="Insert a YouTube link!", font=("Arial", 20))
    title.pack(padx=20, pady=10)

    # Link input
    url_var = tkinter.StringVar()
    link = customtkinter.CTkEntry(app, width=700, height=40, textvariable=url_var)
    link.pack(padx=10, pady=10)

    # # Download button
    # download = customtkinter.CTkButton(app, text="Download", command=startDownload)

    app.mainloop()




if __name__ == '__main__':
    main()