import os
import chess.pgn
import datetime

class PGNManager:
    def __init__(self):
        pass

    def save_game_to_pgn(self, move_history, result):
        game = chess.pgn.Game()
        game.headers["Event"] = "Ajedrez"
        game.headers["Site"] = "Local"
        game.headers["Date"] = str(datetime.date.today())
        game.headers["Round"] = "1"
        game.headers["White"] = "Blancas"
        game.headers["Black"] = "Negras"
        game.headers["Result"] = result

        node = game.add_variation(chess.Move.null())
        for move_str in move_history:
            move = chess.Move.from_uci(move_str)
            node = node.add_variation(move)

        pgn_directory = "pgn_games"
        os.makedirs(pgn_directory, exist_ok=True)
        pgn_file_name = os.path.join(pgn_directory, f"game_{len(os.listdir(pgn_directory)) + 1}.pgn")

        with open(pgn_file_name, "w") as pgn_file:
            pgn_file.write(str(game))

# Aquí puedes agregar más funciones o clases relacionadas con la gestión de partidas PGN si es necesario.
