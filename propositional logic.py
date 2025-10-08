def PL_True(KB, model):
    
    Evaluate if KB is true in the given model
    For simplicity, we'll assume KB and alpha are represented as strings
    and we'll use eval to evaluate them in the model context
    
    try:
    
        context = {}
        for prop, value in model.items():
            context[prop] = value
      
        return eval(KB, context)
    except:
        return False

def TT_Entails(KB, alpha):
    
    Main function to check if KB entails alpha
    

    symbols = extract_symbols(KB + alpha)
    return TT_Check_All(KB, alpha, symbols, {})

def TT_Check_All(KB, alpha, symbols, model):

    Recursive function to check all possible models
 
    if not symbols:
    
        if PL_True(KB, model):
            return PL_True(alpha, model)
        else:
            return True  # When KB is false, entailment holds vacuously
    else:
 
        P = symbols[0]
        rest = symbols[1:]
       
        return (TT_Check_All(KB, alpha, rest, {**model, P: True}) and
                TT_Check_All(KB, alpha, rest, {**model, P: False}))

def extract_symbols(expression):
    """
    Extract unique propositional symbols from expression
    For simplicity, assuming single-letter symbols
    """
    symbols = set()
    for char in expression:
        if char.isalpha() and char.isupper():
            symbols.add(char)
    return sorted(list(symbols))

def generate_truth_table(KB, alpha):
    """
    Generate complete truth table for visualization
    """
    symbols = extract_symbols(KB + alpha)
    truth_table = []
   

    from itertools import product
    for values in product([True, False], repeat=len(symbols)):
        model = dict(zip(symbols, values))
        kb_true = PL_True(KB, model)
        alpha_true = PL_True(alpha, model)
        entailment_holds = not kb_true or alpha_true  # KB → alpha
       
        truth_table.append({
            'model': model.copy(),
            'KB': kb_true,
            'alpha': alpha_true,
            'entailment': entailment_holds
        })
   
    return truth_table

def print_truth_table(truth_table, KB, alpha):
    """
    Print formatted truth table
    """
    if not truth_table:
        return
   

    symbols = list(truth_table[0]['model'].keys())
  
    header = " | ".join(symbols + ["KB", "α", "KB ⊨ α"])
    print(header)
    print("-" * len(header))

    for row in truth_table:
        model_vals = [str(row['model'][s]) for s in symbols]
        kb_val = "T" if row['KB'] else "F"
        alpha_val = "T" if row['alpha'] else "F"
        entail_val = "T" if row['entailment'] else "F"
       
        row_str = " | ".join(model_vals + [kb_val, alpha_val, entail_val])
        print(row_str)


print("=== EXAMPLE 1: P ∧ Q ⊨ P ===")
KB1 = "P and Q"
alpha1 = "P"
result1 = TT_Entails(KB1, alpha1)
truth_table1 = generate_truth_table(KB1, alpha1)
print_truth_table(truth_table1, KB1, alpha1)
print(f"\nResult: {KB1} ⊨ {alpha1} is {result1}")

print("\n" + "="*50 + "\n")

print("=== EXAMPLE 2: (P → Q) ∧ P ⊨ Q ===")
KB2 = "(not P or Q) and P"  # P → Q is equivalent to ¬P ∨ Q
alpha2 = "Q"
result2 = TT_Entails(KB2, alpha2)
truth_table2 = generate_truth_table(KB2, alpha2)
print_truth_table(truth_table2, KB2, alpha2)
print(f"\nResult: {KB2} ⊨ {alpha2} is {result2}")

print("\n" + "="*50 + "\n")

print("=== EXAMPLE 3: P ⊨ Q (should fail) ===")
KB3 = "P"
alpha3 = "Q"
result3 = TT_Entails(KB3, alpha3)
truth_table3 = generate_truth_table(KB3, alpha3)
print_truth_table(truth_table3, KB3, alpha3)
print(f"\nResult: {KB3} ⊨ {alpha3} is {result3}")
