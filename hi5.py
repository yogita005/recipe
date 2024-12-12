import os
import requests
import streamlit as st
import os

class SpoonacularRecipeRecommender:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.spoonacular.com/recipes"

    def find_by_ingredients(self, ingredients, number=10, ranking=1, ignore_pantry=True):
        endpoint = f"{self.base_url}/findByIngredients"
        params = {
            "apiKey": self.api_key,
            "ingredients": ingredients,
            "number": number,
            "ranking": ranking,
            "ignorePantry": ignore_pantry
        }
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            st.error(f"API Request Error: {e}")
            return []

    def get_recipe_details(self, recipe_id):
        endpoint = f"{self.base_url}/{recipe_id}/information"
        params = {
            "apiKey": self.api_key,
            "includeNutrition": True
        }
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            st.error(f"API Request Error: {e}")
            return None

def main():
    st.set_page_config(page_title="Ingredient Recipe Finder", page_icon="🍴")

 
    st.title("🍳 Spoonacular Recipe Recommender")

    api_key = os.getenv("SPOONACULAR_API_KEY")
    if not api_key:
        st.error("API Key not found. Please set the SPOONACULAR_API_KEY environment variable.")
        return

    if 'ingredients' not in st.session_state:
        st.session_state.ingredients = []

  
    st.header("🥬 Find Recipes by Ingredients")

    new_ingredient = st.text_input(
        "Enter an ingredient", placeholder="e.g. chicken"
    )
    
    if st.button("Add Ingredient"):
        if new_ingredient:
            st.session_state.ingredients.append(new_ingredient)

    st.write("### Ingredients List")
    if st.session_state.ingredients:
        for i, ingredient in enumerate(st.session_state.ingredients):
            st.write(f"{i + 1}. {ingredient}")
    else:
        st.info("No ingredients added yet.")

    # Number of recipes slider
    number_of_recipes = st.sidebar.slider("Number of Recipes to Show", min_value=1, max_value=20, value=10)

    # Search button
    if st.button("Find Recipes") and st.session_state.ingredients:
        # Initialize recommender
        recommender = SpoonacularRecipeRecommender(api_key)

        # Find recipes
        try:
            ingredients_string = ",".join(st.session_state.ingredients)
            recipes = recommender.find_by_ingredients(
                ingredients_string, 
                number=number_of_recipes
            )

            # Display results
            if recipes:
                st.header("🍽️ Recommended Recipes")

                # Create columns for recipe cards
                cols = st.columns(3)
                
                for i, recipe in enumerate(recipes):
                    col = cols[i % 3]

                    with col:
                        # Display recipe card
                        st.image(recipe['image'], use_column_width=True)
                        st.subheader(recipe['title'])

                        used_ingredients = ', '.join(
                            [ing['name'] for ing in recipe.get('usedIngredients', [])]
                        )
                        missed_ingredients = ', '.join(
                            [ing['name'] for ing in recipe.get('missedIngredients', [])]
                        )

                        with st.expander("Recipe Details"):
                            st.write(f"**Used Ingredients:** {used_ingredients}")
                            st.write(f"**Missing Ingredients:** {missed_ingredients}")

                            with st.spinner('Fetching recipe details...'):
                                details = recommender.get_recipe_details(recipe['id'])

                                if details:
                                    st.write(f"**Cooking Time:** {details.get('readyInMinutes', 'N/A')} minutes")
                                    st.write(f"**Servings:** {details.get('servings', 'N/A')}")

                                    st.subheader("Full Ingredients")
                                    for ing in details.get('extendedIngredients', []):
                                        st.write(f"- {ing['original']}")

                                    st.markdown(f"[View Full Recipe]({details.get('sourceUrl', '#')})")

            else:
                st.warning("No recipes found matching your ingredients.")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
