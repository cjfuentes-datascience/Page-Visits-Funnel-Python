import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

#Inspect the DataFrames using print and head
print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

# Combine visits and cart using a left merge.
cart_visits = pd.merge(visits, cart, how='left')
print(cart_visits.head())

# How long is your merged DataFrame?
all_visits = len(cart_visits)
print('Length of cart-visits: ' + str(all_visits))

# How many of the timestamps are null for the column cart_time?
empty_cart = len(cart_visits[cart_visits.cart_time.isnull()])
print('Length of empty-carts: ' + str(empty_cart))

# What percent of users who visited Cool T-Shirts Inc. ended up not placing a t-shirt in their cart?
no_cart = empty_cart / all_visits * 100
print('Percentage of users who did not place a t-shirt in their cart:' + ' ' + str(no_cart) + '%')

# Repeat the left merge for cart and checkout and count null values. What percentage of users put items in their cart, but did not proceed to checkout?
cart_checkout = pd.merge(cart, checkout, how='left')
print(cart_checkout.head())
all_cart = len(cart_checkout)
print('Length of cart-checkouts: ' +  str(all_cart))
no_checkout = len(cart_checkout[cart_checkout.checkout_time.isnull()])
print('Length of no-checkouts: ' + str(no_checkout))
print('Percentage of users who did not proceed to checkout: ' + str(no_checkout / all_cart * 100) + '%')

# Merge all four steps of the funnel, in order, using a series of left merges.
all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')
print(all_data.head())
len_all_data = len(all_data)
no_purchase = len(all_data[all_data.purchase_time.isnull()])

# What percentage of users proceeded to checkout, but did not purchase a t-shirt?
print('Percentage of users who did not purchase a t-shirt: ' + str(no_purchase / len_all_data * 100) + '%')

# Which step of the funnel is weakest (i.e., has the highest percentage of users not completing it)?
print('The weakest funnel is cart-visits at ' + str(no_cart) + '%')

# Using the giant merged DataFrame all_data that you created, let’s calculate the average time from initial visit to final purchase. Add a column that is the difference between purchase_time and visit_time.
all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time

# Examine the results by printing the new column to the screen.
print(all_data.time_to_purchase.head())

#Calculate the average time to purchase by applying the .mean() function to your new column.
print(all_data.time_to_purchase.mean())
