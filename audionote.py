import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os
import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime

main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title('AUDIOPOPAD')


# Main menu
main_menu = tk.Menu()

# file
file = tk.Menu(main_menu, tearoff=False)

new_icon = tk.PhotoImage(file='icons2/new.png')
open_icon = tk.PhotoImage(file='icons2/open.png')
save_icon = tk.PhotoImage(file='icons2/save.png')
save_as_icon = tk.PhotoImage(file='icons2/save_as.png')
exit_icon = tk.PhotoImage(file='icons2/exit.png')

file.add_command(label="New", image=new_icon, compound=tk.LEFT, accelerator='Ctrl+N')
file.add_command(label="Open", image=open_icon, compound=tk.LEFT, accelerator='Ctrl+N')
file.add_command(label="Save", image=save_icon, compound=tk.LEFT, accelerator='Ctrl+N')
file.add_command(label="Save As", image=save_as_icon, compound=tk.LEFT, accelerator='Ctrl+N')
file.add_command(labe="Exit", image=exit_icon, compound=tk.LEFT, accelerator='Ctrl+N')

# Edit
edit = tk.Menu(main_menu, tearoff=False)

copy_icon = tk.PhotoImage(file='icons2/copy.png')
paste_icon = tk.PhotoImage(file='icons2/paste.png')
cut_icon = tk.PhotoImage(file='icons2/cut.png')
clear_all_icon = tk.PhotoImage(file='icons2/clear_all.png')
find_icon = tk.PhotoImage(file='icons2/find.png')

edit.add_command(label='Copy', image=copy_icon, compound=tk.LEFT, accelerator='Ctrl+C')
edit.add_command(label='Paste', image=paste_icon, compound=tk.LEFT, accelerator='Ctrl+V')
edit.add_command(label='Cut', image=cut_icon, compound=tk.LEFT, accelerator='Ctrl+X')
edit.add_command(label='Clear All', image=clear_all_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+X')
edit.add_command(label='Find', image=find_icon, compound=tk.LEFT, accelerator='Ctrl+F')

# View
view = tk.Menu(main_menu, tearoff=False)

tool_bar_icon = tk.PhotoImage(file='icons2/tool_bar.png')
status_bar_icon = tk.PhotoImage(file='icons2/status_bar.png')

view.add_checkbutton(label='Tool Bar', image=tool_bar_icon, compound=tk.LEFT)
view.add_checkbutton(label='Status Bar', image=status_bar_icon, compound=tk.LEFT)

# Color theme
color_theme = tk.Menu(main_menu, tearoff=False)

light_default_icon = tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons2/light_plus.png')
dark_icon = tk.PhotoImage(file='icons2/dark.png')
red_icon = tk.PhotoImage(file='icons2/red.png')
monokai_icon = tk.PhotoImage(file='icons2/monokai.png')
night_blue_icon = tk.PhotoImage(file='icons2/night_blue.png')
pink_icon = tk.PhotoImage(file='icons2/pink.png')
yellow_icon = tk.PhotoImage(file='icons2/yellow.png')

theme_choice = tk.StringVar()
color_icons = (
light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon, pink_icon, yellow_icon)

color_dict = {
    'Light Default': ('#000000', '#ffffff'),
    'Light Plus': ('#474747', '#e0e0e0',),
    'Dark': ('#c4c4c4', '#2d2d2d'),
    'Red': ('#8a0b13', '#f0e9e9'),
    'Monokai': ('#d3b774', '#474747'),
    'Night Blue': ('#ededed', '#6b9dc2'),
    'Pink': ('#2d2d2d', '#ffe8e8'),
    'Yellow': ('#ccc929', '#171710')
}

count = 0
for i in color_dict:
    color_theme.add_radiobutton(label=i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT)
    count += 1

# cascade
main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Colour Theme', menu=color_theme)

# tool bar
tool_bar = tk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X)

# font-box
tk_font_names = font.families()
userInput_font_name = tk.StringVar()
font_name = ttk.Combobox(tool_bar, width=35, textvariable=userInput_font_name, state='readonly')
font_name['values'] = tk_font_names
font_name.current(tk_font_names.index('Arial'))
font_name.grid(row=0, column=0, padx=4, pady=2)

