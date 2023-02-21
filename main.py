dict = {}
humn_test = 3769668716709
humn_calls = 0

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


def evaluate(name):  # root: vpmn + pqtt
    if (name == "humn"): # humn is requested for vpmn, pqtt is always 40962717833337
        global humn_calls
        humn_calls += 1
        print(f"humn queried, humn_calls is now {humn_calls}")
        return humn_test
   
    value = dict[name]
    if (isinstance(value, Val)):
        return value.val
    else:
        return value.combine(evaluate(value.left), evaluate(value.right))

def solve_root():
    solve_with("vpmn", 40962717833337)


def solve_with(name, value_to_reach):
    print(f"> Solving {name}")
    if (name == "humn"):        
        print(f"Great success, humn should be {value_to_reach}")
        print()
    else:
        to_evaluate = dict[name]
        if (isinstance(to_evaluate, Val)):
            print("Error, no humn found")
            return
        else:
            expr_to_solve = to_evaluate
            left = expr_to_solve.left
            op = expr_to_solve.op
            right = expr_to_solve.right
            curr_humn_count = humn_calls
            evaluate(left)
            humn_left = humn_calls > curr_humn_count
            if (humn_left):
                print(">> humn on the left")
                solve_left(left, op, evaluate(right), value_to_reach)
            else:
                print(">> humn on the right")
                solve_right(evaluate(left), op, right, value_to_reach)
        
def solve_left(name, op, value_right, value_to_reach):
    match op:
        case "+":
            solve_with(name, value_to_reach - value_right)

        case "-":
            solve_with(name, value_to_reach + value_right)

        case "*":
            solve_with(name, value_to_reach / value_right)
    
        case "/":
            solve_with(name, value_to_reach * value_right)

        case _:
            print(f"Error, unknown op ({op})")

def solve_right(value_left, op, name, value_to_reach):
    match op:
        case "+":
            solve_with(name, value_to_reach - value_left)

        case "-":
            solve_with(name, value_left - value_to_reach)

        case "*":
            solve_with(name, value_to_reach / value_left)
    
        case "/":
            solve_with(name, value_to_reach * value_left)

        case _:
            print(f"Error, unknown op ({op})")


print(f"{len(dict)}")

# res = evaluate("root")
res = evaluate("pqtt") # 3769668716709

print(f"{res} compared to")
print("40962717833337")

if (res < 40962717833337):
    print("Too small")

if (res > 40962717833337):
    print("Too large")

if (res == 40962717833337):
    print("Great success!")
    print()

solve_root()
