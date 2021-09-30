def path_connecting(all_paths_of, a_node, b_node, n_nodes):
    if a_node == b_node:
        return [a_node]
    all_paths_of_tr = all_paths_of
    # all_paths_of_tr = self.all_paths_rot(n_nodes)
    for pth in all_paths_of_tr.values():
        if a_node in pth and b_node in pth:
            index_a = pth.index(a_node)
            index_b = pth.index(b_node)
            start = min(index_a, index_b)
            end = max(index_a, index_b)
            return pth[start: end + 1]


class Tree:
    def __init__(self, value, d=0):
        self.value = value
        self.children: list[Tree] = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def find_node(self, node):
        if self is None:
            return None
        elif self.value == node.value:
            return self
        else:
            for child in self.children:
                found_subtree = child.find_node(node)
                if found_subtree is not None:
                    return found_subtree
            return None

    def to_string(self):
        s = ""
        if self is not None:
            s += "Node " + str(self.value)
            s += " - has children:"
            for child in self.children:
                if child is not None:
                    s += " " + str(child.value)
            s += "\n"
            for child in self.children:
                s += child.to_string()
        return s

    def paths(self):
        if not self.children:
            return [[self.value]]  # one path: only contains self.value
        my_paths = []
        for child in self.children:
            for some_path in child.paths():
                my_paths.append([self.value] + some_path)
        return my_paths

    def all_paths_rot(self, all_nodes_list, n_nodes):
        all_paths = {}
        list_of_paths = self.paths()
        for i in range(1, n_nodes):
            list_of_paths += self.set_new_root(all_nodes_list[i]).paths()
            for path in list_of_paths:
                elements = "".join([str(elem) for elem in sorted(path)])
                if elements not in all_paths.keys():
                    all_paths[elements] = path
        return all_paths

    def parent(self, node):
        if self is None or self.value == node.value:
            return None
        par = None
        for child in self.children:
            if child is None:
                continue
            elif node.value == child.value:
                par = self
                break
        if par is not None:
            return par
        else:
            for child in self.children:
                par = child.parent(node)
                if par is not None:
                    return par
            return None

    def make_child_parent(self, node):
        parent = self.parent(node)
        if parent is not None:
            self.make_child_parent(parent)
            node.add_child(parent)
            parent.remove_child(node)
        return node

    def set_new_root(self, new_root):
        if self.value != new_root.value:
            return self.make_child_parent(new_root)
        return self


n, q = map(int, input().split())
u, v = map(int, input().split())
all_nodes = []
all_nodes_int = set()
my_tree = Tree(u)
new_node = Tree(v)
all_nodes.append(my_tree)
all_nodes_int.add(u)
my_tree.add_child(new_node)
all_nodes.append(new_node)
all_nodes_int.add(v)

for nd in range(n - 2):
    u, v = map(int, input().split())
    u_tree = Tree(u)
    v_tree = Tree(v)
    insert_here: Tree = my_tree.find_node(u_tree)
    if insert_here is not None:
        insert_here.add_child(v_tree)
        all_nodes.append(v_tree)
        all_nodes_int.add(v)
    else:
        insert_here = my_tree.find_node(v_tree)
        insert_here.add_child(u_tree)
        all_nodes.append(u_tree)
        all_nodes_int.add(u)

print(my_tree.to_string())
all_paths_of_tree = my_tree.all_paths_rot(all_nodes, n)

for node_ele in all_nodes_int:
    all_paths_of_tree[str(node_ele)] = [node_ele]
print(all_paths_of_tree.values())

queries = []
for query in range(q):
    a, b = map(int, input().split())
    queries.append([a, b])
    temp_all_paths = all_paths_of_tree.copy()
    connection = path_connecting(temp_all_paths, a, b, n)
    for el_key, el_value in all_paths_of_tree.items():
        for conn in connection:
            if conn in el_value:
                index_of_conn = el_value.index(conn)
                el1 = el_value[0: index_of_conn]
                if el_key in temp_all_paths.keys():
                    temp_all_paths.pop(el_key)
                elmnts1 = "".join([str(elem) for elem in sorted(el1)])
                if len(el1) != 0 and elmnts1 not in temp_all_paths.keys():
                    temp_all_paths[elmnts1] = el1

                if index_of_conn < len(el_value) - 1:
                    el2 = el_value[index_of_conn + 1:]
                    elmnts2 = "".join([str(elem) for elem in sorted(el2)])
                    if len(el2) != 0 and elmnts2 not in temp_all_paths.keys():
                        temp_all_paths[elmnts2] = el2
    new_temp_all_paths = temp_all_paths.copy()
    for el_key, el_value in temp_all_paths.items():
        for conn in connection:
            if conn in el_value:
                index_of_conn = el_value.index(conn)
                el1 = el_value[0: index_of_conn]
                if el_key in new_temp_all_paths.keys():
                    new_temp_all_paths.pop(el_key)
                elmnts1 = "".join([str(elem) for elem in sorted(el1)])
                if len(el1) != 0 and elmnts1 not in new_temp_all_paths.keys():
                    new_temp_all_paths[elmnts1] = el1

                if index_of_conn < len(el_value) - 1:
                    el2 = el_value[index_of_conn + 1:]
                    elmnts2 = "".join([str(elem) for elem in sorted(el2)])
                    if len(el2) != 0 and elmnts2 not in new_temp_all_paths.keys():
                        new_temp_all_paths[elmnts2] = el2

    lengths = {}
    for arr in new_temp_all_paths:
        if len(arr) not in lengths.keys():
            lengths[len(arr)] = 1
        else:
            lengths[len(arr)] += 1
    print(lengths)
    print(new_temp_all_paths)