def print_solution(board):
    """Imprime uma solução do tabuleiro."""
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col):
    """Verifica se é seguro colocar uma rainha na posição (row, col)."""
    # Verifica a mesma linha à esquerda
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Verifica a diagonal superior à esquerda
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Verifica a diagonal inferior à esquerda
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_nqueens(board, col, solutions):
    """Resolve o problema das N rainhas e armazena as soluções."""
    if col == len(board):  # Se colocou todas as rainhas, armazena a solução
        solutions.append([row[:] for row in board])  # Copia o tabuleiro
        return

    # Tenta colocar uma rainha em cada linha da coluna atual
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 'Q'  # Coloca a rainha
            solve_nqueens(board, col + 1, solutions)  # Vai para a próxima coluna
            board[i][col] = '.'  # Remove a rainha (backtracking)

def n_queens_solution(n):
    """Inicializa o tabuleiro e busca as soluções."""
    board = [['.' for _ in range(n)] for _ in range(n)]  # Cria um tabuleiro vazio
    solutions = []  # Armazena as soluções
    solve_nqueens(board, 0, solutions)  # Começa a resolver

    # Exibe as soluções
    if solutions:
        for idx, solution in enumerate(solutions):
            print(f"Solução {idx + 1}:")
            print_solution(solution)
    else:
        print(f"Não há solução para {n} rainhas.")

# Define o número de rainhas
n = 8
n_queens_solution(n)
