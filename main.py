
dict = {}

class Expr:
    def __init__(self, left, op, right):
        self.name = name
        self.left = left
        self.op = op
        self.right = right

    def combine(self, left_val, right_val):
        if (self.op == "+"):
            return left_val + right_val
        elif (self.op == "-"):
            return left_val - right_val
        elif (self.op == "/"):
            return left_val / right_val
        else:
            return left_val * right_val

class Val:
    def __init__(self, val):
        self.name = name
        self.val = val

with open('Input.txt') as f:
    for line in f:
        parts = line.split(" ")
        name = parts[0][:-1]
        num_parts = len(parts)
        if (num_parts == 2):
            dict[name] = Val(int(parts[1]))
        elif (num_parts == 4):
            dict[name] = Expr(parts[1], parts[2], parts[3][:-1])

def evaluate(name):
  value = dict[name]
  if (isinstance(value, Val)):
      return value.val
  else:
    return value.combine(evaluate(value.left), evaluate(value.right))
      

print(f"{len(dict)}")

res = evaluate("root")
print(f"{res}")




        