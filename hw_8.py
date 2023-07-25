import random


class IceCream:
    """A new hw8's class show briefly a process of production an icecream in Lumpaland"""

    def __init__(self, portion_w=100, color="white", shape=("parallelipped", 100, 60, 40)):
        self.portion_w = portion_w
        self.color = color
        self.shape = shape
        # principals of creating
        self._receipe()

    _key = "milk"

    def _receipe(self):
        fat = {"milk": 3, "cream": 10, "plomb": 15, "creme brulee": 20}
        return fat.get(self._key)

    @staticmethod
    def __change_gcolor():
        rgbl = [255, 0, 0]
        random.shuffle(rgbl)
        return tuple(rgbl)

    def show(self):
        print(self.__change_gcolor(), self._receipe())

    def _message_of_the_day(self, salt):
        print("will be soon")

    # getter and setter section
    def get_key(self):
        return self._key

    def set_key(self, key):
        self._key = key


# inheritance and ovrriding

class Shake(IceCream):
    def __init__(self, portion_w=100, color='white', shape=None):
        super().__init__(portion_w, color, shape)
        super()._receipe()

    _key = "cream"

    def _message_of_the_day(self, salt):
        print(f"Only Baskin Robbins's balls and {salt} make you today happier")


class IceTart(IceCream):

    def _message_of_the_day(self, salt):
        """if datatype is int or float then get %10 and will inscribe remainder that way"""
        if type(salt) == 'int' or type(salt) == float:
            salt = str(salt % 10) + " ounces"


FamilyChunk = IceCream(250, 'orange', ("parallelipped", 200, 80, 50))
ice_tart = IceTart(1000, "brown", ("circle", 150))

milk_shake = Shake()
FamilyChunk.show()
milk_shake.show()