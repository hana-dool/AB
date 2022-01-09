"""This module does blah blah."""


class Person:
    """ddddd
    Ags:
        why you say like that?
    Returns:
        dsd s
    """

    def __init__(self, name, age, address):
        """[summary]
        Args:
            name ([type]): [description]
            age ([type]): [description]
            address ([type]): [description]
        """
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        """[summary]
        """
        print(f"안녕하세요. 저는 {self.name}입니다.")

    def greeting2(self):
        """[summary]
        """
        print(f"안녕하세요. 저는 {self.name}입니다.")

    def greeting3(self):
        """[summary]
        """
        print(f"안녕하세요. 저는 {self.name}입니다.")


if __name__ == "__main__":
    cls = Person("마리아", 29, "서울")
    cls.greeting()
