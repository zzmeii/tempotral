import random
from typing import Tuple

import numpy as np


class Individ:
    """
    Описание класса,переменных и перегрузок в нем
    """

    def __init__(self, gen: str):
        self.gen = gen
        self.fit = None
        self.length = len(gen)
        self.dec = self.transl()

    def transl(self):
        """
        Метод описывающий перевод в 10-чную систему
        """
        return int(self.gen, 2)

    def __add__(self, other):
        """
        Перегрузка плюсика
        скрещевание для создания потомков
        """
        model = [random.random() for _ in range(self.length)]
        son = ''
        daughter = ''
        for i in range(self.length):
            if model[i] < 0.5:
                son = son + self[i]
                daughter = daughter + other[i]
            else:
                son = son + other[i]
                daughter = daughter + self[i]

        return Individ(son), Individ(daughter)

    def __getitem__(self, item):
        """
        Работа со списком генотипа
        """
        return self.gen[item]

    def __lt__(self, other):
        """
        Перегрузка знака меньше
        """
        if self.fit < other.fit:
            return True
        return False


def opred(f, f_range, acc):
    def math(num):
        x = f_range[0] + (abs(f_range[1] - f_range[0]) / 2 ** acc) * num
        return eval(f)

    return math


def meow(funk, f_range, cucu, lim, size, f_type) -> Tuple[str, str, float]:
    """

    :param funk: иследуемая функция
    :param f_range:диапазон точек
    :param cucu:точность разбиения
    :param lim:ограничение
    :param size:размер популяции
    :param f_type:выбор значение эксремума (макс или мин)
    dc: список, содержащий точку начала, конца и точность разбиения
    popa: генерация списка с особями популяции
    :return возвращает точку экстремума, особь, точку расположения по оси Х
    """
    funk = opred(funk, f_range, cucu)
    stemps_num = int((f_range[1] - f_range[0]) / (abs(f_range[1] - f_range[0]) / 2 ** cucu))
    popa = [
        Individ(bin(random.randint(0, stemps_num)).replace('0b', '').zfill(len(bin(stemps_num - 1).replace('0b', ''))))
        for _ in range(size)]
    for _ in range(lim):
        for i in popa:
            i.fit = funk(i.dec) if f_type else -funk(i.dec)
        popa.sort()
        popa = popa[:size // 2]
        chil = []
        while len(popa) + len(chil) < size:
            pare = np.random.choice(a=popa, size=2, replace=False)
            temp = pare[0] + pare[1]
            chil.append(temp[0])
            chil.append(temp[1])
        for i in chil:
            popa.append(i)
    return popa[0].fit if f_type else - popa[0].fit, popa[0].gen, f_range[0] + (
                abs(f_range[1] - f_range[0]) / 2 ** cucu) * popa[0].dec


if __name__ == '__main__':
    tf = meow('x**3/(4*(2-x**5)**2)', [-2, 2], 25, 900, 43, 1)
    #       ['2*x/3*x**5', [5, 10], 25, 500, 40, 1]]
    # res = {}
    # for i in tf:
    #     res.update({i[0]: []})
    #     for k in range(10):
    #         res[i[0]].append(meow(i[0], i[1], i[2], i[3], i[4], i[5]))
    #         print(k)
    # print(res)
    # res = {'x**3/(4*(2-x**5)**2)': [(45762.43509822336, '1100100101111110110110111', 1.1483677625656128),
    #                                 (73.75233514402325, '1100101000001010101100001', 1.1569024324417114),
    #                                 (9.079512747664396, '1100011111111111111011110', 1.1249959468841553),
    #                                 (41527.30916706381, '1100100101111110100101101', 1.1483513116836548),
    #                                 (86.91806700578019, '1100101000000000001000001', 1.1562577486038208),
    #                                 (607835.8072890437, '1100100110000101110000101', 1.1487890481948853),
    #                                 (741048986.4189074, '1100100110000100010100010', 1.1487009525299072),
    #                                 (324.0500770909089, '1100100101000011110011101', 1.1447635889053345),
    #                                 (2.014382013625239, '1100110010100010011001000', 1.1974115371704102),
    #                                 (3878141.932417596, '1100100110000011101011111', 1.1486624479293823)],
    #        '2*x/3*x**5': [(10477.957719347958, '0000000001000000000111001', 5.0048913061618805),
    #                       (10416.72627145355, '0000000000000000000100000', 5.000004768371582),
    #                       (10416.728134107721, '0000000000000000000100001', 5.000004917383194),
    #                       (10417.27204099877, '0000000000000000101000101', 5.00004842877388),
    #                       (10417.14351291991, '0000000000000000100000000', 5.000038146972656),
    #                       (10428.35650203214, '0000000000001100010000001', 5.00093474984169),
    #                       (10416.675979895883, '0000000000000000000000101', 5.00000074505806),
    #                       (10416.741172694681, '0000000000000000000101000', 5.0000059604644775),
    #                       (10432.89151250377, '0000000000010001000000001', 5.001297146081924),
    #                       (10416.666666666668, '0000000000000000000000000', 5.0)]}
