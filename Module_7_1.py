class Product:
    def __init__(self,name,weigth,category):
        self.name = name
        self.weigth = weigth
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weigth}, {self.category}'

class Shop:
    #def __str__(self):
     #   return f'{}'
    __file_name = 'products.txt'
    def get_products(self):
        product_str = open(self.__file_name,'r')
        x = (product_str.read())
        product_str.close()
        return f'{x}'

    def add(self, *products):
        for i in products:
            self.add = open(self.__file_name, 'a')
            if i.name in self.get_products():
                print(f'Продукт {i.name} уже есть в магазине')
            else:
                self.add.write(f'{i}\n')
                self.add.close()
        self.add.close()



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())