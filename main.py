

import state_machine
from state import State
from user_interface import UserInterface, create_graph_visualization
from utility import create_graph, create_driver


def controller():

    ui = UserInterface()
    inst = ui.run()

    from utility import instruction_split
    from utility import check_instruction_validity

    filtered_inst = check_instruction_validity(instruction_split(inst))
    graph, full_node_list = create_graph(filtered_inst)
    create_graph_visualization(graph)
    create_driver()
    state = State()
    state_machine.state_machine_run(state, graph)


if __name__ == '__main__':
    controller()
