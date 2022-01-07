from tkinter.colorchooser import askcolor

import PySimpleGUI as sg
from pyvis.network import Network


class UserInterface:

    def __init__(self):
        layout_settings = [
            [sg.Multiline(size=(35, 20), key='textInput')],
            [sg.Button('Find data dependencies'), sg.Button('Choose color')]]

        sg.theme('DarkAmber')

        self.window = sg.Window(title="", layout=layout_settings, margins=(300, 150)).finalize()
        self.window.Maximize()

    def run(self):
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED:
                break
            if event == 'Choose color':
                color = askcolor(title='Choose color')[1]
            if event == 'Find data dependencies':
                return values['textInput']


def create_graph_visualization(graph):
    net = Network(notebook=True, directed=True, width='100%', height='100%')
    net.inherit_edge_colors(False)

    for root in graph.nodes:
        add_connected_component(root, net)

    net.show("dependency_graph.html")


def add_connected_component(node, net):
    net.add_node(node.number, label=(str(node.number)), color=node.color.value, shape='circle', x=10, y=10)
    if node.father is not None:
        net.add_edge(node.father.number, node.number, width=4, title=' '.join(node.instruction[:-1]))

    for child in node.children:
        add_connected_component(child, net)
