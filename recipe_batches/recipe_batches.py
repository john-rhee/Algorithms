#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  recipe_values = [*recipe.values()]
  ingredients_values = [*ingredients.values()]
  possible=[]
  for i in range(0, len(recipe_values)):
    if recipe_values[i]>ingredients_values[i]:
      possible.append('cant')
    else:
      possible.append('can')
  if 'cant' in possible:
    print('You cannot make it because you dont have enough ingredients')
  else:
    print('You can make it because you have enough ingredients')  

          
recipe_batches({ 'milk': 100, 'butter': 50, 'flour': 5 },
  { 'milk': 138, 'butter': 60, 'flour': 51 })

# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))