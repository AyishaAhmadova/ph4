class ŞahmatDasi:
    def __init__(self, rəng):
        self.rəng = rəng

    def hərəkət(self):
        pass

class Şah(ŞahmatDasi):
    def hərəkət(self):
        print("Şah hərəkət etdi.")

class Vəzir(ŞahmatDasi):
    def hərəkət(self):
        print("Vəzir hərəkət etdi.")

class At(ŞahmatDasi):
    def hərəkət(self):
        print("At hərəkət etdi.")

class Taxta:
    def __init__(self):
        self.parçalar = []

    def parça_əlavə_et(self, parça):
        self.parçalar.append(parça)

    def bütün_parçaları_hərəkət_et(self):
        for parça in self.parçalar:
            parça.hərəkət()

taxta = Taxta()
taxta.parça_əlavə_et(Şah("Ağ"))
taxta.parça_əlavə_et(Vəzir("Siyah"))
taxta.parça_əlavə_et(At("Ağ"))
taxta.bütün_parçaları_hərəkət_et()
