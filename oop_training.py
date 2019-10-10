class Member:
    def __init__(self, login, passw, name, id, age, gender, product, child):
        self.__login = login
        self._password = passw
        self._name = name
        self._id = id
        self._age = age
        self._gender = gender
        self._product = product
        self._children = child

    # ID

    def set_id(self, new_id):
        self._id = new_id

    def get_id(self):
        print('Member class')
        return self._id

    # NAME

    def set_name(self, new_name):
        self._name = new_name

    def get_name(self):
        return self._name

    # AGE

    def set_date(self, new_date):
        self._age = new_date

    def get_date(self):
        return self._age

    # GENDER

    def set_gender(self, new_gender):
        self._gender = new_gender

    def get_gender(self):
        return self._gender

    # CHILD

    def set_children(self, child):
        self._children = child

    def get_children(self):
        return self._children

    # PRODUCT

    def set_product(self, product):
        self._product = product

    def get_product(self):
        return self._product

    def set_product_child(self, product_child):
        self._product.append(product_child)

    @classmethod
    def what_is(cls):
        return 'registration form'


class Men(Member):
    def __init__(self, login, passw, name, id, age,
                 gender, product, child, pushup):
        super().__init__(login, passw, name, id, age,
                         gender, product, child)
        self.__pushup = pushup

    def gold_pushup(self):
        if 18 <= self._age <= 30:
            if self.__pushup < 45:
                print('good number of push-up with your weight:')
                return 45
            else:
                print('good number of push-up with your weight:')
                return self.__pushup
        elif 31 <= self._age <= 50:
            if self.__pushup < 30:
                print('good number of push-up with your weight:')
                return 30
            else:
                return self.__pushup
        elif 51 <= self._age <= 80:
            if self.__pushup < 15:
                print('good number of push-up with your weight:')
                return 15
            else:
                print('good number of push-up with your weight:')
                return self.__pushup

    def get_id(self):
        print('Men class')
        return self._id

    @classmethod
    def what_is(cls):
        return 'information of male member'


class Women(Member):
    def __init__(self, login, passw, name, id, age,
                 gender, product, child, weight, squat):
        super().__init__(login, passw, name, id, age,
                         gender, product, child)
        self.__squat = squat
        self.__weight = weight

    def gold_squat(self):
        if 18 <= self._age <= 30:
            if self.__squat < 50:
                print(self.__weight * 1.5, 'maximum weight in barbell back squat')
                print('good number of squat with your weight:')
                return 40
            else:
                print(self.__weight * 1.5, 'maximum weight in barbell back squat')
                print('good number of squat with your weight:')
                return self.__squat
        elif 31 <= self._age <= 45:
            if self.__squat < 35:
                print(self.__weight * 1.5 - 15, 'maximum weight in barbell back squat')
                print('good number of squat with your weight:')
                return 25
            else:
                print(self.__weight * 1.5 - 10, 'maximum weight in barbell back squat')
                print('good number of squat with your weight:')
                return self.__squat
        elif 46 <= self._age <= 65:
            if self.__squat < 15:
                print('good number of squat with your weight:')
                return 15
            else:
                print('good number of squat with your weight:')
                return self.__squat

    def get_id_child(self):
        print('Women class')
        return self._id

    @classmethod
    def what_is(cls):
        return 'information of female member'


woman1 = Women('login', 'pass', 'Alexandra', 1, 24,
               'female', ['Watercolor', 'JS'], False, 46, 30)
man1 = Men('login', 'pass', 'Alexander', 2, 25,
           'male', ['Weapon', 'Men clothes', 'JS'], False, 15)


woman1.set_children(True)


print('----------append new item of product----------')


man_woman_list = [woman1, man1]
for item in range(len(man_woman_list)):
    if man_woman_list[item].get_children():
        man_woman_list[item].set_product_child('Children clothes')
