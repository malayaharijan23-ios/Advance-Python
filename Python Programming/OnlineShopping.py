products = {
    "phone": 20000,
    "laptop": 50000,
    "watch": 5000,
    "earbuds": 1000,
    "tablet": 15000,
    "camera": 25000,
    "headphones": 3000
}
cart={}
def view_products():
    print("\nAvailable Products:")
    for item, price in products.items():
        print(item,"-Rs",price)
def add_to_cart():
    item=input("Enter product name: ").lower()
    if item in products:
        qty= int(input("Enter quantity: "))
        cart[item] = (products[item], qty)
        print(item, "added to cart")
    else:
        print("Product not available")
def remove_item():
    item = input("Enter item to remove: ").lower()
    if item in cart:
        del cart[item]
        print(item, "removed from cart")
    else:
        print("Item not in cart")
def generate_receipt(total):
    print("\nRECEIPT")
    for item, data in cart.items():
        price = data[0]
        qty = data[1]
        subtotal = price * qty
        print(item, "| Qty:", qty, "| Rs", subtotal)
    print("Total Amount = Rs", total)
    print("Thank You for Shopping!")
def checkout():
    if not cart:
        print("Cart is empty")
        return
    total = 0
    for price, qty in cart.values():
        total += price * qty
    generate_receipt(total)
while True:
    print("\n1.View Products")
    print("2.Add to Cart")
    print("3.Remove Item")
    print("4.Checkout")
    print("5.Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        view_products()
    elif choice == "2":
        add_to_cart()
    elif choice == "3":
        remove_item()
    elif choice == "4":
        checkout()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid Choice")