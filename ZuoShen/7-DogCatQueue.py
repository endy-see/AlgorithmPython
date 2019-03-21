"""
猫狗队列
给定宠物、猫和狗的类，实现一种猫狗队列的结构，要求实现如下方法：
add：将cat类和dog类的实例放入队列中
     如果type='dog'，入狗队列（右边入队）；type='cat'，入猫队列
pollAll：将队列中所有的实例按照进队列的先后顺序依次弹出
     比较猫狗队列对头（左边）count大小，小者先出
pollDog：将队列中dog类的实例按照进队列的先后顺序依次弹出
pollCat：将队列中cat类的实例按照进队列的先后顺序依次弹出
isEmpty：检查队列中是否还有dog或cat的实例
isDogEmpty：检查队列中是否有dog类的实例
isCatEmpty：检查队列中是否有cat类的实例
"""


class Pet:
    def __init__(self, type):
        self.type = type


class Dog(Pet):
    def __init__(self):
        super(Dog, self).__init__('dog')


class Cat(Pet):
    def __init__(self):
        super(Cat, self).__init__('cat')


class PetEnterQueue:
    def __init__(self, pet, count):
        self.pet = pet
        self.count = count

    def get_enter_pet_type(self):
        return self.pet.type


from collections import deque


class DogCatQueue:
    def __init__(self):
        self.dogQ = deque()
        self.catQ = deque()
        self.count = 0

    def add(self, pet):
        if pet.type == 'dog':
            self.dogQ.append(PetEnterQueue(pet, self.count))
            self.count += 1
        elif pet.type == 'cat':
            self.catQ.append(PetEnterQueue(pet, self.count))
            self.count += 1
        else:
            raise Exception('err, not dog or cat')

    def pollAll(self):
        if self.dogQ and self.catQ:
            if self.dogQ[0].count < self.catQ[0].count:
                return self.dogQ.popleft().pet
            else:
                return self.catQ.popleft().pet
        elif self.dogQ:
            return self.dogQ.popleft().pet
        elif self.catQ:
            return self.catQ.popleft().pet
        else:
            raise RuntimeError('err, queue is empty!')

    def pollDog(self):
        if self.dogQ:
            return self.dogQ.popleft().pet
        raise RuntimeError('err, Dog queue is empty!')

    def pollCat(self):
        if self.catQ:
            return self.catQ.popleft().pet
        raise RuntimeError('err, Cat queue is empty!')

    def isEmpty(self):
        return self.catQ and self.dogQ

    def isDogQueueEmpty(self):
        return True if not self.dogQ else False

    def isCatQueueEmpty(self):
        return True if not self.catQ else False


if __name__ == '__main__':
    dog_cat_queue = DogCatQueue()

    dog1 = Dog()
    cat1 = Cat()
    dog2 = Dog()
    cat2 = Cat()
    dog3 = Dog()
    cat3 = Cat()

    dog_cat_queue.add(dog1)
    dog_cat_queue.add(cat1)
    dog_cat_queue.add(dog2)
    dog_cat_queue.add(cat2)
    dog_cat_queue.add(dog3)
    dog_cat_queue.add(cat3)

    dog_cat_queue.add(dog1)
    dog_cat_queue.add(cat1)
    dog_cat_queue.add(dog2)
    dog_cat_queue.add(cat2)
    dog_cat_queue.add(dog3)
    dog_cat_queue.add(cat3)

    dog_cat_queue.add(dog1)
    dog_cat_queue.add(cat1)
    dog_cat_queue.add(dog2)
    dog_cat_queue.add(cat2)
    dog_cat_queue.add(dog3)
    dog_cat_queue.add(cat3)

    while not dog_cat_queue.isDogQueueEmpty():
        print(dog_cat_queue.pollDog().type)

    while not dog_cat_queue.isEmpty():
        print(dog_cat_queue.pollAll().type)
