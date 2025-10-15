

def fol_fc_ask(KB, alpha):
    """
    FUNCTION FOL-FC-ASK(KB, α)
    Forward chaining for first-order logic (simplified version).
    """
    while True:
        new = set()
        for rule in KB:
            if isinstance(rule, tuple):  # Rule format: (premises, conclusion)
                premises, conclusion = standardize_variables(rule)

                for theta in find_substitutions(premises, KB):
                    q_prime = substitute(theta, conclusion)

                    if q_prime not in KB and q_prime not in new:
                        new.add(q_prime)

                        phi = unify(q_prime, alpha)
                        if phi is not None:
                            return phi
        if not new:
            break
        KB.extend(new)
    return False



def standardize_variables(rule):
    """Return rule as-is (simplified version)."""
    return rule


def find_substitutions(premises, KB):
    """Find substitutions θ that satisfy premises in KB."""
    # Simplified: only checks if all premises exist in KB
    matches = []
    if all(p in KB for p in premises):
        matches.append({})
    return matches


def substitute(theta, expr):
    """Apply substitution θ to expr (dummy version)."""
    return expr


def unify(x, y):
    """Unify two expressions (simple equality check)."""
    if x == y:
        return {}
    else:
        return None



if __name__ == "__main__":
    # KB contains rules and facts
    KB = [
        (["Human(x)"], "Mortal(x)"),  # Rule: Human(x) => Mortal(x)
        "Human(Socrates)"              # Fact: Human(Socrates)
    ]

    alpha = "Mortal(Socrates)"  # Query

    result = fol_fc_ask(KB, alpha)
    print("Query:", alpha)
    print("Result:", result if result else "False (Not entailed)")
