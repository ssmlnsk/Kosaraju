import cProfile
from main_s import GraphSCC

with cProfile.Profile() as p:
    scc = GraphSCC(901)
    c = 900

    for i in range(c):
        scc.add_edge(i, i+1)

    for i in range(c):
        scc.print_scc()

if __name__ == "__main__":
    p.print_stats()
