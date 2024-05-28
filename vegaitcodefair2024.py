from collections import deque

def puddles(matrix):
    # We can represent the puddle as a m*n matrix filled with ones and zeroes
    depth = len(matrix)
    water = 0
    for i in range(depth):
        # The iteration through the matrix starts from the last row
        current_row = matrix[depth - 1 - i]
        stack = deque()
        for field in current_row:
            # We skip over the empty fields at the beginning and push all other fields on a stack
            if field == 0 and len(stack) == 0:
                pass
            else:
                stack.append(field)
        # This variable will check whether we're inside a puddle or not
        # We will remove empty fields top of the stack until we reach a field with mud, starting from there
        # water will build up in the puddle, which we will account for in the water variable 
        inside = False
        while len(stack) != 0:
            stack_top = stack.pop()
            if not inside and stack_top == 0:
                continue
            elif stack_top == 1:
                inside = True
            elif inside and stack_top == 0:
                water += 1
    return water

if __name__ == "__main__":

    puddle_A = [[1, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 1, 0, 0, 0, 1],
                [1, 0, 0, 1, 1, 0, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1]]
    print(puddles(puddle_A))

    puddle_B = [[1, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 1, 0, 0, 0, 1],
                [1, 0, 1, 1, 0, 0, 1, 1],
                [1, 1, 1, 1, 0, 0, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1]]
    print(puddles(puddle_B))