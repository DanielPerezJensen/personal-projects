import lifegame as lg

if __name__ == "__main__":

    init_state1 = [[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]

    expected_next_state1 = [[0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0]]

    actual_next_state1 = lg.iterate(init_state1)

    if expected_next_state1 == actual_next_state1:
        print('Passed 1')
    else:
        print('Failed 1')
        print("Expected:\n {}".format(expected_next_state1))
        print("Actual:\n {}".format(actual_next_state1))

    init_state2 = [[0, 0, 1],
                   [0, 1, 1],
                   [0, 0, 0]]
    expected_next_state2 = [[0, 1, 1],
                            [0, 1, 1],
                            [0, 0, 0]]
    actual_next_state2 = lg.iterate(init_state2)
    if expected_next_state2 == actual_next_state2:
        print('Passed 2')
    else:
        print('Failed 1')
        print('Expected:\n'.format(expected_next_state2))
        print('Actual:\n'.format(actual_next_state2))
