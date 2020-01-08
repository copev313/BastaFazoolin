#Basta Fazoolin' Project
#Created as part of Codecademy - Classes Project
#By: E.Cope
#Date: Jan 2020


class Menu:
  
  def __init__(self, name, items, start, end):
    self.name = name
    self.items = items
    self.start_time = start
    self.end_time = end
  
  def __repr__(self):
    return "%s Menu: Available %s:00 - %s:00" %(self.name, self.start_time, self.end_time)
  
  def calculate_bill(self, food_ordered):
    bill = 0
    for food in food_ordered:
      bill += self.items[food]
    
    return bill
    

brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

brunch = Menu("Brunch", brunch_items, 11, 16)

early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

early_bird = Menu("Early-Bird", early_bird_items, 15, 18)

dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

dinner = Menu("Dinner", dinner_items, 17, 23)

kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

kids = Menu("Kids", kids_items, 11, 21)

#step8
print(brunch)
#10
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
#11
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))


class Franchise:
  
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
    
  def __repr__(self):
    return self.address
  
  def available_menus(self, time):
    for menu in self.menus:
      if (time > menu.start_time and time < menu.end_time):
        return menu

      
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

#17
print(flagship_store.available_menus(12))

#18
print(flagship_store.available_menus(17))

#19
class Business:
  
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

    
new_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu("Take a\' Arepa", new_items, 10, 20)

#23
arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)


#21
basta = Business('\'Basta Fazoolin\'with my Heart', [flagship_store, new_installment])

new_business = Business('Take a\' Arepa', arepas_place)
