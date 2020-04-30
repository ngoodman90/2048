from unittest import TestCase

from two_thousand_forty_eight import TwoThousandFortyEight


class BoardTests(TestCase):
    def test_move_down_when_has_one_value_and_not_possible_then_error_raised(self):
        g = TwoThousandFortyEight(board=[[0, 0, 0, 0],
                                         [0, 0, 0, 0],
                                         [0, 0, 0, 0],
                                         [0, 0, 0, 2]])
        with self.assertRaises(ValueError):
            g.move_down()

    def test_move_down_when_bottom_row_populated_and_not_possible_then_error_raised(self):
        g = TwoThousandFortyEight(board=[[0, 0, 0, 0],
                                         [0, 0, 0, 0],
                                         [0, 0, 0, 0],
                                         [4, 8, 4, 2]])
        with self.assertRaises(ValueError):
            g.move_down()

    def test_move_down_when_right_row_populated_and_not_possible_then_error_raised(self):
        g = TwoThousandFortyEight(board=[[0, 0, 0, 4],
                                         [0, 0, 0, 2],
                                         [0, 0, 0, 4],
                                         [0, 0, 0, 2]])
        with self.assertRaises(ValueError):
            g.move_down()

    def test_move_down_when_has_merge_then_merged(self):
        g = TwoThousandFortyEight(board=[[0, 0, 0, 0],
                                         [0, 0, 0, 0],
                                         [0, 0, 0, 2],
                                         [0, 0, 0, 2]])
        self.assertEqual([[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 4]],
                         g.move_down())

    def test_move_down_when_has_merge_from_top_then_merged(self):
        g = TwoThousandFortyEight(board=[[0, 0, 0, 2],
                                         [0, 0, 0, 2],
                                         [0, 0, 0, 0],
                                         [0, 0, 0, 0]])
        self.assertEqual([[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 4]],
                         g.move_down())

    def test_move_down_when_has_merge_but_not_together_then_merged(self):
        g = TwoThousandFortyEight(board=[[0, 0, 0, 2],
                                         [0, 0, 0, 0],
                                         [0, 0, 0, 2],
                                         [0, 0, 0, 0]])
        self.assertEqual([[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 4]],
                         g.move_down())

    def test_move_down_when_has_merge_and_shouldnt_merge_then_one_merged(self):
        g = TwoThousandFortyEight(board=[[0, 0, 0, 4],
                                         [0, 0, 0, 2],
                                         [0, 0, 0, 2],
                                         [0, 0, 0, 0]])
        self.assertEqual([[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 4],
                          [0, 0, 0, 4]],
                         g.move_down())

    def test_move_down_when_has_two_merges_then_merged(self):
        g = TwoThousandFortyEight(board=[[0, 0, 0, 2],
                                         [0, 0, 0, 2],
                                         [0, 0, 0, 2],
                                         [0, 0, 0, 2]])
        self.assertEqual([[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 4],
                          [0, 0, 0, 4]],
                         g.move_down())

    def test_move_down_when_has_two_different_merges_then_merged(self):
        g = TwoThousandFortyEight(board=[[0, 0, 0, 4],
                                         [0, 0, 0, 4],
                                         [0, 0, 0, 2],
                                         [0, 0, 0, 2]])
        self.assertEqual([[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 8],
                          [0, 0, 0, 4]],
                         g.move_down())

    def test_move_down_when_value_has_to_move_all_the_way_down(self):
        g = TwoThousandFortyEight(board=[[0, 0, 0, 4],
                                         [0, 0, 0, 0],
                                         [0, 0, 0, 0],
                                         [0, 0, 0, 0]])
        self.assertEqual([[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 4]],
                         g.move_down())

    def test_move_up_when_has_one_value_and_not_possible_then_error_raised(self):
        g = TwoThousandFortyEight(board=[[0, 0, 0, 2],
                                         [0, 0, 0, 0],
                                         [0, 0, 0, 0],
                                         [0, 0, 0, 0]])
        with self.assertRaises(ValueError):
            g.move_up()

    def test_move_up_when_has_merge_then_merged(self):
        g = TwoThousandFortyEight(board=[[0, 0, 0, 0],
                                         [0, 0, 0, 0],
                                         [0, 0, 0, 2],
                                         [0, 0, 0, 2]])
        self.assertEqual([[0, 0, 0, 4],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0]],
                         g.move_up())

    def test_move_up_when_has_merge_but_not_together_then_merged(self):
        g = TwoThousandFortyEight(board=[[0, 0, 0, 2],
                                         [0, 0, 0, 0],
                                         [0, 0, 0, 2],
                                         [0, 0, 0, 0]])
        self.assertEqual([[0, 0, 0, 4],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0]],
                         g.move_up())

    def test_move_right_when_has_one_value_and_not_possible_then_error_raised(self):
        g = TwoThousandFortyEight(board=[[0, 0, 0, 0],
                                         [0, 0, 0, 0],
                                         [0, 0, 0, 0],
                                         [0, 0, 0, 2]])
        with self.assertRaises(ValueError):
            g.move_right()

    def test_move_down_when_bottom_row_populated_and_merges_possible_then_error_raised(self):
        g = TwoThousandFortyEight(board=[[0, 0, 0, 0],
                                         [0, 0, 0, 0],
                                         [0, 0, 0, 0],
                                         [4, 8, 4, 2]])
        with self.assertRaises(ValueError):
            g.move_right()

    def test_move_right_when_has_merge_but_not_together_then_merged(self):
        g = TwoThousandFortyEight(board=[[0, 0, 0, 0],
                                         [0, 0, 0, 0],
                                         [0, 0, 0, 0],
                                         [4, 0, 4, 0]])
        self.assertEqual([[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 8]],
                         g.move_right())

    def test_move_left_when_has_one_value_and_not_possible_then_error_raised(self):
        g = TwoThousandFortyEight(board=[[0, 0, 0, 0],
                                         [0, 0, 0, 0],
                                         [0, 0, 0, 0],
                                         [2, 0, 0, 0]])
        with self.assertRaises(ValueError):
            g.move_left()

    def test_move_left_when_bottom_row_populated_and_merges_possible_then_error_raised(self):
        g = TwoThousandFortyEight(board=[[0, 0, 0, 0],
                                         [0, 0, 0, 0],
                                         [0, 0, 0, 0],
                                         [4, 8, 4, 2]])
        with self.assertRaises(ValueError):
            g.move_left()

    def test_move_left_when_has_merge_but_not_together_then_merged(self):
        g = TwoThousandFortyEight(board=[[0, 0, 0, 0],
                                         [0, 0, 0, 0],
                                         [0, 0, 0, 0],
                                         [4, 0, 4, 0]])
        self.assertEqual([[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [8, 0, 0, 0]],
                         g.move_left())

    def test_add_value_to_random_zeroed_cell_doesnt_overwrtie_non_zero(self):
        g = TwoThousandFortyEight(board=[[8, 8, 8, 8],
                                         [8, 8, 8, 8],
                                         [8, 8, 8, 8],
                                         [8, 8, 8, 0]])
        g.add_value_to_random_zeroed_cell()
        self.assertTrue(g.board[3][3] in [2, 4])

    def test_has_lost_when_lost(self):
        g = TwoThousandFortyEight(board=[[8, 4, 2, 4],
                                         [4, 8, 4, 2],
                                         [8, 4, 8, 4],
                                         [4, 2, 4, 2]])
        self.assertTrue(g.has_lost())

    def test_has_lost_when_not_lost(self):
        g = TwoThousandFortyEight(board=[[8, 4, 2, 4],
                                         [4, 8, 4, 2],
                                         [8, 4, 8, 4],
                                         [4, 2, 4, 0]])
        self.assertFalse(g.has_lost())

    def test_has_won_when_not_won(self):
        g = TwoThousandFortyEight(board=[[8, 4, 2, 4],
                                         [4, 8, 4, 2],
                                         [8, 4, 8, 4],
                                         [4, 2, 4, 0]])
        self.assertFalse(g.has_won())

    def test_has_won_when_won(self):
        g = TwoThousandFortyEight(board=[[8, 4, 2, 4],
                                         [4, 8, 4, 2],
                                         [8, 4, 8, 4],
                                         [4, 2, 4, 2048]])
        self.assertTrue(g.has_won())
