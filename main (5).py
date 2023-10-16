def linear_search_product(product_list, target_product):
    indices = []
    for i in range(len(product_list)):
        if product_list[i] == target_product:
            indices.append(i)
    return indices

products = ["apple", "banana", "apple", "orange", "apple"]
target = "apple"
result = linear_search_product(products, target)

if not result:
    print("Product not found.")
else:
    print("Product found at indices:", end=" ")
    for index in result:
        print(index, end=" ")
    print()