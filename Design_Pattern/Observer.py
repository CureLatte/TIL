# ABCMeta : 추상 클래스
# abstractmethod : 인터페이스

from abc import abstractmethod


# Observer 패턴은 interface만 사용한다!!!!
# Observer 인테페이스 구현
class Observer:
    # Observer 인터페이스는 update 메소드만!
    @abstractmethod
    def update_observer(self, value):
        pass


# Subject 인터페이스 구현
class Subject:
    # Observer 등록
    @abstractmethod
    def register_observer(self, observer: Observer):
        pass

    # Observer 등록 해제
    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    # Observer 변경된 내역 알려 주기!
    # value = 변경되는 값들 (여러개 가능)
    @abstractmethod
    def notify_observer(self, value):
        pass


########################################################
# 실제 모델 구현
class Newspaper(Subject):

    def __init__(self):
        # __observer_list : 구독자 들 리스트
        self.__observer_list = []

    # observer 등록 구현
    def register_observer(self, observer: Observer):
        self.__observer_list.append(observer)

    # observer 등록 해제 구현
    def remove_observer(self, observer: Observer):
        self.__observer_list.remove(observer)

    # observer 업데이트 구현
    def notify_observer(self, value):
        for observer in self.__observer_list:
            observer.update_observer(value)


# 학생 class
class Student(Observer):
    def __init__(self):
        self.__data = 'NO data'

    # 실제 데이터 업데이트
    def update_observer(self, value):
        self.__data = value

    # 데이터 변경 확인을 위한 메소드
    def check_data_receive(self):
        print(self.__data)


class Teacher(Observer):
    def __init__(self):
        self.__data = 'NO data'

    # 실제 데이터 업데이트
    def update_observer(self, value):
        self.__data = value

    # 데이터 변경 확인을 위한 메소드
    def check_data_receive(self):
        print(self.__data)


def main():
    # Newspaper 생성
    newspaper = Newspaper()
    user1 = Student()
    user2 = Teacher()

    print('---user1만 구독')
    newspaper.register_observer(user1)
    newspaper.notify_observer('1번')
    user1.check_data_receive()
    user2.check_data_receive()
    print('\n')

    print('---user1, user2 구독')
    newspaper.register_observer(user2)
    newspaper.notify_observer('2번')
    user1.check_data_receive()
    user2.check_data_receive()
    print('\n')

    print('---user2 구독')
    newspaper.remove_observer(user1)
    newspaper.notify_observer('3번')
    user1.check_data_receive()
    user2.check_data_receive()
    print('\n')

    print('---user1 user2 구독')
    newspaper.register_observer(user1)
    newspaper.notify_observer('4번')
    user1.check_data_receive()
    user2.check_data_receive()
    print('\n')


if __name__ == '__main__':
    main()
