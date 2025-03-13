def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    # tc O(n), sc O(n).
    if not node:
        return None
    
    def dfs_clone(node, node_copy):
        for neigh in node.neighbors:
            if neigh not in node_copy_mapping:
                neigh_copy = Node(neigh.val)
                node_copy_mapping[neigh] = neigh_copy
                dfs_clone(neigh, neigh_copy)
            node_copy.neighbors.append(node_copy_mapping[neigh])

    node_copy_mapping = {}
    node_copy = Node(node.val)
    node_copy_mapping[node] = node_copy
    dfs_clone(node, node_copy)
    return node_copy