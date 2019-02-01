def solve(source, destination, middle, n):
    if n == 1:
        print('Move ', n, ' from ', source, ' to ', destination)
        return;
    solve(source, middle, destination, n-1)
    print('Move ', n ,' from ', source,' to ', destination)
    solve(middle, destination, source, n-1)

solve('A', 'C', 'B', 3)