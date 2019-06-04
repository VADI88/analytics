def solution(N):
    s = str(bin(N)).strip("0b")
    print(s)
    count = 0
    count_final = 0
    for i in range(0, len(s)):
        if i == 0:
            prev = s[i]
        else:
            if (prev == s[i - 1]) & (s[i] == "0"):
                count += 1
                prev = s[i]
            elif s[i] == "1":
                if count > count_final:
                    count_final = count
                count = 0

    return count_final


N = [1, 2, 3, 4, 5, 147, 483, 647,1041]

for i in N:
    print(solution(i))