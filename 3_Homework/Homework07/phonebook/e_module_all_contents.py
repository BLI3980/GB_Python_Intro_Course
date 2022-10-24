import d_data_read as book

#  Takes formatted data and outputs the entire table to tabulated format.
# =======================================================================


def show_all(data):
    table = book.data_read(data)
    data = []
    temp = []
    for item in table:
        for value in item.values():
            temp.append(value)
        data.append(temp)
        temp = []
    return data


