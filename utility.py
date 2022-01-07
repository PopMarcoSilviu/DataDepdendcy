from selenium import webdriver

from data import Node, LimitedQueue, Graph

supported_instructions = ['add', 'sub', 'xor', 'and', 'or', 'addi', 'sw', 'lw', 'j', 'bne']
supported_registers_dict = \
    {
        'R': 16,
    }
nb_of_instruction_dependency = \
    {
        'add': 2,
        'sub': 2,
        'xor': 2,
        'and': 2,
        'or': 2,
        'addi': 2,
        'bne': 2,
        'lw': 2,
        'sw': 2,
        'j': 2,
    }

r_instruction = ['add', 'sub', 'xor', 'and', 'or']


def instruction_split(instruction_list):
    lines = instruction_list.split('\n')
    lines_ranked = [x + ' ' + str(i) for i, x in enumerate(lines)]
    import re

    parts = map(lambda x: re.split('[ ,]', x), lines_ranked)
    return list(parts)


def check_instruction_validity(instruction_list):
    # print(instruction_list)
    filtered_by_instruction = list(filter(lambda x: (x[0].lower() in supported_instructions), instruction_list))
    return filtered_by_instruction


driver = None


def create_driver():
    global driver
    driver = webdriver.Firefox()
    driver.get('http://localhost:63342/pythonProject/dependency_graph.html')


def refresh_page():
    global driver
    if isinstance(driver, webdriver.Firefox):
        driver.refresh()


def create_graph(instruction_split_list):
    queue = LimitedQueue(4)
    node_list = []
    full_node_list = []

    for index, inst in enumerate(instruction_split_list):
        print(inst)
        current_node = Node(int(inst[4]), inst)
        full_node_list.append(current_node)

        for i in reversed(range(0, queue.get_size())):

            if nb_of_instruction_dependency[inst[0]] >= queue.get_size() - i:
                source_register_list = [inst[2]]
                if inst[0] in r_instruction:
                    source_register_list.append(inst[3])

                if queue[i].instruction[1] in source_register_list:
                    current_node.add_father(queue[i])
                    current_node.change_color()
                    queue[i].add_child(current_node)
                    break

        if current_node.father is None:
            node_list.append(current_node)

        queue.enqueue(current_node)

    return Graph(node_list), full_node_list
