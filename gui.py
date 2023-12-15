import PySimpleGUI as psg


def create_window():
    psg.set_options(font=("Arial Bold", 14))
    tab1 = [
        [psg.Text("IP адрес"), psg.Input(key='-ping_address-')],
    ]
    tab2 = [

    ]
    tab3 = [
        [psg.Text("IP адрес"), psg.Input(key='-pathping_address-')],
        [psg.Button('Начать поиск', key='-pathping_begin-')],
        [psg.Canvas(key='-pathping_canvas-')]
    ]
    tab4 = [

    ]

    layout = [[psg.TabGroup([
        [psg.Tab('ping', tab1),
         psg.Tab('ipconfig', tab2),
         psg.Tab('pathping', tab3),
         psg.Tab('route', tab4)]])],
        [psg.OK(), psg.Cancel()]
    ]

    return psg.Window('Сети', layout, finalize=True)
