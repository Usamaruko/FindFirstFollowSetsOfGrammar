import re
from collections import OrderedDict

# Author: [Usamaruko]
# Description: A program to compute the FIRST and FOLLOW sets of a given grammar.

productions = OrderedDict()    # Stores grammar productions while preserving order
first_sets = {}                # Stores the FIRST set for each non-terminal
follow_sets = {}               # Stores the FOLLOW set for each non-terminal
non_terminals = []             # Stores non-terminals in the order they were read

def load_grammar(file_path):
    """Load grammar productions from a file and identify non-terminals, preserving order."""
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            left, right = line.strip().split('→')
            left, right = left.strip(), right.strip()
            if left not in non_terminals:
                non_terminals.append(left)  # Store non-terminals in order
            productions[left] = [alt.strip().split() for alt in right.split('|')]
            
            # Search and record non-terminals on the right-hand side
            for production in productions[left]:
                for symbol in production:
                    if is_non_terminal(symbol) and symbol not in non_terminals:
                        non_terminals.append(symbol)

def is_non_terminal(symbol):
    """Check if a symbol is a non-terminal: uppercase letters or containing an apostrophe."""
    return bool(re.match(r"[A-Z](')?", symbol))

def compute_first(symbol):
    """Calculate the FIRST set for a given symbol."""
    if symbol in first_sets:
        return first_sets[symbol]

    first = set()
    if symbol not in non_terminals:  # If it's a terminal
        return {symbol}  # Return the terminal set directly

    for production in productions[symbol]:
        for sym in production:
            sym_first = compute_first(sym)
            first.update(sym_first - {'Ɛ'})
            if 'Ɛ' not in sym_first:
                break
        else:
            first.add('Ɛ')

    first_sets[symbol] = first
    return first

def compute_follow(symbol):
    """Calculate the FOLLOW set for a given symbol."""
    if symbol in follow_sets:
        return follow_sets[symbol]

    follow = set()
    if symbol == non_terminals[0]:  # The FOLLOW of the start symbol contains #
        follow.add('#')

    for lhs, rhs_list in productions.items():
        for rhs in rhs_list:
            for i, sym in enumerate(rhs):
                if sym == symbol:
                    for next_sym in rhs[i + 1:]:
                        next_first = compute_first(next_sym)
                        follow.update(next_first - {'Ɛ'})
                        if 'Ɛ' not in next_first:
                            break
                    else:
                        if lhs != symbol:
                            follow.update(compute_follow(lhs))

    follow_sets[symbol] = follow
    return follow

def compute_all_firsts_and_follows():
    """Compute FIRST and FOLLOW sets for all non-terminals."""
    for non_terminal in non_terminals:  # Only compute for non-terminals
        compute_first(non_terminal)
    for non_terminal in non_terminals:  # Only compute for non-terminals
        compute_follow(non_terminal)

def main():
    file_path = "grammar.txt"  # Set the file path
    load_grammar(file_path)
    compute_all_firsts_and_follows()
    
    # Output FIRST sets
    print("FIRST Sets:")
    for non_terminal in non_terminals:
        first_set = first_sets.get(non_terminal, set())
        formatted_first_set = ", ".join(first_set) if first_set else ""
        print(f"FIRST({non_terminal}) = {{ {formatted_first_set} }}")

    # Output FOLLOW sets
    print("\nFOLLOW Sets:")
    for non_terminal in non_terminals:
        follow_set = follow_sets.get(non_terminal, set())
        formatted_follow_set = ", ".join(follow_set) if follow_set else ""
        print(f"FOLLOW({non_terminal}) = {{ {formatted_follow_set} }}")

if __name__ == "__main__":
    main()
