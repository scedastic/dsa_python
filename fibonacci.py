def fib(n):
    if n <=0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
fibos = [0,1]
def fib_eff(n):
    if n < 0:
        return 0
    if len(fibos) <= n:
        for i in range(len(fibos), n + 1):
            fibos.append(fibos[i-1] + fibos[i-2])
    return fibos[n]
        



if __name__ == "__main__":
    test_inputs = [0, 1, -12, 5, 6, 9]
    test_outputs = [0, 1, 0,5,8, 34]
    
    print("Recursive")
    for i in range(len(test_inputs)):
        if test_outputs[i] == fib(test_inputs[i]):
            print("Good")
        else:
            print(f"Not Good, got {fib(i)} instead of {test_outputs[i]}")

    print("Memoization")
    for i in range(len(test_inputs)):
        if test_outputs[i] == fib_eff(test_inputs[i]):
            print("Good")
        else:
            print(f"Not Good, got {fib_eff(i)} instead of {test_outputs[i]}")

    
    