import PIL.Image
import PIL.ImageTk
import customtkinter as ctk
import os
from colorama import Fore

red = Fore.RED
cyan = Fore.CYAN
reset = Fore.RESET

# $ REWRITING THE MAIN CLASS
class Aa:
    try:
        def __init__(self):
            pass
        __errors = [
            "Error 0: Content Is NULL",
            "Error 1: Img Is Not Found"
        ]
        __imgsPath = [
            r'imgs/close.png',
            r'imgs/check.png',
            r'imgs/info.png',
            r'imgs/warn.png',
            r"imgs/custom.png",
            r"imgs/icon.png"
        ]

        def FileFinder(self,imgPath:str=None):
            if imgPath is None: return None
            else: 
                File = os.path.abspath(__file__)
                Dir = os.path.dirname(File)
                FilePath = os.path.join(Dir, imgPath)
                return FilePath

        def creatingApp(self ,title=None ,content="AuraAlerts Content!!" ,theme="light"):
            app = ctk.CTk()
            app.resizable(False,False)
            
            if title:app.title('AuraAlerts Title!!')
            else:app.title(title)

            ctk.set_appearance_mode(theme)

            height = len(content)
            width = len(content) 

            app._max_height = height+100
            app._max_width = width+200

            # $ Icon
            icon = self.__imgsPath[5]
            iconPath = self.FileFinder(icon)

            if os.path.exists(iconPath):
                image = PIL.Image.open(iconPath)
                photo = PIL.ImageTk.PhotoImage(image)
                app.iconbitmap(iconPath,False)
                app.iconphoto(False,photo)
            return app


        def creatingWindow(self,title ,content ,buttonText,buttonColor,buttonHoverColor, textColor,img,theme):
            app = self.creatingApp(title, content, theme)
            
            imgPath = self.FileFinder(img)
            if imgPath:
                photoImage = PIL.Image.open(imgPath)
                CTK_image = ctk.CTkImage(light_image=photoImage,dark_image=photoImage,size=(33,33))
                ShowImage = ctk.CTkLabel(app,text='',image=CTK_image)
                ShowImage.pack(anchor='center',pady=6)
            else:print(self.__errors[1])
            
            # $ creating label content
            LabelContent = ctk.CTkLabel(app, text=content)
            LabelContent.pack(padx=10)

            # $ Frame
            Frame = ctk.CTkFrame(app,fg_color='#333',bg_color='#333',height=30)
            Frame.pack(fill='both', anchor='center')
            Button = ctk.CTkButton(Frame,text='close', fg_color=buttonColor,hover_color=buttonHoverColor,text_color=textColor, command=lambda:app.destroy(),width=10, corner_radius=4)
            
            # $ button
            if self.custom:
                Button.configure(text=buttonText)
                Button.pack(anchor='e', pady=5, padx=10)
            else:
                Button.pack(anchor='e', pady=5, padx=10)



            app.mainloop()
            # app


        def error(self, title, content, theme='light'):
            Image = self.FileFinder(self.__imgsPath[0])
            self.creatingWindow(title=title,content=content,buttonText='close',buttonColor="#ff5757", buttonHoverColor="#cc3838", textColor="#363636",img=Image,theme=theme)
        
        def success(self, title, content, theme='light'):
            Image = self.FileFinder(self.__imgsPath[1])
            self.creatingWindow(title=title,content=content,buttonText='close',buttonColor="#57ff89", buttonHoverColor="#4bd274", textColor="#363636",img=Image,theme=theme)

        def info(self, title, content, theme='light'):
            Image = self.FileFinder(self.__imgsPath[2])
            self.creatingWindow(title=title,content=content,buttonText='close',buttonColor="#5cc0ff", buttonHoverColor="#53b0ea", textColor="#363636",img=Image,theme=theme)

        def warn(self, title, content, theme='light'):
            Image = self.FileFinder(self.__imgsPath[3])
            self.creatingWindow(title=title,content=content,buttonText='close',buttonColor="#ffbb5c", buttonHoverColor="#d79f50", textColor="#363636",img=Image,theme=theme)
            
        def custom(self, title, content, buttonText='close',buttonColor="#b55dfd" , buttonHoverColor="#a055dd", textColor="#363636", img=None, theme='light'):
            if img is None:
                Image = self.FileFinder(self.__imgsPath[4])
                self.creatingWindow(title=title,content=content, buttonText=buttonText,buttonColor=buttonColor, buttonHoverColor=buttonHoverColor, textColor=textColor,img=Image,theme=theme)
            else:
                Image = self.FileFinder(img)
                self.creatingWindow(title=title,content=content, buttonText=buttonText,buttonColor=buttonColor, buttonHoverColor=buttonHoverColor, textColor=textColor,img=Image,theme=theme)
    except Exception as error:
        print(f'{red}Error{cyan}:{error}{reset}')
