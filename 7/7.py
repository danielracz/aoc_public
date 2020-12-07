import networkx as nx
import networkx.algorithms as nxa

INPUT_FILE = "7.in"

with open(INPUT_FILE, 'r') as f:
    inp = f.read().splitlines()

G = nx.DiGraph()

# input parse ugly af, see reddit for better ways to do it
for line in inp:
    bid = "".join(line.strip().split()[:2])
    if bid not in G.nodes:
        G.add_node(bid)
    l = line.strip().split("bags contain")
    if len(l) > 1:
        for each in l[1:][0].split(","):
            if each.endswith("."):
                each = each[:-1]
            if each.split()[0] == "1":
                nid = "".join(each.split("bag")[0].split()[1:])
                if nid not in G.nodes:
                    G.add_node(nid)
                G.add_edge(nid, bid, weight = 1)
            elif each.split()[0] != "no":
                nid = "".join(each.split("bags")[0].split()[1:])
                if nid not in G.nodes:
                    G.add_node(nid)
                G.add_edge(nid, bid, weight = int(each.split()[0]))

# part1:
print(len(nxa.dfs_tree(G, "shinygold").nodes) - 1)

H = G.reverse()
def get_sum(H, node):
    if H.out_degree(node) == 0:
        return 1

    return sum(G[n][node]['weight'] * get_sum(H, n) for n in H.neighbors(node)) + 1

# part2
print(get_sum(H, "shinygold") - 1)
