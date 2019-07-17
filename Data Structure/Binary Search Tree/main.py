class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None

    def add(self, item):
        if self.head.val is None:
            self.head.val = item
        else:
            self.__add_node(self.head, item)

    def __add_node(self, cur, item):
        if cur.val >= item:
            if cur.left is not None:
                self.__add_node(cur.left, item)
            else:
                cur.left = Node(item)
        else:
            if cur.right is not None:
                self.__add_node(cur.right, item)
            else:
                cur.right = Node(item)

    def search(self, item):
        if self.head.val is None:
            return False
        else:
            return self.__search_node(self.head, item)

    def __search_node(self, cur, item):
        if self.head.var == item:
            return True
        else:
            if cur.val >= item:
                if cur.left is not None:
                    return self.__search_node(cur.left, item)
                else:
                    return False
            else:
                if cur.right is not None:
                    return self.__search_node(cur.right, item)
                else:
                    return False

    def remove(self, item):
        if self.head.val is None:
            print('there is no item')
        if self.head.val == item:
            if self.head.left is None and self.head.right is None:
                self.head = None
            elif self.head.left is None and self.head.right is not None:
                self.head = self.head.right
            elif self.head.left is not None and self.head.right is None:
                self.head = self.head.left
            else:
                self.head.val = self.__most_left_val_from_right_node(self.head.right).val
                self.__removeitem(self.head, self.head.right, self.head.val)
        else:
            if self.head.val > item:
                self.__remove(self.haed, self.head.left, item)
            else:
                self.__remove(self.head, self.head.right, item)

    def __remove(self, parent, cur, item):
        if cur is None:
            print("There is no item:", item)
        if cur.val == item
            if cur.left is None and cur.right is None:
                if parent.left == cur:
                    parent.left = None
                else:
                    parent.right = None
            elif cur.left is None and cur.right is not None:
                if parent.left == cur:
                    parent.left = cur.left
                else:
                    parent.right = cur.left
            else:
                cur.val = self.__most_left_val_from_right_node(cur.right).val
                self.__removeitem(cur, cur.right, cur.val)

    def __most_left_val_from_right_node(self, cur):
        if cur.left is None:
            return cur
        else:
            return self.__most_left_val_from_right_node(cur.left)

    def __removeitem(self, parent, cur, item):
        if cur.val == item:
            if parent.left == item:
                parent.left = None
            else:
                parent.right = None
        else:
            if cur.val > item:
                self.__removeitem(cur, cur.left, item)
            else:
                self.__removeitem(cur, cur.right, item)

    def preorder_traverse(self):
        if self.head is not None:
            self.__preorder(self.head)

    def __preorder(self, cur):
        self.preorder_list.append(cur.val)
        print(cur.val)
        if cur.left is not None:
            self.__preorder(cur.left)
        if cur.right is not None:
            self.__preorder(cur.right)

    def inorder_traverse(self):
        if self.head is not None:
            self.__inorder(self.head)

    def __inorder(self, cur):
        if cur.left is not None:
            self.__inorder(cur.left)

        self.inorder_list.append(cur.val)
        print(cur.val)

        if cur.right is not None:
            self.__inorder(cur.right)

    def postorder_travers(self):
        if self.head is not None:
            self.__postorder(self.head)

    def __postorder(self, cur):
        if cur.left is not None:
            self.__postorder(cur.left)

        if cur.right is not None:
            self.__postorder(cur.right)

        self.postorder_list.append(cur.val)
        print(cur.val)