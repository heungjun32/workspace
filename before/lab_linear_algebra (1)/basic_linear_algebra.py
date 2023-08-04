def vector_size_check(*vector_variables):
    result = [len(vector_variables[a]) == len(vector_variables[a+1]) for a in range(len(vector_variables) - 1)]
    return all(result) 


def vector_addition(*vector_variables):
    result = [sum (t) for t in zip(*vector_variables)]
    return result


def vector_subtraction(*vector_variables):
    if vector_size_check(*vector_variables) == False:
        raise ArithmeticError
    result = [2*t[0]-sum(t) for t in zip(*vector_variables)]
    return result


def scalar_vector_product(alpha, vector_variable):
    result = [alpha * t for t in vector_variable]
    return result


def matrix_size_check(*matrix_variables):
    result = [len(matrix_variables[a]) == len(matrix_variables[a+1]) for a in range(len(matrix_variables) - 1)]
    return all(result)


def is_matrix_equal(*matrix_variables):
    token_list = []
    for matrix in zip(*matrix_variables):
        for row in zip(*matrix):
            token_result = True if row[0] == row [1] else False
            token_list.append(token_result)
    if False in token_list:
        result = False
    else:
        result = True
    
    return result


def matrix_addition(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    
    result = [[sum(row) for row in zip(*t)] for t in zip(*matrix_variables)]

    # result = []
    # for row in zip(*matrix_variables):
    #     bind_list = []
    #     for elements in zip(*row):
    #         elements = sum (elements)
    #         bind_list.append(elements)
    #     result.append(bind_list)

    return result


def matrix_subtraction(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError

    result = [[2*i[0]-sum(i) for i in zip(*t)] for t in zip(*matrix_variables)]

    # result = []
    # for row in zip(*matrix_variables):
    #     bind_list = []
    #     for elements in zip(*row):
    #         elements = 2*(elements[0]) - sum(elements)
    #         bind_list.append(elements)
    #     result.append(bind_list)

    return result


def matrix_transpose(matrix_variable):
    result = [[i for i in t] for t in zip(*matrix_variable)]
    return result

def scalar_matrix_product(alpha, matrix_variable):
    result = []
    for row in matrix_variable:
        bind_list = []
        for elements in row:
            elements = alpha * elements
            bind_list.append(elements)
        result.append(bind_list)
    
    return result


def is_product_availability_matrix(matrix_a, matrix_b):
    result = len([t for t in zip(*matrix_a)])==len(matrix_b)
    return result


def matrix_product(matrix_a, matrix_b):
    if is_product_availability_matrix(matrix_a, matrix_b) == False:
        raise ArithmeticError
    result = []
    for row in matrix_a:
        bind_list = []
        for column in zip(*matrix_b):
            elements = []
            for a,b in zip(row,column):
                elements.append( a * b )
            bind_list.append(sum(elements))
        result.append(bind_list)
    return result

if __name__ == "__main__":
    

    matrix_x= [[2, 5], [1, 1]]
    matrix_y = [[1, 1, 2], [2, 1, 1]]
    matrix_z = [[2, 4], [5, 3], [1, 3]]

    print(matrix_product(matrix_y, matrix_z)) # Expected value: [[9, 13], [10, 14]]
    print(matrix_product(matrix_z, matrix_x)) # Expected value: [[8, 14], [13, 28], [5, 8]]
    print(matrix_product(matrix_x, matrix_x)) # Expected value: [[9, 15], [3, 6]]
    print(matrix_product(matrix_z, matrix_w)) # Expected value: False