def Armstrong(N):
    sum = 0
    temp = N
    while(temp > 0):
        digit = temp % 10
        sum = sum + (digit**3)
        temp = temp // 10

    if N == sum:
        print(N, "is a Armstrong number.")
    else:
        print(N, "is not a Armstrong number.")

Armstrong(153)
Armstrong(371)
Armstrong(12212)
