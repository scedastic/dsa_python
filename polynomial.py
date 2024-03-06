from math import sqrt
def solve_for_x(a, b, c) -> (float, float):
    """Solves equations in the form of ax**2 + bx + c = 0.

    Args:
        a (float): Coefficient for x**2
        b (float): Coefficient for x
        c (float): Constant
    Returns:
        x1 and x2
    """
    # Get the determinant to see if solution is "real"
    determinant = pow(b, 2) - 4*a*c
    if determinant < 0:
        raise Exception("Solution is imaginary")
    x1 = (-1*b + sqrt(determinant)) / 2 * a
    x2 = (-1*b - sqrt(determinant)) / 2 * a
    return (x1, x2)


if __name__ == "__main__":
    print("Polynomial for x**2 + 3x + 2")
    print(solve_for_x(1, 3, 2))
    print("Polynomial for x**2 - 16")
    print(solve_for_x(1, 0, -16))