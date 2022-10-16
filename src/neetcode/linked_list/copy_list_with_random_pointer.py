# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        node = head
        new_head: Node | None = None
        new_node: Node | None = None
        new_node_by_old_node: dict[Node, Node] = {}

        # Todo need to keep a ref dict so i can link the randoms next
        while node is not None:
            # check if node exists in new dict, if it does, reference it, else create a new one and add it to the dict
            if node in new_node_by_old_node:
                new_next = new_node_by_old_node[node]
            else:
                new_next = Node(x=node.val)
                new_node_by_old_node[node] = new_next

            if new_head is None:
                new_head = new_next
                new_node = new_head

            # extend next node
            new_node.next = new_next
            # extend new list by new node
            new_node = new_next

            # check if random exists, if it does check for its existence, otherwise, create
            rand = node.random
            if rand is not None:
                if rand in new_node_by_old_node:
                    new_node.random = new_node_by_old_node[rand]
                else:
                    new_node.random = Node(x=rand.val)
                    new_node_by_old_node[rand] = new_node.random

            node = node.next

        return new_head


if __name__ == "__main__":
    s = Solution()
    input = Node(x=-1)

    output = s.copyRandomList(input)

    print(output)