from replit import clear

menus = {
  "espresso": {
    "ingredients": {
      "water": 50,
      "coffee": 18,
    },
    "cost": 499.9,
  },
    "latte": {
    "ingredients": {
      "water": 200,
      "milk": 200,
      "coffee": 24,
    },
    "cost": 749.9,
  },
    "capuccino": {
    "ingredients": {
      "water": 200,
      "milk": 150,
      "coffee": 24,
    },
    "cost": 799.9,
  },
}

resources = {
  "water": 500,
  "milk": 400,
  "coffee": 600,
}

def drinks(coffee):
  espressos = menus["espresso"]["ingredients"]
  lattes = menus["latte"]["ingredients"]
  capuccinos = menus["capuccino"]["ingredients"]
  if coffee == "espresso":
    return espressos
  elif coffee == "latte":
    return lattes
  elif coffee == "capuccino":
    return capuccinos
  else:
    return "coffee not available"

def available_resources(ingredients, resources):
  for item in ingredients:
    ingredient_ = ingredients[item]
    if ingredient_ > resources[item]:
      return "sorry not enough resources"
    else:
      return "your coffee is being processed"

def make_payment(payment, paid):
  amount_ = payment
  if paid > amount_:
    return "payment successful"
  else:
    return "payment not successful"

def make_coffee():
  is_on = True
  profit = 0
  
  while is_on:
    choice = input('choose coffee: espresso, Latte or capuccino?:').lower()
    user = input("do you want to print report, yes or no?: ")
    if choice == "off":
      is_on = False
    elif user == "report":
        for resource, mil in resources.items():
          print(f"{resource}: {mil}ml")
    else:
      print(f"i am having {choice}")
      coffee_choice = drinks(choice)
      print(f"Your {choice} will be made with: {coffee_choice}")
      is_available = available_resources(coffee_choice, resources)
      print(is_available)
      if not is_available:
        is_on = False
      else:
        payment = float(input(f"how much are you paying for {choice}? "))
        paid = make_payment(menus[choice]["cost"], payment)
        profit_ = round(payment - menus[choice]["cost"])
        if not paid:
          profit = profit
        else:
          profit += profit_
        print(paid)
        print(f"your profit is {profit}")   
make_coffee()