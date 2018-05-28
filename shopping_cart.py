# michelle cronin
# list of products
products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

product_ids = []

# while loop to obtain user iput
while True:
# make input uppercase in case user types lowercase
    product_id = input("Please input a product identifier or type DONE if there are no other items: ").upper()
    if product_id == "DONE":
      break
# user input is a string, so we need to match product id as a string (from products list) against user's input of a product id (already a string)
    elif [p for p in products if str(p["id"]) == product_id]:
# if product id is valid, it gets added to our products_id list
      product_ids.append(product_id)
# if product id is not valid, user is told so; then loop starts up again asking for user input
    else:
      print("Invalid Entry. Try again below.")

# import datetime library so we can use current date and time
import datetime
now = datetime.datetime.now()

# print beginning of receipt
print("\n\n------------------")
print("Thanks for shopping at BUBBLES GROCERY!")
print("----------")
# add current time info
print(now.strftime("Phone: 555-555-5555 \nWeb: http://bubbles-grocery.net \nCheckout Time: %A %B %d, %Y at %I:%M:%S %p"))
print("----------")

# function --> calculate tax
def tax_owed(price):
  ny_tax = .08875
  return price * ny_tax

#function --> return product names from each dict within list
# ?? can't get it to print though...
def sort_by_name(product):
  return product["name"]

price_tracker = 0
matching_products_list = []

for pid in product_ids:
# make user inputs of product ids int for comparison purposes
# ?? maybe can do this sooner; integrate with validation check?
    matching_product = [p for p in products if p["id"] == int(pid)]
# avoid adding list to a list; this way you add the dict details
    matching_product = matching_product[0]
# adds individual dict as individual items in list
    matching_products_list.append(matching_product)
    price_tracker += matching_product["price"]

# sort matching products alphabetically by name
matching_products_list = sorted(matching_products_list, key=sort_by_name)

print("YOU PURCHASED THE FOLLOWING ITEMS: ")
for p in matching_products_list:
  print("+ {0} (${1:.2f})".format(p["name"], p["price"]))

print("----------")
print("Total price: ${0:.2f}.".format(price_tracker))
print("Added NYC Sales Tax (8.875%): ${0:.2f}.".format(tax_owed(price_tracker)))
print("TOTAL AMOUNT OWED: ${0:.2f}.".format(price_tracker + tax_owed(price_tracker)))
print("----------")
print("We value our customers and hope you return soon to BUBBLES GROCERY!")
print("------------------")
