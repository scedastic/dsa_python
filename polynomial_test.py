import pytest
from polynomial import solve_for_x

@pytest.mark.parametrize("a,b,c,x1,x2", [
    (1,3,2,-1,-2), 
    (1,0,-16,4,-4),
    (1,0,0,0,0),
    (1,0,-169,13,-13)
])
def test_solutions(a, b, c, x1, x2):
    xs = solve_for_x(a, b, c)
    assert x1 in xs and x2 in xs

@pytest.mark.parametrize("a, b, c",[
    (1, 0, 1),
    (1, 0, 50),
])
def test_imaginary(a,b,c):
    with pytest.raises(Exception):
        solve_for_x(a, b, c)