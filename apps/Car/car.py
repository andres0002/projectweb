class Car():
    def __init__(self, request):
        self.request=request
        self.session=request.session
        car=self.session.get('car')
        if (not car):
            car=self.session['car']={}
        self.car=car

    def add(self, product):
        if (str(product.id) not in self.car.keys()):
            self.car[product.id]={
                'id': product.id,
                'name': product.nameProduct,
                'price': float(product.priceProduct),
                'amount': 1,
                'image': product.imageProduct.url
            }
        else:
            for key, value in self.car.items():
                if (key==str(product.id)):
                    value['amount'] += 1
                    value['price'] += product.priceProduct
                    break
        self.save_car()

    def save_car(self):
        self.session['car']=self.car
        self.session.modified=True

    def delete(self, product):
        id=str(product.id)
        if (id in self.car):
            del self.car[id]
            self.save_car()

    def substract_product(self, product):
        for key, value in self.car.items():
            if (key==str(product.id)):
                value['amount'] -= 1
                value['price'] -= product.priceProduct
                if (value['amount'] < 1):
                    self.delete(product)
                break
        self.save_car()

    def clean_car(self):
        self.session['car']={}
        self.session.modified=True
