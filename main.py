def pricing_calc():
    while True:
        try:
            cost_price = float(input("Enter cost price: "))
            if cost_price >0:
                break
            else:
                print("Error! Cost price must be greater then 0.")
        except ValueError:
            print("Error! Please enter a valid number (use dot for decimals).")
        
    if cost_price <10:
        sales_price = (cost_price / 100)*170
    elif 10 <= cost_price <30:
        sales_price = (cost_price / 100)*150
    elif 30 <= cost_price <50:
        sales_price = (cost_price / 100)*140
    elif cost_price >= 50:
        sales_price = (cost_price / 100)*130
    
    print(f"\n--> Sale price is: {sales_price:.2f}")
    
pricing_calc()