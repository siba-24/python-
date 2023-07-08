def calculate_water_bill(meterage, consumption_type):
    if meterage < 0:
        print("مصرف آب نمی‌تواند منفی باشد")
        return

    bill_amount = 0

    if consumption_type in ['H', 'h']:
        # مصرف خانگی
        block_size = meterage // 100
        bill_amount = block_size * 500

    elif consumption_type in ['I', 'i']:
        # مصرف صنعتی
        if meterage <= 4000000:
            block_size = meterage // 100
            bill_amount = block_size * 750 + (meterage * 0.00025)
        else:
            bill_amount = meterage * 0.00025

    elif consumption_type in ['E', 'e']:
        # مصرف تجاری
        if meterage <= 2000000:
            block_size = meterage // 1500
            bill_amount = block_size * 600 + (meterage * 0.00004)
        else:
            bill_amount = meterage * 0.00004

    print("مبلغ صورتحساب آب: ", bill_amount)

# مثال‌ها
calculate_water_bill(500, 'H')
calculate_water_bill(2500000, 'I')
calculate_water_bill(3000000, 'I')
calculate_water_bill(1500000, 'E')
calculate_water_bill(3000000, 'E')
calculate_water_bill(-100, 'H')

