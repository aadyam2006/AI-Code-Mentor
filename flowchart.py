from graphviz import Digraph

def generate_flowchart(code):

    flow = Digraph()

    flow.node("Start")

    lines = code.split("\n")

    prev = "Start"
    step_count = 0

    for line in lines:

        line = line.strip()

        if line == "":
            continue   # skip empty lines

        step = f"step{step_count}"

        flow.node(step, line)

        flow.edge(prev, step)

        prev = step
        step_count += 1

    flow.node("End")
    flow.edge(prev, "End")

    return flow