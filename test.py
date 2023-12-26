from Game import Game


def test_vertical_win():
    game = Game()

    i = 0
    while not game.has_winner():
        if i % 2 == 0:
            is_legal = game.move(1)
        else:
            is_legal = game.move(0)
        assert is_legal, 'Illegal move was made.'
        i += 1

    assert game.get_winner() == 1, f'Winner should be 1. Was: {game.get_winner()}.'
    assert i == 7, f'Win should be on 6th move. Was: {i}'


def test_horizontal_win_from_left():
    game = Game()

    i = 0
    white = 0
    while not game.has_winner():
        if i % 2 == 0:
            is_legal = game.move(white)
            white += 1
        else:
            is_legal = game.move(5)
        assert is_legal, 'Illegal move was made.'
        i += 1

    assert game.get_winner() == 1, f'Winner should be 1. Was: {game.get_winner()}.'
    assert i == 7, f'Win should be on 6th move. Was: {i}'


def test_horizontal_win_from_right():
    game = Game()

    i = 0
    white = 6
    while not game.has_winner():
        if i % 2 == 0:
            is_legal = game.move(white)
            white -= 1
        else:
            is_legal = game.move(1)
        assert is_legal, 'Illegal move was made.'
        i += 1
        print(f'Move: {i}. Has winner: {game.has_winner()}\nGame:\n{game}')
    print(f'Final board:\n{game}')

    assert game.get_winner() == 1, f'Winner should be 1. Was: {game.get_winner()}.'
    assert i == 7, f'Win should be on 6th move. Was: {i}'


def test_random_1():
    game = Game()
    moves = [0, 5, 1, 0, 4, 1, 0, 3, 2, 3, 0, 5, 0, 2]
    for move in moves:
        is_legal = game.move(move)
        assert is_legal, f'Illegal move: {move}.'
    assert game.get_winner() == 2, f'Was expecting winner == 2. Was: {game.get_winner()}'


def test_random_2():
    game = Game()
    moves = [3, 5, 2, 2, 6, 3, 5, 1, 0, 2, 4, 4, 6, 4, 3, 5, 0, 4, 1, 6, 5, 2, 6, 6, 2, 5, 6, 3, 1, 1]
    for move in moves:
        is_legal = game.move(move)
        assert is_legal, f'Illegal move: {move}.'
    assert game.get_winner() == 2, f'Was expecting winner == 2. Was: {game.get_winner()}'


def test_diagonal_1():
    game = Game()
    moves = [0, 1, 1, 2, 3, 2, 2, 3, 3, 4, 3]
    for move in moves:
        is_legal = game.move(move)
        assert is_legal, f'Illegal move: {move}.'
    assert game.get_winner() == 1, f'Was expecting winner == 1. Was: {game.get_winner()}'


def test_diagonal_2():
    game = Game()
    moves = [6, 5, 5, 4, 3, 4, 4, 3, 3, 4, 3]
    for move in moves:
        is_legal = game.move(move)
        assert is_legal, f'Illegal move: {move}.'
    assert game.get_winner() == 1, f'Was expecting winner == 1. Was: {game.get_winner()}'


def test_illegal_continuation():
    game = Game()
    moves = [6, 5, 5, 4, 3, 4, 4, 3, 3, 4, 3]
    for move in moves:
        is_legal = game.move(move)
        assert is_legal, f'Illegal move: {move}.'
    assert not game.move(0), 'Wrongly allowed move after a player wins.'


def test_deny_too_high():
    game = Game()
    moves = [0, 0, 0, 0, 0, 0]
    for move in moves:
        is_legal = game.move(move)
        assert is_legal, f'Illegal move: {move}.'
    error = None
    try:
        game.move(0)
    except IndexError as e:
        error = e
    assert type(error) == IndexError, 'Expected IndexError on illegal move.'


def test_random_3():
    game = Game()
    moves = [0, 4, 6, 5, 0, 1, 5, 1, 1, 5, 4, 1, 3, 0, 3, 2, 3, 1, 0, 0, 2]
    for i, move in enumerate(moves):
        print(f'About to move with Game:\n{game}')
        is_legal = game.move(move)
        assert is_legal, f'Move #{i} should have been legal.'


# test_horizontal_win_from_right()
# import random
# print('[' + ', '.join([str(random.randint(0, 6)) for _ in range(30)]) + ']')
# test_random_3()