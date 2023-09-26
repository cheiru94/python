# legacy system
def AndGate(x1, x2):
    if x1 == 1 and x2 == 1:
        return 1
    else:
        return 0


def OrGate(x1, x2):
    if x1 == 0 and x2 == 0:
        return 0
    else:
        return 1

# Perceptron - ML


def perceptron(x1, x2):
    w1 = 0.5
    w2 = 0.5
    bias = -0.5
    result = x1 * w1 + x2 * w2 + bias       # Perceptron 부분
    return 1 if result > 0 else 0           # Activation Function 부분


print(AndGate(0, 0))
print(AndGate(0, 1))
print(AndGate(1, 0))
print(AndGate(1, 1))
print()
print(perceptron(0, 0))
print(perceptron(0, 1))
print(perceptron(1, 0))
print(perceptron(1, 1))
