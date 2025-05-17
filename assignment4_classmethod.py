class Bank:
    bank_name = "OldBank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

b1 = Bank()
b2 = Bank()
print("Before:", b1.bank_name)
Bank.change_bank_name("NewBank")
print("After:", b2.bank_name)