class food:
    def __init__(self, food, amount) :
        self.__foodname = food
        self.__amountinpounds = amount
        self.__standardpriceperpound = 0.00
        self.__calculate_price()

    def __calculate_price(self) :
        self.__Pricelist()

    def __Pricelist(self):
        if self.foodname == "Dry Cured Iberian Ham":
            self.__standardpriceperpound = 177.80
        elif self.foodname == "Wagyu Steaks":
            self.__standardpriceperpound = 450.00
        elif self.foodname == "Matsutake Mushrooms":
            self.__standardpriceperpound = 272.00
        elif self.foodname == "Kopi Luwak Coffee":
            self.__standardpriceperpound = 306.50
        elif self.foodname == "Moose Cheese":
            self.__standardpriceperpound = 487.20
        elif self.foodname == "White Truffles":
            self.__standardpriceperpound = 3600.00
        elif self.foodname == "Blue Fin Tuna":
            self.__standardpriceperpound = 3603.00
        elif self.foodname == "Le Bonnotte Potatoes":
            self.__standardpriceperpound = 270.81
        else: #item not on list
            self.__standardpriceperpound = 0.00
    
    def calculatecost_JS(self):
        return self.__standardpriceperpound * self.__amountinpounds

    def getfoodname_JS(self):
        return self.__foodname
    
    def getamountinpounds_JS(self):
        return self.__amountinpounds

    def getstandardpriceperpound_JS(self):
        return self.__standardpriceperpound

    def __str__(self):
        return f"Item: {self._food_name}\nAmount ordered: {self._amount_in_pounds:.1f} pounds\n" \
               f"Price per pound: ${self._standard_price_per_pound:.2f}\n" \
               f"Price of order: ${self.calculate_cost_JS():.2f}"



