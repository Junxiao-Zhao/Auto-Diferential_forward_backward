import sympy

x = sympy.symbols('x')
fx = list()

#Create a tree node
class Node:

    def __init__(self, val = None, df = None, l_node = None, r_node = None):
        self.value = val
        self.df = df
        self.left = l_node
        self.right = r_node

    def get_val(self):
        return self.value
    
    def get_df(self):
        return self.df
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def set_val(self, val):
        self.value = val
    
    def set_df(self, val):
        self.df = val
    
    def set_left(self, node):
        self.left = node
    
    def set_right(self, node):
        self.right = node

    def is_leaf(self):
        return (self.left == None and self.right == None)

#compute the ln+1 through recursion
def l_func(n):
    if n == 1:
        return x
    else:
        return 4 * l_func(n - 1) * (1 - l_func(n - 1))

#Create the tree
def create_tree(n):
    root = Node()
    current = root
    for i in range(n):
        left_n = Node()
        right_n = Node()
        current.set_left(left_n)
        current.set_right(right_n)
        current = current.get_left()
    return root

#Insert the value's of each u
def insert_value(node):
    if node.is_leaf():
        node.set_val(fx[0])
        fx.pop(0)
    else:
        insert_value(node.get_left())
        insert_value(node.get_right())
        node.set_val(node.get_left().get_val() * node.get_right().get_val())

#Compute the derivative of each u
def compute_df(node, n, x_value):
    for i in range(n):
        left_node = node.get_left()
        right_node = node.get_right()
        left_node.set_df(node.get_df() * right_node.get_val().evalf(subs={x: x_value}))
        right_node.set_df(node.get_df() * left_node.get_val().evalf(subs={x: x_value}))
        node = node.get_left()

#backward Auto Differential
def backward(node, val, x_value):
    if node.is_leaf():
        val.append(node.get_df() * sympy.diff(node.get_val()).evalf(subs={x: x_value}))
    else:
        backward(node.get_left(), val, x_value)
        backward(node.get_right(), val, x_value)

def main():
    n = int(input("How many times do you want to get the funtion for Auto Differential? "))
    x = int(input("What's the value of x? "))
    #factor ln+1
    temp = sympy.factor_list(l_func(n))
    for i in range(len(temp[1])):
        fx.append(temp[1][i][0] ** temp[1][i][1])
    fx[0] = fx[0] * temp[0]
    
    n = len(fx)
    root = create_tree(n - 1)
    insert_value(root)
    root.set_df(1)
    compute_df(root, n - 1, x)
    values = list()
    backward(root, values, x)
    print("The result of Auto Differential (backward) of the function is", sum(values))

main()