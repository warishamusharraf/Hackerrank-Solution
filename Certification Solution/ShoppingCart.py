
class ShoppingCart():
    def __init__(self):
        self.list = []
       

    def add(self,items):
        self.list.append(items)
        
    def total(self):
        total=0
        for i in self.list:
         if isinstance(i, int):
             total+=i
        print(total)
          

employe=ShoppingCart()
employe.add("Warisha")
employe.add("khan")
employe.add(8000)
employe.add(8000)
employe.total()