# sizebox
user_input_font_size = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width=30, textvariable=user_input_font_size, state="readonly")
x = (i for i in range(2, 81))
sizes = tuple(x)
font_size['values'] = sizes
font_size.current(sizes.index(12))
font_size.grid(row=0, column=1, padx=4, pady=2)

# bold button
bold_icon = tk.PhotoImage(file='icons2/bold.png')
bold_button = ttk.Button(tool_bar, image=bold_icon)
bold_button.grid(row=0, column=2, padx=4, pady=2)

# italic button
italic_icon = tk.PhotoImage(file='icons2/italic.png')
italic_button = ttk.Button(tool_bar, image=italic_icon)
italic_button.grid(row=0, column=3, padx=4, pady=2)

# underline button
underline_icon = tk.PhotoImage(file='icons2/underline.png')
underline_button = ttk.Button(tool_bar, image=underline_icon)
underline_button.grid(row=0, column=4, padx=4, pady=2)

# font color button
font_color_icon = tk.PhotoImage(file='icons2/font_color.png')
font_color_button = ttk.Button(tool_bar, image=font_color_icon)
font_color_button.grid(row=0, column=5, padx=4, pady=2)

# left align button
left_icon = tk.PhotoImage(file='icons2/left.png')
left_button = ttk.Button(tool_bar, image=left_icon)
left_button.grid(row=0, column=6, padx=4, pady=2)

# center align button
center_icon = tk.PhotoImage(file='icons2/center.png')
center_button = ttk.Button(tool_bar, image=center_icon)
center_button.grid(row=0, column=7, padx=4, pady=2)

# right align button
right_icon = tk.PhotoImage(file='icons2/right.png')
right_button = ttk.Button(tool_bar, image=right_icon)
right_button.grid(row=0, column=8, padx=4, pady=2)

# speak button
speak_icon = tk.PhotoImage(file='icons2/speak.png')
speak_button = ttk.Button(tool_bar, image=speak_icon)
speak_button.grid(row=0, column=9, padx=12, pady=2)

# listen button
listen_icon = tk.PhotoImage(file='icons2/listen.png')
listen_button = ttk.Button(tool_bar, image=listen_icon)
listen_button.grid(row=0, column=10, padx=0, pady=2)

# scroll bar
sb = tk.Scrollbar(main_application)
sb.pack(side=tk.RIGHT, fill=tk.Y)

# text window
text_window = tk.Text(main_application)
text_window.focus_set()
text_window.pack(fill=tk.BOTH, expand='true')
sb.config(command=text_window.yview)
text_window.config(wrap='word', relief=tk.FLAT, yscrollcommand=sb.set)
current_font_family = 'Arial'
current_font_size = 12

#font settings
def font_property_func(event=None):
    global current_font_family
    global current_font_size
    current_font_family = userInput_font_name.get()
    current_font_size = user_input_font_size.get()
    text_window.configure(font=(current_font_family, current_font_size))


font_name.bind("<<ComboboxSelected>>", font_property_func)
font_size.bind("<<ComboboxSelected>>", font_property_func)

text_window.configure()


#button settings
def bold_button_sett():
    text_property = font.Font(font=text_window['font'])
    print(text_property)
    if text_property.actual()['weight'] == 'normal':
        text_window.configure(font=(current_font_family, current_font_size, 'bold'))
        print(text_property)
    if text_property.actual()['weight'] == 'bold':
        text_window.configure(font=(current_font_family , current_font_size, 'normal'))
        print(text_property)


bold_button.configure(command=bold_button_sett)


# italic functionlaity
def change_italic():
    text_property = tk.font.Font(font=text_window['font'])
    print(text_property)
    if text_property.actual()['slant'] == 'roman':
        text_window.configure(font=(current_font_family, current_font_size, 'italic'))
        print(text_property)
    if text_property.actual()['slant'] == 'italic':
        text_window.configure(font=(current_font_family, current_font_size, 'normal'))
        print(text_property)


italic_button.configure(command=change_italic)


# underline functionality
def change_underline():
    text_property = tk.font.Font(font=text_window['font'])
    print(text_property)
    if text_property.actual()['underline'] == 0:
        text_window.configure(font=(current_font_family, current_font_size, 'underline'))
        print(text_property)
    if text_property.actual()['underline'] == 1:
        text_window.configure(font=(current_font_family, current_font_size, 'normal'))
        print(text_property)


