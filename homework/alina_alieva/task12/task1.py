class BotanicalFlower:
    def __init__(self, name, price, life, fresh, color, size):
        self.name = name
        self.price = price
        self.life = life
        self.fresh = fresh
        self.color = color
        self.size = size


class Rosa(BotanicalFlower):
    color = 'red'


class Lavanda(BotanicalFlower):
    color = 'blue'



class Buket:
    list_flowers = []

    def price(self):
        result = 0
        for flower in self.list_flowers:
            result += flower.price
        return result

    def add_flower(self, flower):
        self.list_flowers.append(flower)

    def lifetime(self):
        timeres = 0
        for flower in self.list_flowers:
            timeres += flower.life
            result = timeres / len(self.list_flowers)
        return result

    def sort_by(self, attribute):
        self.list_flowers.sort(key=lambda flower: getattr(flower, attribute))
        for flower in self.list_flowers:
            print(f"{flower.name} | {flower.price} | {flower.life} | {flower.fresh} | {flower.color} | {flower.size}")

    def searching(self, attribute, value):
        search = list(filter(lambda flower: getattr(flower, attribute) == value, self.list_flowers))
        for flower in search:
            print(f"{flower.name} | {attribute}: {value}")
        return search


rosa = Rosa("Rose", 1, 3, 'True', 'red', 30)
rosa2 = Rosa("Rosa Peon", 3, 3, 'red', 'red', 15)
lavanda = Lavanda("Lavanda",2, 2, 'blue', 'red', 1)

rBuket = Buket()
rBuket.add_flower(rosa)
rBuket.add_flower(rosa2)
rBuket.add_flower(lavanda)


print(rBuket.price())
print(rBuket.lifetime())
rBuket.sort_by('life')
print("-------")
rBuket.sort_by('fresh')
print("-------")
rBuket.searching("price", 1)
