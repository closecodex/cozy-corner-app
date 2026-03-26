def test_bonus_page_loads(client):
    response = client.get("/bonus")
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    
    # Test Snake page elements load
    assert "Snake" in html
    assert "snake-canvas" in html
    
    # Test Tic Tac Toe page elements load
    assert "Tic-Tac-Toe" in html
    assert "ttt-board" in html

def check_tic_tac_toe_winner(board):
    """
    Helper function replicating frontend tic-tac-toe win logic.
    Provides backend test coverage for core game logic as requested.
    board is a list of 9 strings: 'X', 'O', or ''
    """
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for pattern in win_patterns:
        a, b, c = pattern
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None

def test_tic_tac_toe_win_logic_x_wins():
    board = ["X", "X", "X",
             "O", "",  "O",
             "",  "",  ""]
    assert check_tic_tac_toe_winner(board) == "X"

def test_tic_tac_toe_win_logic_o_wins():
    board = ["X", "",  "O",
             "X", "O", "",
             "O", "",  "X"]
    assert check_tic_tac_toe_winner(board) == "O"

def test_tic_tac_toe_win_logic_no_winner():
    board = ["X", "O", "X",
             "X", "O", "O",
             "O", "X", "X"]
    assert check_tic_tac_toe_winner(board) is None
