def sum(a, b):
    return a + b

def diff(a, b):
    return a - b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return 0

print("Out If Structure Code")

if __name__ == "__main__":
    # Pruebas
    print(sum(4,5))
    print(diff(1,9))