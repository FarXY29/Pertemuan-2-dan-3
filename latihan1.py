import PySimpleGUI as sg
window = sg.Window(title="Latihan Pertama",layout=[

    [sg.Text("Nama    : 2210010154")],
    [sg.Text("Nama    : Muhammad Hambali Ta'simbillah")],
    [sg.Text("Kelas    : 5M Reguler Banjarmasin")],
    [sg.Text("Matkul   : Pemograman Visual 3")]
    ],
    background_color='#FF5733',
    size=(400,200))
window()
window.close()