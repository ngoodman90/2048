from two_thousand_forty_eight import TwoThousandFortyEight


def main():
    g = TwoThousandFortyEight(board=[[0, 0, 0, 0],
                                     [0, 0, 0, 0],
                                     [0, 0, 0, 0],
                                     [0, 0, 1024, 1024]])
    while not g.has_lost():
        try:
            g.print_board()
            print('Waiting for input')
            g.parse_input()
            g.add_value_to_random_zeroed_cell()
            if g.has_won():
                print('Congratulations! You won the game :)')
        except ValueError as e:
            print(str(e))
    print('You lost')


if __name__ == "__main__":
    main()
