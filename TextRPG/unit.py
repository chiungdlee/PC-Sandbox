class Unit :
    __name = ""
    __hp = ""
    __ap = ""

    def __init__(self, name, hp, ap):
        self.__name = name
        self.__hp = hp
        self.__ap = ap

    def set_hp(self, hp):
        self.__hp = hp

    def set_ap(self, ap):
        self.__ap = ap

