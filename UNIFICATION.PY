def unify(x, y, theta=None):
    if theta is None:
        theta = {}
    if x == y:
        return theta
    elif is_variable(x):
        return unify_var(x, y, theta)
    elif is_variable(y):
        return unify_var(y, x, theta)
    if isinstance(x, list) and isinstance(y, list):
        if x[0] != y[0]:
            return "Failure"
        if len(x) != len(y):
            return "Failure"
        return unify(x[1:], y[1:], theta)
    if isinstance(x, tuple) and isinstance(y, tuple):
        if len(x) != len(y):
            return "Failure"
        for xi, yi in zip(x, y):
            theta = unify(xi, yi, theta)
            if theta == "Failure":
                return "Failure"
        return theta
    return "Failure"

def unify_var(var, x, theta):
    if var in theta:
        return unify(theta[var], x, theta)
    elif x in theta:
        return unify(var, theta[x], theta)
    elif occurs_check(var, x, theta):
        return "Failure"
    else:
        theta[var] = x
        return theta

def is_variable(term):
    return isinstance(term, str) and term[0].islower()

def occurs_check(var, x, theta):
    if var == x:
        return True
    elif isinstance(x, list):
        return any(occurs_check(var, xi, theta) for xi in x)
    elif isinstance(x, tuple):
        return any(occurs_check(var, xi, theta) for xi in x)
    elif x in theta:
        return occurs_check(var, theta[x], theta)
    return False

if __name__ == "__main__":
    print("Unify(P(x), P(a)) →", unify(["P", "x"], ["P", "a"]))
    print("Unify(Q(x, b), Q(a, y)) →", unify(["Q", "x", "b"], ["Q", "a", "y"]))
    print("Unify(Loves(x, John), Loves(Mary, y)) →", unify(["Loves", "x", "John"], ["Loves", "Mary", "y"]))
    print("Unify(P(x), Q(x)) →", unify(["P", "x"], ["Q", "x"]))
