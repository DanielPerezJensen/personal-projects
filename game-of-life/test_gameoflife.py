import gameoflife as gol
import unittest


class TestGameOfLife(unittest.TestCase):
    def test_iteration(self):
        # tests if iterations are correct
        init_state1 = [[0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0]]
        expected_next_state1 = [[0, 0, 0],
                                [0, 0, 0],
                                [0, 0, 0]]
        actual_next_state1 = gol.iterate(init_state1)

        init_state2 = [[0, 0, 1],
                       [0, 1, 1],
                       [0, 0, 0]]
        expected_next_state2 = [[0, 1, 1],
                                [0, 1, 1],
                                [0, 0, 0]]
        actual_next_state2 = gol.iterate(init_state2)

        self.assertEqual(expected_next_state1, actual_next_state1)
        self.assertEqual(expected_next_state2, actual_next_state2)

    def test_initialize_board(self):
        board1 = gol.init(5, 5)
        board2 = gol.init(4, 6)
        board3 = gol.init(23, 1)

        self.assertEqual(len(board1), 5)
        self.assertEqual(len(board1[0]), 5)

        self.assertEqual(len(board2), 4)
        self.assertEqual(len(board2[0]), 6)

        self.assertEqual(len(board3), 23)
        self.assertEqual(len(board3[0]), 1)

    def test_loadboard(self):
        expected_board_1 = [[0, 0, 0, 0, 0],
                            [0, 0, 1, 0, 0],
                            [0, 0, 1, 0, 0],
                            [0, 0, 1, 0, 0],
                            [0, 0, 0, 0, 0]]

        expected_board_2 = [[0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 1, 1, 1, 0],
                            [0, 1, 1, 1, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0]]

        actual_board_1 = gol.load_initial_state("beacon.txt")
        actual_board_2 = gol.load_initial_state("toad.txt")

        self.assertEqual(expected_board_1, actual_board_1)
        self.assertEqual(expected_board_2, actual_board_2)
