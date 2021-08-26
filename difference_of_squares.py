def difference_of_squares(n_limit):

    squareSum = 0
    sumSquare = 0
    
    for k in range(1, n_limit + 1):
        squareSum += k
        
    squareSum = squareSum ** 2
    
    for k in range(1, n_limit + 1):
        sumSquare += k ** 2
    
    return squareSum, sumSquare, squareSum - sumSquare

print(difference_of_squares(10))