underline_button.configure(command=change_underline)


#font color functionality
def font_color_change():
    user_input_color = tk.colorchooser.askcolor()
    #print(user_input_color)
    text_window.configure(fg=user_input_color[1])


font_color_button.configure(command=font_color_change)


#aligning functionality
def left_align():
    text_content = text_window.get(1.0, 'end')
    #print(text_content)
    text_window.tag_config('left', justify=tk.LEFT)
    text_window.delete(1.0, tk.END)
    text_window.insert(tk.INSERT, text_content, 'left')


left_button.configure(command=left_align)


def center_align():
    text_content = text_window.get(1.0, 'end')
    #print(text_content)
    text_window.tag_config('center', justify=tk.CENTER)
    text_window.delete(1.0, tk.END)
    text_window.insert(tk.INSERT, text_content, 'center')

center_button.configure(command=center_align)


def right_align():
    text_content = text_window.get(1.0, 'end')
    text_window.tag_config('right', justify=tk.RIGHT)
    text_window.delete(1.0, tk.END)
    text_window.insert(tk.INSERT, text_content, 'right')


right_button.configure(command=right_align)



def chec(event=None):
    newwin = tk.Toplevel(main_application)
    newwin.geometry('200x800')
    lab = tk.Label(newwin, text='ho gaya......')
    lab.grid(row=0,column=1)

def call(event=None):
    newWindow = tk.Toplevel(main_application)
    newWindow.geometry('250x400')
    lab = tk.Label(newWindow, text='ho gaya......')
    lab.grid(row=0, column=2)

    newWindow_sb = tk.Scrollbar(newWindow)
    newWindow_sb.pack(side=tk.RIGHT, fill=tk.Y)
    textWindow_recogniseResponse = tk.Text(newWindow)
    textWindow_recogniseResponse.focus_set()
    textWindow_recogniseResponse.pack(fill=tk.BOTH, expand='true')
    newWindow_sb.config(command=textWindow_recogniseResponse.yview)
    textWindow_recogniseResponse.config(wrap='word', relief=tk.FLAT, yscrollcommand=newWindow_sb.set)
    newWindow_font_family = 'Arial'
    newWindow_font_size = 12
    textWindow_recogniseResponse.configure(font=(newWindow_font_family, newWindow_font_size))'''


    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    print(voices)
    engine.setProperty('voice', voices[0].id)

    def speak(audio):
        '''this function will take an string argument
        and speak it through speaker '''
        engine.say(audio)
        engine.runAndWait()

    def wishme():
        '''this function will speak
        and wish the user according to time'''

        hour = (int(datetime.datetime.now().hour))
        if (hour >= 0 and hour < 12):
            speak('hey haider! good morning dude')
            textWindow_recogniseResponse.insert(tk.INSERT,'hey haider! good morning dude')
        elif hour >= 12 and hour < 16:
            speak('hey haider! good afternoon dude')

        else:
            speak('hey haider! good evening dude')
        speak("i am malaman , please tell me how may i help you")

    def commandtaking():
        '''this function will take an audio command and print it on screen
        and create a file named output.txt save the command as string in that file'''

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('say something..............')
            r.adjust_for_ambient_noise(source, duration=1)
            r.pause_threshold = 0.9
            r.dynamic_energy_threshold = True
            audio = r.listen(source)

        try:
            print('recognising....')
            print('text: ' + r.recognize_google(audio))
            query = r.recognize_google(audio)

            if str is bytes:
                result = u"{}".format(query).encode("utf-8")

            else:
                result = "{}".format(query)

            with open("outputs.txt", "a") as f:
                f.write(result)
        except:
            print('not recognised , speak again! ')
            return "None"
        return query

    if __name__ == "__main__":
        wishme()
        while (1):
            query = commandtaking().lower()
            if query == "none":
                print("DID NOT RECOGNISED")
            if query == "exit":
                print(query)
                break
            print(query)
            text_window.insert(tk.INSERT, query)

listen_button.configure(command=call)

# status bar
status_bar = ttk.Label(main_application, text='Status Bar')
status_bar.pack(side=tk.BOTTOM)


'''def stat():
    if text_window.edit_modified
'''






photo = tk.PhotoImage(file="icons2/malaman2.png")
main_application.iconphoto(False, photo)
main_application.config(menu=main_menu)
main_application.mainloop()
