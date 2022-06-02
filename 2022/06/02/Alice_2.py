class Judge:
    def __init__(self):
        self.roleClass = None

    def __getattribute__(self, item):
        print(item, 'hi')

    def testify(self, target):
        print('증언하라!', self)
        pass

    def call_witness(self, guard, target):
        guard.come_in_witness(target)


class Cook:
    def __init__(self):
        pass

    def cooking(self):
        print('요리중!')


class Guard:
    def __init__(self):
        pass

    def come_in_witness(self, target):
        pass


class Witness:
    def __init__(self):
        pass

    def say(self):
        pass


class King:
    def __init__(self):
        self.__role_judge = None

    def __getattr__(self, name):
        return print('해당 메소드가 없습니다. ', name)

    @property
    def judge(self):
        return self.__role_judge

    @judge.setter
    def judge(self, data):
        self.__role_judge = data

    def start_judgment(self, data):
        data.roleClass = self
        self.judge = data


class Queen:
    def __init__(self):
        self.role = None


class WhiteRabbit:
    def __init__(self):
        self.role = None

    def start_guide(self, guard):
        self.role = guard


class HatSeller:
    def __init__(self):
        pass


class Alice:
    def __init__(self):
        pass


class Chef:
    def __init__(self):
        pass


# 역할을 넣었다 뺐다
def main():
    judge = Judge()
    guard = Guard()
    witness = Witness()
    alice = Alice()

    heart_king = King()
    heart_king.start_judgment(judge)
    rabbit = WhiteRabbit()
    rabbit.start_guide(guard)
    heart_king.judge.call_witness(guard, alice)


if __name__ == '__main__':
    main()

