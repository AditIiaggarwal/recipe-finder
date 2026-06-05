import requests

recipes = {
    "1": "Pizza",
    "2": "Burger",
    "3": "Noodles",
    "4": "Tacos",
    "5": "Pancakes"
}


print("\nRecipe Explorer")

print("1. Pizza")
print("2. Burger")
print("3. Noodles")
print("4. Tacos")
print("5. Pancakes")

choice = input("\nChoose a recipe (1-5): ")

if choice in recipes:

    recipe = recipes[choice]

    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={recipe}"

    response = requests.get(url)
    data = response.json()

    if data["meals"]:

        meal = data["meals"][0]

        print("\nRecipe Name:", meal["strMeal"])
        print("Category:", meal["strCategory"])
        print("Cuisine:", meal["strArea"])

        print("\nIngredients:")

        for i in range(1, 21):
            ingredient = meal[f"strIngredient{i}"]

            if ingredient and ingredient.strip():
                print("-", ingredient)

        print("\nInstructions:")
        print(meal["strInstructions"][:500] + "...")

        print("\nYouTube:")
        print(meal["strYoutube"])

    else:
        print("Recipe not found.")

else:
    print("Invalid choice.")