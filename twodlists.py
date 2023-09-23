#essentially creating a grid structure
number_grid = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9], 
    [0]
]
#[row][index]
print(number_grid[2][1])

#how to go through 2d list 
for row in number_grid: 
    for col in row: 
        print(row)