from abc import ABCMeta, abstractmethod


# 오리의 추상 클래스
class Duck(metaclass=ABCMeta):
    def __init__(self):
        self.name = ''
        # 추상 클래스 - 추상 인터페이스
        self.flybehavior = FlyBehavior()
        self.quackbehavior = QuackBehavior()

    def swim(self):
        return print(self.name + 'is swiming!')

    def display(self):
        return print(self.name + 'is display!')

    def fly(self):
        self.flybehavior.fly()

    def quack(self):
        self.flybehavior.fly()


# Fly 종류를 나누기 위한 인터페이스
class FlyBehavior:
    @abstractmethod
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        return print('오리 날기!!')


class FlyWidthNoWings(FlyBehavior):
    def fly(self):
        return print('저는 날수 없어요')


# 울음 소리 행동 추가
class QuackBehavior:
    # 추상 메소드이므로 데코레이터 붙여주기
    @abstractmethod
    def quack(self):
        pass


# 울음소리 - 꽥꽥
class Quack(QuackBehavior):
    def quack(self):
        return print('꽥 꽥')


# 울음소리 - 삑 삑
class Squeack(QuackBehavior):
    def quack(self):
        return print('삑 삑')


# 울음소리 - 못냄
class MuteQuack(QuackBehavior):
    def quack(self):
        return print('아무것도 안함')


# 다양한 오리 클래스 구현 - MallardDuck
class MallardDuck(Duck):
    def __init__(self):
        super().__init__()
        self.name = 'MallardDuck'
        self.flybehavior = FlyWithWings()
        self.quackbehvior = MuteQuack()

    def fly(self):
        self.flybehavior.fly()

    def quack(self):
        self.quackbehvior.quack()


# 다양한 오리 클래스 구현 - JS Duck
class JSDuck(Duck):
    def __init__(self):
        super().__init__()
        self.name = 'JS오리'
        self.flybehavior = FlyWidthNoWings()
        self.quackbehavior = Squeack()


# Main 함수 실행
def main():
    a = MallardDuck()
    a.fly()
    a.swim()
    a.display()
    a.quack()

    b = JSDuck()
    b.fly()
    b.quack()
    return 0


if __name__ == "__main__":
    main()
