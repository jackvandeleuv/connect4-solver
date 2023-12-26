from Game import Game

class Agent:
    def __init__(self, player: int):
        self.game = Game()
        self.player = player


    def one_move_win(self) -> int | None:
        for col in range(len(self.game.board)):
            game_copy = self.game.copy()
            game_copy.move(col)
            if game_copy.get_winner() == self.player:
                return col
            

    def find_bottom_horizontal_threats(self) -> list:
        threats = [None for _ in range(len(self.game.tops))]
        for row in self.game.board[::-1]:
            for offset in range(4):
                window_val = len(set(row[offset : 4 + offset]) - set([0]))
                if window_val == 1:
                    for row in row[offset : 4 + offset]:
                        


                for i in range(offset, 4 + offset):
                    pass
                



    def play(self) -> int:
        one_mover = self.one_move_win()
        if one_mover is not None:
            return one_mover

    
