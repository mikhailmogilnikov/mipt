class Node:
    """Класс для представления узла дерева"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_expression_tree(expression):
    """Функция для построения дерева выражений из строки"""
    def is_operator(c):
        return c in "+-*/^"

    def precedence(op):
        """Возвращает приоритет оператора"""
        if op in "+-":
            return 1
        if op in "*/":
            return 2
        if op == "^":
            return 3
        return 0

    def construct_tree(tokens):
        stack = []
        operators = []

        for token in tokens:
            if token.isalnum():
                stack.append(Node(token))
            elif is_operator(token):
                while (operators and precedence(operators[-1]) >= precedence(token)):
                    op = operators.pop()
                    right = stack.pop()
                    left = stack.pop()
                    op_node = Node(op)
                    op_node.left = left
                    op_node.right = right
                    stack.append(op_node)
                operators.append(token)
            elif token == "(":
                operators.append(token)
            elif token == ")":
                while operators and operators[-1] != "(":
                    op = operators.pop()
                    right = stack.pop()
                    left = stack.pop()
                    op_node = Node(op)
                    op_node.left = left
                    op_node.right = right
                    stack.append(op_node)
                operators.pop()

        while operators:
            op = operators.pop()
            right = stack.pop()
            left = stack.pop()
            op_node = Node(op)
            op_node.left = left
            op_node.right = right
            stack.append(op_node)

        return stack[0]

    tokens = []
    i = 0
    while i < len(expression):
        if expression[i].isalnum():
            tokens.append(expression[i])
        elif expression[i] in "+-*/^()":
            tokens.append(expression[i])
        i += 1

    return construct_tree(tokens)

def postorder_traversal(root):
    """Обратный обход дерева (постфиксная запись)"""
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=" ")

expression = "(a+b)*(c*(d+e+f))+g*(i+j^2)"
root = build_expression_tree(expression)

print("Обратный обход дерева:")
postorder_traversal(root)
