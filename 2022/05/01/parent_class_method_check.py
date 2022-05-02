class Parent:
    def my_method(self):
        return '부모의 결과'


class Child(Parent):
    def my_method(self, *args, **kwargs):
        print('자식 ')
        # super를 통해서 상위 부모클래스를 실행
        return super(Child, self).my_method(*args, **kwargs)


def in_framework():
    result = Child().my_method()
    print(result)

in_framework()
