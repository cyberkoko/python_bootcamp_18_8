def add_matrices(m1, m2):
    rezult = ()
    for row_i in range(len(m1)):
        row = ()
        for col_i in range(len(m1(row_i)):
            element = m1(row_i)(col_i) + m2(row_i)(col_i)
            row.append(element)
        rezult.append(row)

    return rezult


def sub_matrices(m1, m2):
    rezult = ()
    for row_i in range(len(m1)):
        row = ()
        for col_i in range(len(m1(row_i))):
            element = m1(row_i)(col_i) - m2(row_i)(col_i)
            row.append(element)
        rezult.append(row)

    return rezult


