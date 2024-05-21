# Housing in mexico

house_0_list = [ 255000, 185, 3]    #This is an observation of an individual house in Mexico 
print(type(house_0_list))

print(house_0_list[0]/house_0_list[1])  #This is Price per square meter of house


house_nested_list = [        #This is a LIST of LISTS having observations of the houses in Mexico parameters being price, Sq Mtrs, BHK's!
    [115910.26, 128.0, 4.0], #these each sub list are now called as the ROW of the Tabular Data
    [48718.17, 210.0, 3.0],
    [28977.56, 58.0, 2.0],
    [36932.27, 79.0, 3.0],
    [83903.51, 111.0, 3.0],
]

print(len(house_nested_list))

# After having so many observations, we can now automate the price/sq mtr of the floor area.
for H in house_nested_list:
    price_m2 = H[0] / H[1]
    H.append(price_m2)
    print(H)



#Lists are a good way to organize data, but one drawback is that we can only represent values. 
#Why is that a problem? For example, someone looking at `[115910.26, 128.0, 4]` wouldn't know which values corresponded to price, area, etc. 
#A better option might be a [**dictionary**]

house_0_dict = {
    "Price_House": 1152036,
    "area": 185,
    "BHK's":4
}

print(house_0_dict)

house_0_dict["price_sqmtr"] = house_0_dict["Price_House"] / house_0_dict["area"]
print(house_0_dict)

#Since it was done for an individule house, no wwe do it for more than 1 house and automate it
house_0_dict = [
{
    "Price_House": 1152036,
    "area": 185,
    "BHK's":4
},
{   
    "Price_House": 2500000,
    "area": 195,
    "BHK's":4
},
{
   "Price_House": 5000000,
    "area": 200,
    "BHK's":4
},
{
   "Price_House": 1500000,
    "area": 150,
    "BHK's":3
},
{   "Price_House": 1000000,
    "area": 125,
    "BHK's":2
}]

print(house_0_dict)

for house in house_0_dict:              #useed for loop to iterate the price per sqmeteres calculation
    house ["price_per_m2"] = house["Price_House"] / house["area"]
    print(house_0_dict)


#There's a difference between normal / regular for loop and dictionary for loop, 
#1. In regular For loop, we do not use 'house' when using conditions intead provide a key. 
#2. While in Dictionary For loop, we use house to specify where exactly the key should go.
#3. Lastly, print it out for the results


#lets calculate the mean price for the houses at Mexico!

mean_price = []     #This line initializes an empty list called mean_price. This list will be used to store the prices of the houses.

#The for loop is intended to iterate over the houses in house_0_dict. 
#However, this can be writtern in another way here because house_0_dict is a dictionary of dictionaries, and iterating over a dictionary as "for house in house_0_dict:""

for house in house_0_dict.values():
    mean_price.append(house["Price_House"])
    print(mean_price)

house_mean_price = sum(mean_price) / len(mean_price)
print(house_mean_price)
