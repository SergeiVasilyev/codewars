def loop_size(node):
    n = node
    i = 0
    while True:
        n.data = i
        # print(n.data)
        if hasattr(n.next, 'data'):
            return n.data - n.next.data + 1
        n = n.next
        i += 1


if __name__=='__main__':
    # Create Node
    class Node:
        def __init__(self, next=None):
            self.next = next

    # First chain
    node1 = Node()
    node2 = Node()
    node3 = Node()
    node4 = Node()
    node5 = Node()
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node2
    print('Chain 1 =', loop_size(node1), '\n Expected Result = 4')

    # Second chain
    # Make a longer chain with a loop of 29
    nodes = [Node() for _ in range(50)]
    for node, next_node in zip(nodes, nodes[1:]):
        node.next = next_node
    nodes[49].next = nodes[21]
    print('CHain 2 =', loop_size(nodes[0]), '\n Expected Result = 29')
