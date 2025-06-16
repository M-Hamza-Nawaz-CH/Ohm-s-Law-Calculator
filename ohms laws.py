def ohms_law_calculator():
    print("🔌 Ohm’s Law Calculator")
    print("Choose what you want to calculate:")
    print("1. Voltage (V)")
    print("2. Current (I)")
    print("3. Resistance (R)")

    choice = input("Enter 1, 2, or 3: ")

    if choice == '1':
        I = float(input("Enter Current (I) in Amperes: "))
        R = float(input("Enter Resistance (R) in Ohms: "))
        V = I * R
        print(f"Voltage (V) = {V:.2f} Volts")

    elif choice == '2':
        V = float(input("Enter Voltage (V) in Volts: "))
        R = float(input("Enter Resistance (R) in Ohms: "))
        if R == 0:
            print("Resistance cannot be zero.")
            return
        I = V / R
        print(f"Current (I) = {I:.2f} Amperes")

    elif choice == '3':
        V = float(input("Enter Voltage (V) in Volts: "))
        I = float(input("Enter Current (I) in Amperes: "))
        if I == 0:
            print("Current cannot be zero.")
            return
        R = V / I
        print(f"Resistance (R) = {R:.2f} Ohms")

    else:
        print("Invalid choice. Please select 1, 2, or 3.")

# Run the calculator
ohms_law_calculator()
