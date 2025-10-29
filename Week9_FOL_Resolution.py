from copy import deepcopy


def is_variable(x):
    return isinstance(x, str) and x[0].islower()

def unify(x, y, subs=None):
    if subs is None:
        subs = {}
    if x == y:
        return subs
    elif is_variable(x):
        return unify_var(x, y, subs)
    elif is_variable(y):
        return unify_var(y, x, subs)
    elif isinstance(x, tuple) and isinstance(y, tuple) and x[0] == y[0] and len(x[1]) == len(y[1]):
        for a, b in zip(x[1], y[1]):
            subs = unify(apply_subs(a, subs), apply_subs(b, subs), subs)
            if subs is None:
                return None
        return subs
    else:
        return None

def unify_var(var, x, subs):
    if var in subs:
        return unify(subs[var], x, subs)
    elif is_variable(x) and x in subs:
        return unify(var, subs[x], subs)
    elif occurs_check(var, x, subs):
        return None
    elif var != x:  
        subs[var] = x
    return subs

def occurs_check(var, x, subs):
    if var == x:
        return True
    elif isinstance(x, tuple):
        return any(occurs_check(var, arg, subs) for arg in x[1])
    elif is_variable(x) and x in subs:
        return occurs_check(var, subs[x], subs)
    return False

def apply_subs(x, subs):
    
    if is_variable(x):
        val = subs.get(x, x)
        if val == x: 
            return x
        return apply_subs(val, subs)
    elif isinstance(x, tuple):
        return (x[0], [apply_subs(a, subs) for a in x[1]])
    else:
        return x

def make_hashable(clause):
    """Convert clause into hashable form for sets."""
    result = []
    for pred in clause:
        if isinstance(pred, tuple) and isinstance(pred[1], list):
            result.append((pred[0], tuple(pred[1])))
        else:
            result.append(pred)
    return tuple(result)

def resolve(ci, cj):
    new_clauses = []
    for li in ci:
        for lj in cj:
            if li[1] != lj[1] and li[0][0] == lj[0][0]:
                subs = unify(li[0], lj[0])
                if subs is not None:
                    new_ci = [apply_subs(x[0], subs) for x in ci if x != li]
                    new_cj = [apply_subs(x[0], subs) for x in cj if x != lj]
                    new_clause = new_ci + new_cj
                    new_clause = [(p[0], tuple(p[1])) if isinstance(p[1], list) else p for p in new_clause]
                    if new_clause == []:
                        return [[]]
                    new_clauses.append(new_clause)
    return new_clauses

def fol_resolution(kb, query):
    clauses = deepcopy(kb)
    clauses.append([(query, False)]) 

    new = set()
    print("Knowledge Base:")
    for c in kb:
        print("  ", c)
    print("\nQuery:", query)
    print("\n--- Starting Resolution ---")

    while True:
        n = len(clauses)
        pairs = [(clauses[i], clauses[j]) for i in range(n) for j in range(i + 1, n)]
        for (ci, cj) in pairs:
            resolvents = resolve(ci, cj)
            for res in resolvents:
                if res == []:
                    print("\n❌ Contradiction found — query is entailed.")
                    return True
                new.add(make_hashable(res))
        new_clauses = [list(x) for x in new if list(x) not in clauses]
        if not new_clauses:
            print("\n⚠️ No contradiction — query not entailed.")
            return False
        clauses.extend(new_clauses)



kb = [
    [(('P', ['x']), False), (('Q', ['x']), True)],  # ¬P(x) ∨ Q(x)
    [(('P', ['A']), True)]                          # P(A)
]

query = ('Q', ['A'])

if __name__ == "__main__":
    fol_resolution(kb, query)
