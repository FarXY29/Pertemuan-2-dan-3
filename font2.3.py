import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Latihan Pertama",
                   layout=[[sg.Text("FTI UNISKA"
                                    ,font=("Helvetica",24))],
                           [sg.Text("FAKULTAS TEKNOLOGI INFORMASI"
                                    ,font=("Courier",18,"italic","bold","underline"))],
                           [sg.Text("UNISKA MAB BANJARMASIN"
                                    ,text_color="#FFCC00")]],
    size=(500,300),
    font=("Times", 18))
window()
window.close() 