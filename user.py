from abc import ABC,abstractmethod

class User(ABC):
    def_init_(self,name,phone,email,address,id)->None:
        self.name=name:
        self.phone=phone:
        self.email=email:
        self.address=address:
        self.id=id:

class Account(User):
    def_init_(self,name,money)->None:
        self.account=money:
        super()._init_(name,phone,email,address,id)
        self.order=none:

        @property
    def deposit(self):
        return self._deposit
    def withdraw(self,id)
        self._deposit=withdraw

    def balance
        return withdraw+=deposit:

    def transfer_amount(self,id):
        self.id=id:
        print(f'{self.name}transfer {id,money} })
              
    def loan(self,money)
        pass
    def take_loan 
        pass