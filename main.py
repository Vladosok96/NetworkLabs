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

fig, ax = plt.subplots()
fig_canvas_agg = FigureCanvasTkAgg(fig, window['-pathping_canvas-'].TKCanvas)
fig_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)

G = nx.Graph()
options = {
    "font_size": 7,
    'width': 1,                 # line width of edges
    'arrowstyle': '-|>',        # array style for directed graph
    'arrowsize': 18,            # size of arrow
}

while True:
    event, values = window.read()
    print(event, values)
    if event in (psg.WIN_CLOSED, 'Exit'):
        break
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
            nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue',
                    font_color='black', arrows=True, **options)
            fig_canvas_agg.draw()

            window.read(timeout=1)

            last_ip = current_ip
            current_ip = pathping.get_next_ip()

        window.read(timeout=1)
        window['-pathping_table-'].update(values=pathping.get_stat())

window.close()