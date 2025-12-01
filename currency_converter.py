 # currency_converter.py

USD_TO_RAND = 18.45  # Example rate
RAND_TO_USD = 1 / USD_TO_RAND

def convert_usd_to_rand(amount):
    return amount * USD_TO_RAND

def convert_rand_to_usd(amount):
    return amount * RAND_TO_USD

def main():
    print("--- Currency Converter (USD ↔ ZAR) ---")
    amount = float(input("Enter amount: "))
    print("Convert:\n1. USD → ZAR\n2. ZAR → USD")
    choice = input("Select (1 or 2): ")

    if choice == "1":
        print(f"ZAR {convert_usd_to_rand(amount):.2f}")
    elif choice == "2":
        print(f"USD {convert_rand_to_usd(amount):.2f}")
    else:
        print("Invalid choice.")

if __name__ == "_main_":
    main()