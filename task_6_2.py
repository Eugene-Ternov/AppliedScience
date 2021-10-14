#2. Класс дороги и масса покрытия для неё (длина и ширина дороги - protected)

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_cover_weight(self, cover_unit_weight, cover_thick):
        return cover_unit_weight * cover_thick * self._length * self._width / 1000

if __name__ == "__main__":

    class InheritedRoad(Road):
        pass

    example_road = Road(4800, 25)
    asphalt_weight = example_road.get_cover_weight(25, 4.9)
    print(f"Масса асфальта: {asphalt_weight:.3f} т")
    p = InheritedRoad(6800, 24)
    asphalt_weight = 22 * 6 * p._length * p._width
    print(f"Расчётная масса асфальта для новой дороги {p._width} на {p._length} м - {asphalt_weight * 0.001:.3f} т")
