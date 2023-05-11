cost = float(input("Cost? $"))
weight_unit = float(input("1) Cost per lb (oz to lb) \n2) Cost per oz (lb to oz) \n"))

if weight_unit == 1:
    weight_amount = float(input("Weight in oz? "))
    converted_weight = weight_amount/16
    cost_per_lb = cost/converted_weight
    print(f"Your cost per lb is: {round(cost_per_lb, 2)}")
elif int(weight_unit) == 2:
    weight_amount = float(input("Weight in lb? "))
    converted_weight = weight_amount*16
    cost_per_oz = cost/converted_weight
    print(f"Your cost per oz is: {round(cost_per_oz, 2)}")







