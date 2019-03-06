import random

class Pound:
    def __init__(self,rare=False):
        self.rare=rare
        if self.rare:
            self.value=1.25
        else:
            self.value=1.00
        self.colour="gold"
        self.num_edges=1
        self.diameter=22.5
        self.thickness=3.15
        self.head=True

    def __del__(self):
        print("coin spent")

    def rust(self):
        self.colour="greenish"

    def clean(self):
        self.colour="gold"

    def flip(self):
        head_option=[True,False]
        choice=random.choice(head_option)
        self.head=choice

coin1=Pound()
print(coin1.value)
print(coin1.colour)
print(coin1.num_edges)
print(coin1.diameter)
print(coin1.thickness)
print(coin1.head)

coin2=Pound()
coin2.rust()
print(coin2.colour)
coin2.flip()
print(coin2.head)
coin1=Pound()
coin1=Pound()
coin2=Pound()
coin1=Pound()



