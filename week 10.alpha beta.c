def alpha_beta_pruning(node, depth, alpha, beta, maximizing_player, values, tree):
    indent = "  " * depth
    print(f"{indent}Visiting Node {node} | Depth={depth} | Alpha={alpha} | Beta={beta} | Maximizing={maximizing_player}")

    if node not in tree or len(tree[node]) == 0:
        print(f"{indent}Leaf Node {node} → Value={values[node]}")
        return values[node]

    if maximizing_player:
        max_eval = float('-inf')
        for child in tree[node]:
            eval = alpha_beta_pruning(child, depth + 1, alpha, beta, False, values, tree)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            print(f"{indent}Node {node}: Updated Alpha={alpha}")
            if beta <= alpha:
                print(f"{indent}Pruning remaining children of Node {node} (alpha={alpha}, beta={beta})")
                break
        print(f"{indent}Returning {max_eval} from Node {node}")
        return max_eval
    else:
        min_eval = float('inf')
        for child in tree[node]:
            eval = alpha_beta_pruning(child, depth + 1, alpha, beta, True, values, tree)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            print(f"{indent}Node {node}: Updated Beta={beta}")
            if beta <= alpha:
                print(f"{indent}Pruning remaining children of Node {node} (alpha={alpha}, beta={beta})")
                break
        print(f"{indent}Returning {min_eval} from Node {node}")
        return min_eval


if __name__ == "__main__":
    tree = {
        0: [1, 2],
        1: [3, 4],
        2: [5, 6],
        3: [7, 8],
        4: [9, 10],
        5: [11, 12],
        6: [13, 14],
        7: [15, 16],
        8: [17, 18],
        9: [19, 20],
        10: [21, 22],
        11: [23, 24],
        12: [25, 26],
        13: [27, 28],
        14: [29, 30]
    }

    values = {
        15: 3, 16: 5,
        17: 6, 18: 2,
        19: 8, 20: 1,
        21: 4, 22: 9,
        23: 7, 24: -2,
        25: 0, 26: 5,
        27: 6, 28: 3,
        29: 2, 30: 10
    }

    print("\n--- Deep Alpha-Beta Traversal ---\n")
    best_value = alpha_beta_pruning(0, 0, float('-inf'), float('inf'), True, values, tree)
    print(f"\nBest value for the maximizing player: {best_value}")
