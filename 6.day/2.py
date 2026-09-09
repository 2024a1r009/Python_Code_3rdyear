cp="2345"
while True:
    pin=input("Enter 4-digit Pin:")

    if len(pin)!=4:
        print("PIN must be exactly 4 digit")
        continue

    if pin==cp:
        print("Lock opned")
        break
    else:
        print("No")