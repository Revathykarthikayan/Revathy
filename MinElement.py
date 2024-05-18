def get_rated_list():
    rated_list = []
    # List of items to be rated
    items = ['physics', 'chemistry', 'mathematics', 'language', 'english']
    
    # Loop to get ratings for each item
    for item in items:
        rating = float(input(f"Enter the rating for {item}: "))
        rated_list.append((item, rating))

    return rated_list
rated_list = get_rated_list()
print("Rated list entered by the user:")
for item, rating in rated_list:
    print(f"{item}: {rating}")
sort = sorted(rated_list)
result =min(sort)
print(" Minimum element in list is:",result)