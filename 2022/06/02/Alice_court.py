class Judge:
    def __init__(self):
        self.role = None
        self.witness = None

    def testify(self):
        print(self.role.name, ':  증언하라!')
        print(self.witness.role.name, ': ', self.witness.role.saw)

    def call_witness(self, guard, target):
        print(self.role.name, ': ', target.name , '을 불러와라!')
        self.witness = guard.take_witness(target)
        print('\n', self.witness.role.name , '이 증인석으로 왔다. \n')

    def end_judgment(self):
        print('\n', self.role.name, '가 판사 자리를 물러났다.\n')
        print('법정 끝!')


class Guard:
    def __init__(self):
        self.role = None

    def take_witness(self, witness):
        print(self.role.name, ': ', witness.name, '는 증인석으로 오시오!')
        w = Witness()
        w.role = witness
        return w


class Witness:
    def __init__(self):
        self.role = None

    def testimony(self):
        return self.role.saw()


class King:
    def __init__(self):
        self.name = '하트킹'

    def start_judgment(self):
        print('\n', self.name, '가 재판을 열었다!\n')
        judge = Judge()
        judge.role = self
        guard = Guard()
        return judge, guard


class Queen:
    def __init__(self):
        self.name = '하트 퀸'

    def start_judgment(self):
        print('\n', self.name, '가 재판을 열었다!\n')
        judge = Judge()
        judge.role = self
        guard = Guard()
        return judge, guard


class Alice:
    def __init__(self):
        self.name = '앨리스'
        self.saw = '저는 아무것도 몰라요!'


class Chef:
    def __init__(self):
        self.name = '요리사'
        self.saw = '저는 요리만 했습니다!'


class Rabbit:
    def __init__(self):
        self.name = '하얀 토끼'
        self.saw = '나는 못봄'


def main():
    heart_king = King()
    alice = Alice()
    rabbit = Rabbit()
    queen = Queen()
    chef = Chef()

    judge, guard = heart_king.start_judgment()
    guard.role = rabbit

    judge.call_witness(guard, alice)
    judge.testify()

    judge.call_witness(guard, chef)
    judge.testify()

    judge.end_judgment()

    q_judge, q_guard = queen.start_judgment()
    q_guard.role = rabbit

    q_judge.call_witness(q_guard, chef)
    q_judge.testify()

    judge.end_judgment()


if __name__ == '__main__':
    main()