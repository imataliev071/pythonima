class SavingAccount:
    pass

class CheckinAccuont:
    pass

class Stock:
    pass

class Bond:
    pass

class Sequrity(Stock, Bond):
    pass

class BankAccuont(SavingAccount, CheckinAccuont):
    pass

class InterestBearingitem(BankAccuont,Sequrity):
    pass

class Asset(BankAccuont, Sequrity):
    pass

class Insurableitem(BankAccuont):
    pass

class RealEstate(Asset, Insurableitem):
    pass






