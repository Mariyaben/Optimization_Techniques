#4. Sequencing Problem

import numpy as np

def sequence_assign(seq_table):
    if len(seq_table) != 2:
        seq_table = convert_to_2_machines(seq_table)
    print("seq_table", seq_table)
    assign = np.zeros(len(seq_table[0]))
    marked = np.zeros([2, len(seq_table[0])])
    i_H = 0
    i_G = -1

    while (np.sum(marked) / 2) != len(seq_table[0]):
        print("marked", marked)
        print("zeros", np.min(seq_table[marked == 0]))
        print(seq_table)

        min_value = np.min(seq_table[marked == 0])  # Corrected line
        min_index = np.where(seq_table == min_value)
        print("min_index", min_index)

        if len(min_index[1]) == 1:
            if min_index[0][0] == 0:
                assign[i_H] = min_index[1][0]
                marked[0, min_index[1][0]] = 1
                marked[1, min_index[1][0]] = 1
                i_H += 1
            elif min_index[0][0] == 1:
                assign[i_G] = min_index[1][0]
                marked[0, min_index[1][0]] = 1
                marked[1, min_index[1][0]] = 1
                i_G -= 1
        else:
            if min_index[0][0] == min_index[0][1]:
                if seq_table[min_index[0][1], min_index[1][1]] < seq_table[min_index[0][0], min_index[1][0]]:
                    assign[i_G] = min_index[1][1]
                    marked[0, min_index[1][1]] = 1
                    marked[1, min_index[1][1]] = 1
                    i_G -= 1
                else:
                    assign[i_H] = min_index[1][0]
                    marked[0, min_index[1][0]] = 1
                    marked[1, min_index[1][0]] = 1
                    i_H += 1
            else:
                assign[i_H] = min_index[1][0]
                assign[i_G] = min_index[1][1]
                marked[0, min_index[1][0]] = 1
                marked[1, min_index[1][1]] = 1
                i_H += 1
                i_G -= 1

    return assign, marked

def main():
    table = np.array([[2, 5, 4, 9, 6, 8, 7, 5, 4], [6, 8, 7, 4, 3, 9, 3, 8, 11]])
    assign, marked = sequence_assign(table)
    print("Assignments:", assign)
    print("Marked:", marked)

if __name__ == "__main__":
    main()
