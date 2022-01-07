import time

from user_interface import create_graph_visualization


def state_machine_run(state, graph):
    # time.sleep(5)
    full_node_list = graph.get_node_list()
    while True:

        if full_node_list:
            state.add_instruction(full_node_list[0])
            full_node_list.pop(0)

        state.increase_time()
        state.inst_update(graph)

        create_graph_visualization(graph)

        time.sleep(2)

        if not state.working():
            break
