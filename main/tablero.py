import chess
from chess_display import display

class ChessBoard:
    def __init__(self):
        self.board = chess.Board()

    def make_move(self, move):
        if move in self.board.legal_moves:
            self.board.push(move)
            return True
        return False

    def get_legal_moves(self):
        return list(self.board.legal_moves)

    def is_checkmate(self):
        return self.board.is_checkmate()

    def display_board(self):
        display(self.board)
    pass

# Ejemplo de uso
if __name__ == "__main__":
    chess_game = ChessBoard()
    chess_game.display_board()




