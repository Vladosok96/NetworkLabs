import PySimpleGUI as psg


def create_window():
    psg.set_options(font=("Arial Bold", 14))
    ping = [
        [psg.Text("IP адрес"), psg.Input(key='-ping_address-')],
    ]
    ipconfig = [

    ]
    pathping_table = [
        [psg.Table(values=[['', '', '', '']],
                   headings=['прыжок', 'RTT', 'исходный', 'маршрутный', 'адрес'],
                   auto_size_columns=True,
                   display_row_numbers=False,
                   justification='center', key='-pathping_table-',
                   selected_row_colors='red on yellow',
                   enable_events=True,
                   expand_x=True,
                   expand_y=True,
                   enable_click_events=True)]
    ]
    pathping_graph = [
        [psg.Canvas(key='-pathping_canvas-')]
    ]
    pathping = [
        [psg.Text("IP адрес"), psg.Input(key='-pathping_address-')],
        [psg.Button('Начать поиск', key='-pathping_begin-')],
        [psg.TabGroup([
            [psg.Tab('таблица', pathping_table),
             psg.Tab('граф', pathping_graph)]], size=(950, 600))],
        [psg.Canvas(key='-pathping_canvas-')]
    ]
    route = [

    ]

    layout = [[psg.TabGroup([
        [psg.Tab('ping', ping),
         psg.Tab('ipconfig', ipconfig),
         psg.Tab('pathping', pathping),
         psg.Tab('route', route)]])],
        [psg.OK(), psg.Cancel()]
    ]

    return psg.Window('Сети', layout, finalize=True, size=(1000, 700))
