from src import tic_tac_toe_winner


def test_import_tic_tac_toe_winner():
    try:
        from tic_tac_toe import tic_tac_toe_winner  # ➜ 1
        assert callable(tic_tac_toe_winner), "tic_tac_toe not callable"  # ➜ 2
    except ImportError as error:  # ➜ 3
        assert False, error


if __name__ == '__main__':
    for test in (
            test_import_tic_tac_toe_winner,
    ):  # ➜ 4
        print(f'{test.__name__}: ', end='')
        try:
            test()
            print('OK')
        except AssertionError as error:
            print(error)


def test_empty_board():
    assert tic_tac_toe_winner(' ' * 9) is None


def test_3x_in_a_row():
    winner = tic_tac_toe_winner('XXX O O  ')
    assert winner == 'X', f"expected X, got {winner}"


