import parsers
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
import networkx as nx
import gui
import PySimpleGUI as psg

# ping, ipconfig, pathping, route

matplotlib.use('TkAgg')

window = gui.create_window()

fig_ping, ax_ping = plt.subplots()
fig_canvas_agg_ping = FigureCanvasTkAgg(fig_ping, window['-ping_canvas-'].TKCanvas)
fig_canvas_agg_ping.get_tk_widget().pack(side='top', fill='both', expand=1)

fig_canvas_agg_pathping = FigureCanvasTkAgg(fig_ping, window['-pathping_canvas-'].TKCanvas)
fig_canvas_agg_pathping.get_tk_widget().pack(side='top', fill='both', expand=1)

ipconfig = None
pathping = None
ping = None

G = nx.Graph()
options = {
    "font_size": 7,
    'width': 1,                 # line width of edges
    'arrowstyle': '-|>',        # array style for directed graph
    'arrowsize': 18,            # size of arrow
}

while True:
    event, values = window.read()

    if event in (psg.WIN_CLOSED, 'Exit'):
        break

    if event == '-ping_begin-':
        if pathping != None:
            pos = nx.kamada_kawai_layout(G)

            plt.figure(1)
            plt.clf()
            nx.draw(G, pos, node_color='skyblue', with_labels=True, node_size=700, font_color='black', arrows=True,
                    **options)
            fig_canvas_agg_ping.draw()

            window.read(timeout=1)

        ping = parsers.PingParser(values['-ping_address-'],
                                  values['-ping_n-'],
                                  values['-ping_l-'],
                                  values['-ping_f-'],
                                  values['-ping_i-'],
                                  values['-ping_r-'],
                                  values['-ping_w-'])
        while not ping.is_done:
            ping.read()
            window['-ping_info-'].update(value=ping.info)
            window.read(timeout=1)

    if event == '-ipconfig_begin-':
        ipconfig = parsers.IpconfigParser()
        titles = []
        for adapter in ipconfig.adapters:
            titles.append(adapter[0])
        window['-ipconfig_list-'].update(values=titles)

    if event == '-ipconfig_list-':
        adapter_name = values['-ipconfig_list-'][0]
        for adapter in ipconfig.adapters:
            if adapter_name == adapter[0]:
                window['-ipconfig_info-'].update(value=adapter[1])

    if event == '-pathping_begin-':
        pathping = parsers.PathPingParser(values['-pathping_address-'])
        last_ip = False
        current_ip = pathping.get_next_ip()
        while current_ip != False:

            G.add_node(current_ip)
            if last_ip is not False:
                G.add_edge(last_ip, current_ip)

            pos = nx.kamada_kawai_layout(G)

            plt.figure(1)
            plt.clf()
            nx.draw(G, pos, node_color='skyblue', with_labels=True, node_size=700, font_color='black', arrows=True, **options)
            fig_canvas_agg_pathping.draw()

            window.read(timeout=1)

            last_ip = current_ip
            current_ip = pathping.get_next_ip()

        window.read(timeout=1)
        window['-pathping_table-'].update(values=pathping.get_stat())
        psg.popup("Готово")

window.close()
