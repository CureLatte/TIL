def solution(s):
    answer = True
    smaller = s.lower()
    q_p = 0
    q_y = 0

    for letter in smaller:
        if letter == 'p':
            q_p += 1
        elif letter == 'y':
            q_y += 1
    if q_p == q_y:

        return True
    else:
        return False