def solution(dartResult):
    answer = 0
    points = []
    point = ''
    cnt = 0
    for letter in dartResult:
        if letter.isdigit():
            point += letter
            continue
        else:
            if letter == 'D':
                points.append(int(point) ** 2)
            elif letter == 'S':
                points.append(int(point) ** 1)
            elif letter == 'T':
                points.append(int(point) ** 3)
            else:
                print(letter)
                if letter == '*':
                    points[-1] *= 2
                    try:
                        points[-2] *= 2
                    except:
                        pass
                elif letter == '#':
                    points[-1] *= -1

            point = ''
    return sum(points)
