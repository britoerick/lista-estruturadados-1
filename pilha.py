def isEmpty(array):
    if not array:
        return True
    else:
        return False


def size(array):
    return len(array)


def top(array):
    return array[-1]


def pop(array):
    return array[:-1]


def push(value, array):
    if type(array) is str:
        arrayAux = []
        for i in range(0, len(array)):
            arrayAux.append(array[i])

        arrayAux.append(value)
        return arrayAux
    else:
        array.append(value)
        return array