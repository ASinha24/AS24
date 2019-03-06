import random

class coin:
    def __init__ (self, rare=False, clean=True, heads=True, **kwargs):
        for key, value in kwargs.items():
            setattr(self,key,value)#equal to self.original_value=1
        self.is_rare=rare
        self.is_clean=clean
        self.heads=heads
            

        if self.is_rare:
            self.value=self.original_value*1.25
        else:
            self.value=self.original_value

        if self.is_clean:
            self.colour=self.clean_colour
        else:
            self.colour=self.rusty_colour

    def rust(self):
        self.colour=self.rusty_colour

    def clean(self):
        self.colour=self.clean_colour

    def __del__ (self):
        print("coin spent")

    def flip(self):
        choice=random.choice([True,False])
        self.heads=choice


class Pound(coin):
    def __init__(self):
        data={
            "original_value":1.00,
            "clean_colour":"gold",
            "rusty_colour":"greenish",
            "num_edges":1,
            "diameter":22.5,
            "thickness":3.15,
            "mass":9.5,
            
            }
        super().__init__(**data)
    
    
