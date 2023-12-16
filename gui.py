import PySimpleGUI as psg


def create_window():
    psg.set_options(font=("Arial Bold", 14))
    ping_table = [
        [psg.MLine(size=(100, 30), key='-ping_info-', font=("Arial Bold", 9))]
    ]
    ping_graph = [
        [psg.Canvas(key='-ping_canvas-')]
    ]
    ping = [
        [psg.Text("IP адрес"), psg.Input(key='-ping_address-')],
        [psg.Button('Начать поиск', key='-ping_begin-')],
        [psg.TabGroup([
            [psg.Tab('информация', ping_table),
             psg.Tab('граф', ping_graph)]], size=(950, 600))],
        [psg.Canvas(key='-ping_canvas-')]
    ]
    ipconfig = [
        [psg.Column([
            [psg.Button('Запуск', key='-ipconfig_begin-')],
            [psg.Listbox([], size=(50, 8), expand_y=True, enable_events=True, key='-ipconfig_list-', font=("Arial Bold", 9))]
         ], size=(400, 450)),
         psg.Column([
            [psg.MLine(size=(70, 20), key='-ipconfig_info-', font=("Arial Bold", 9))]
         ], size=(520, 450))]
    ]
    pathping_table = [
        [psg.Table(values=[['', '', '', '']],
                   headings=['прыжок', 'RTT', 'исходный', 'маршрутный', 'адрес'],
                   auto_size_columns=True,
                   display_row_numbers=False,
                   justification='center',
                   key='-pathping_table-',
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
             psg.Tab('граф', pathping_graph)]], size=(950, 600))]
    ]
    route = [

    ]

    layout = [
        [psg.TabGroup([
          [psg.Tab('ping', ping),
           psg.Tab('ipconfig', ipconfig),
           psg.Tab('pathping', pathping),
           psg.Tab('route', route)]
        ])]
    ]

    return psg.Window('Сети', layout, finalize=True, size=(1000, 700))
