class Game:
    def __init__(self):
        ROWS = 6
        COLS = 7
        self.board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        self.to_move = 1  # 1 or 2
        self.tops = [-1 for _ in range(COLS)]
        self.winner = None
        self.turn = 0


    def copy(self):
        game_copy = Game()

        game_copy.board = self.board
        game_copy.to_move = self.to_move
        game_copy.tops = self.tops
        game_copy.winner = self.winner

        return game_copy

    
    def __str__(self) -> str:
        strings = []
        for row in self.board[::-1]:
            row = [str(x) for x in row]
            strings.append('|'.join(row))
        return '\n'.join(strings)
    

    def __is_legal(self, col: int) -> bool:
        """
        Returns bool indicating if move was legal.
        """
        # print('1:', type(col) == int) 
        # print('2:', col <= len(self.__board[0]))
        # print('3:', col >= 0)
        # print('4:', self.__winner is None)
        # print('5:', self.__tops[col] < len(self.__board))
        # print('6:', self.__board[self.__tops[col] + 1][col] == 0)
        
        return (
            type(col) == int and 
            col <= len(self.board[0]) and 
            col >= 0 and
            self.winner is None and
            self.tops[col] < len(self.board) and
            self.board[self.tops[col] + 1][col] == 0
        )
        

    def __vertical_winner(self) -> int | None:
        for col in range(len(self.board[0])):
            start = 0
            while start + 3 < len(self.board):
                maybe_winner = self.board[start][col]
                if maybe_winner == 0:
                    start += 1
                    continue
                for x in range(1, 4):
                    if self.board[start + x][col] != maybe_winner:
                        break
                if x == 3 and self.board[start + x][col] == maybe_winner:
                    return maybe_winner
                start += 1
                

    def __horizontal_winner(self) -> int | None:
        for row in range(len(self.board)):
            start = 0
            while start + 3 < len(self.board[0]):
                maybe_winner = self.board[row][start]
                if maybe_winner == 0:
                    start += 1
                    continue
                for x in range(1, 4):
                    if self.board[row][start + x] != maybe_winner:
                        break
                if x == 3 and self.board[row][start + x] == maybe_winner:
                    return maybe_winner
                start += 1


    def __diagonal_winner(self) -> int | None:
        diagonals = [
            [(0, 0), (1, 1), (2, 2), (3, 3)],
            [(0, 1), (1, 2), (2, 3), (3, 4)],
            [(0, 2), (1, 3), (2, 4), (3, 5)],
            [(0, 3), (1, 4), (2, 5), (3, 6)],
            [(1, 0), (2, 1), (3, 2), (4, 3)],
            [(1, 1), (2, 2), (3, 3), (4, 4)],
            [(1, 2), (2, 3), (3, 4), (4, 5)],
            [(1, 3), (2, 4), (3, 5), (4, 6)],
            [(2, 0), (3, 1), (4, 2), (5, 3)],
            [(2, 1), (3, 2), (4, 3), (5, 4)],
            [(2, 2), (3, 3), (4, 4), (5, 5)],
            [(2, 3), (3, 4), (4, 5), (5, 6)],
            [(3, 0), (2, 1), (1, 2), (0, 3)],
            [(3, 1), (2, 2), (1, 3), (0, 4)],
            [(3, 2), (2, 3), (1, 4), (0, 5)],
            [(3, 3), (2, 4), (1, 5), (0, 6)],
            [(4, 0), (3, 1), (2, 2), (1, 3)],
            [(4, 1), (3, 2), (2, 3), (1, 4)],
            [(4, 2), (3, 3), (2, 4), (1, 5)],
            [(4, 3), (3, 4), (2, 5), (1, 6)],
            [(5, 0), (4, 1), (3, 2), (2, 3)],
            [(5, 1), (4, 2), (3, 3), (2, 4)],
            [(5, 2), (4, 3), (3, 4), (2, 5)],
            [(5, 3), (4, 4), (3, 5), (2, 6)]
        ]
        for diagonal in diagonals:
            match = True
            maybe_winner = self.board[diagonal[0][0]][diagonal[0][1]]
            if maybe_winner == 0:
                continue
            for pos in diagonal[1:]:
                if self.board[pos[0]][pos[1]] != maybe_winner:
                    match = False
            if match is True:
                return maybe_winner


    def __check_win_condition(self) -> None:
        h_winner = self.__horizontal_winner()
        if h_winner is not None:
            self.winner = h_winner
            print(f'H winner with board:\n{self}')
            return

        v_winner = self.__vertical_winner()
        if v_winner is not None:
            self.winner = v_winner 
            print(f'V winner with board:\n{self}')
            return     
        
        d_winner = self.__diagonal_winner()
        if d_winner is not None:
            self.winner = d_winner
            return
        

    def has_winner(self) -> bool:
        return self.winner is not None
    

    def __player_to_move(self) -> int:
        if self.to_move == 2:
            return 1
        else:
            return 2
    

    def get_winner(self) -> int:
        return self.winner
        

    def move(self, col: int) -> bool:
        """
        Returns bool indicating if move was legal.
        """

        if self.__is_legal(col) is False:
            return False
        
        if self.get_winner() is not None:
            return False

        self.board[self.tops[col] + 1][col] = self.to_move
        self.tops[col] += 1
        self.__check_win_condition()
        self.to_move = self.__player_to_move()
        self.turn += 1
        
        return True
        