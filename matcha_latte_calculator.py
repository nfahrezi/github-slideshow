"""Simple calculator for matcha latte water and milk amounts."""


def main() -> None:
    print("Matcha Latte Ratio Calculator")
    print("We'll use a 1:4:8 ratio (matcha : 80°C water : milk).")

    while True:
        user_input = input("How many grams of matcha powder do you have? ").strip()
        try:
            matcha_grams = float(user_input)
            if matcha_grams <= 0:
                print("Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number, such as 2 or 2.5.")

    water_ml = matcha_grams * 4
    milk_ml = matcha_grams * 8

    print("\nFor a balanced matcha latte:")
    print(f"- 80°C water: {water_ml:.1f} ml")
    print(f"- Milk: {milk_ml:.1f} ml")


if __name__ == "__main__":
    main()
