from collections import deque


def check_relation(net, first, second):
    names_graph = {}
    list_names = []
    for pair in net:
        list_names.extend([single for single in pair if single not in list_names])
    for name in list_names:
        names_graph[name] = []
        for pair in net:
            if name in pair:
                names_graph[name].append(pair[0] if pair[0] != name else pair[1])
    checked = [first, ]
    first_queue = deque()
    second_queue = deque()
    if first in names_graph[second]:
        return True
    checked.append(second)
    first_queue += names_graph[first]
    second_queue += names_graph[second]
    while first_queue:
        checking_name = first_queue.popleft()
        if checking_name in second_queue:
            return True
        else:
            checked.append(checking_name)
            for name in names_graph[checking_name]:
                if name not in checked and name not in first_queue:
                    first_queue.append(name)
    return False


if __name__ == '__main__':
    net = (
        ("Ваня", "Леша"), ("Леша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Леша", "Лена"), ("Оля", "Петя"),
        ("Степа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша")
    )

    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Леша", "Настя") is False
    assert check_relation(net, "Степа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True