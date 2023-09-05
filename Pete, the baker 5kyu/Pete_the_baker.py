# My solution
def cakes(recipe, available):
    max_number_of_cakes = -1
    for product in recipe:
        if product in available:
            amount = available[product] // recipe[product]
            max_number_of_cakes = amount if max_number_of_cakes >= amount or max_number_of_cakes == -1 else max_number_of_cakes
        else:
            return 0

    return max_number_of_cakes


# Solution from Codewars
# This solution create list of possible cake by ingredient and then get min value from list 
def cakes2(recipe, available):
    return min([available[i]//recipe[i] if i in available else 0 for i in recipe])


if __name__=='__main__':
    print('Maximum:', cakes2({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 5000, "sugar": 599, "eggs": 5, "milk": 200}))
    print('Maximum:', cakes2({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000, "milk": 2000}))