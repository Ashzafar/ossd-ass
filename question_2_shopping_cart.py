# written by Ashir Mehmood oss v1

class Product:
    def __init__(self):
        # dummy data instead of db fetch
        self.products = {
            "laptops": {
                1: ["phsical product", "HP 840 G series", 90000, 10],
                2: ["phsical product", "HP 850 G series", 100000, 10],
                3: ["phsical product", "Dell 7400 series", 85000, 10]
            },
            "bikes": {
                1: ["physical product", "honda 150cc", 200000, 10]
            },
            "pens": {
                1: ["physical prodcuct", "piano 0.7mm", 100, 50]
            },
            "game passes": {
                1: ["digital product", "xbox gaming monthly", 10000, 100]
            },
            "daraz vouchers": {
                1: ["digital product", "daraz-recharge", 5000, 100]
            },
            "notepads": {
                1: ["physical product", "al-kitab", 1000, 100]
            },
            "bags": {
                1: ["physical product", "black medium backpack", 1500, 100]
            }
        }

    # def log(self):  # every method needs a parameter, in case none needed, pass "self"
        # print(self.products["laptop"][2])  # one has to give name of key then
        # index of "key:tuple" pair element

    def set_total_price(self, total_price):
        self.total = total_price


class PhysicalProduct(Product):
    def __init__(self):
        self.total = 0


    def set_total_price(self, total_price):
        self.total = total_price


class DigitalProduct(Product):
    def __init__(self):
        self.total = 0

    def set_total_price(self, total_price):
        self.total = total_price


class ShoppingCart():
    def __init__(self, p):
        self.total_price = None
        self.item_list = None
        self.cart = []
        self.p = p
        self.prod_price = 0
        self.total = 0
        self.name = None

        self.p_product = PhysicalProduct()
        self.d_product = DigitalProduct()


    def add_item(self, key1):
        my_list = self.p.products[key1]
        print(my_list, "\n")
        item = int(input())

        if my_list[item][3] > 0:
            self.cart.append(my_list[item])  # try to access dict's dict's key
            self.p.stock = my_list[item][3]
            self.p.stock -= 1
            my_list[item][3] = self.p.stock  # supposed to do db query

            if my_list[item][0] == "physical product":
                self.prod_price += my_list[item][2]  # price updation
                self.p_product.set_total_price(self.prod_price)
                self.total += my_list[item][2]
            else:
                self.prod_price += my_list[item][2]  # price updation
                self.d_product.set_total_price(self.prod_price)
                self.total += my_list[item][2]

        else:
            print("OUT OF STOCK")


    def delete_item(self):
        if self.cart.len() == 0:
            exit()
        else:
            for i in range(1):
                print(*self.cart)
            opt = int(input("delete: "))
            for i in self.p.products:
                if self.p.products[i][1] == self.cart[opt][1]:
                    self.p.product[i][3] += 1
            self.total -= self.cart[opt][2]
            self.cart.pop(opt)


    def set_name(self, name):
        self.name = name


    def get_name(self):
        print(self.name)


    def view_cart(self):
        print(
            '\n',
            self.name,
            '\n total price:',
            self.total,
            '\n items:',
            self.cart)


def __main__():
    p = Product()
    sc = ShoppingCart(p)
    cust_name = input("Enter customer's name: ")
    sc.set_name(cust_name)

    while (True):
        opt = int(input("1.ADD, 2.DELETE, 3.VIEW: "))

        match opt:
            case 1:
                selection = int(input(
                    "This is your shopping cart, choose items to buy: 1.laptops 2.bikes 3.pens 4.game passes 5.daraz recharge 6.bags\n"))

                match selection:
                    case 1:
                        key = "laptops"
                        sc.add_item(key)

                    case 2:
                        key = "bikes"
                        sc.add_item(key)
                    case 3:
                        key = "pens"
                        sc.add_item(key)
                    case 4:
                        key = "game passes"
                        sc.add_item(key)
                    case 5:
                        key = "daraz vouchers"
                        sc.add_item(key)
                    case 6:
                        key = "notepads"
                        sc.add_item(key)
                    case 6:
                        key = "bags"
                        sc.add_item(key)
            case 2:
                sc.delete_item()
            case 3:
                sc.view_cart()


if __name__ == "__main__":
    __main__()
