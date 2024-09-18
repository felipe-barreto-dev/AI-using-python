def print_solution(board):
    """Imprime uma solução do tabuleiro de N rainhas."""
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col):
    """Verifica se é seguro colocar uma rainha na posição (linha, coluna)."""
    # Verifica se há outra rainha na mesma linha
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

def solve_nqueens(board, col):
    """Resolve o problema das N rainhas usando backtracking."""
    if col >= len(board):  # Se todas as rainhas foram colocadas
        return True

    # Tenta colocar uma rainha em cada linha da coluna atual
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 'Q'  # Coloca a rainha
            if solve_nqueens(board, col + 1):  # Move para a próxima coluna
                return True
            board[i][col] = '.'  # Se falhou, remove a rainha (backtracking)

    return False  # Se não for possível colocar a rainha, retorna False

def n_queens_solution(n):
    """Inicializa o tabuleiro e chama a função para encontrar uma solução."""
    board = [['.' for _ in range(n)] for _ in range(n)]  # Cria o tabuleiro vazio
    if solve_nqueens(board, 0):  # Inicia a solução
        print_solution(board)  # Imprime a solução encontrada
    else:
        print(f"Não há solução para {n} rainhas.")

# Define o número de rainhas
n = 8
n_queens_solution(n)
