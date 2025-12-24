
prices_catalog = {'yellow':80,
                  'red':75,
                  'green':100,
                  'blue':150}

# Create list of colors for indexing
colors_list = list(prices_catalog.keys())

# Create display string
color_options = ", ".join([f"{i+1}- {color}" for i, color in enumerate(colors_list)])

# Get user input
user_input = int(input(f"Choose color: {color_options}: "))  # Convert to int
user_amount = int(input("insert cloths amount: "))

# Index the colors_list, not color_options
selected_color = colors_list[user_input - 1]

print(f'color: {selected_color}')
print(f'price per item: {prices_catalog[selected_color]}')
print(f'total price: {prices_catalog[selected_color] * user_amount}')