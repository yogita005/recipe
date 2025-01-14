# Recipe Recommender
<img width="953" alt="image" src="https://github.com/user-attachments/assets/25512ae9-61f8-48c2-bc18-12f8157ea530" />
<img width="956" alt="image" src="https://github.com/user-attachments/assets/596705c3-2da9-41e7-a9c8-72197c843b0f" />


## Overview

The **Recipe Recommender** is a Streamlit app that allows users to find recipes based on a list of ingredients they have. By utilizing the Spoonacular API, the app suggests delicious recipes that match the provided ingredients, along with detailed cooking instructions, ingredients, and other helpful recipe information.

## Features

- **Ingredient-based Recipe Search**: Users can input ingredients and get recipe suggestions based on what they have.
- **Customizable Results**: Control the number of recipes shown (from 1 to 20).
- **Detailed Recipe Information**: View details like ingredients, cooking time, servings, and more.
- **Interactive UI**: Add ingredients, view results in a clean layout with expandable recipe details.

## Installation

### Prerequisites

Before using the app, you need to have:

- A valid **Spoonacular API Key**. You can get one from [Spoonacular API](https://spoonacular.com/food-api).
- Python 3.x installed.
- The following Python libraries installed:

```bash
pip install streamlit requests
```

### Setting up the API Key

1. Get your API Key from Spoonacular.
2. Set the API key as an environment variable.

#### On Windows (Command Prompt):
```bash
set SPOONACULAR_API_KEY=your_api_key_here
```

#### On macOS/Linux (Terminal):
```bash
export SPOONACULAR_API_KEY=your_api_key_here
```

Alternatively, you can manually input the API key in the code, but it’s better to keep it secure in an environment variable.

## Running the App

Once everything is set up, run the app using the following command:

```bash
streamlit run app.py
```

This will launch the app in your browser, and you can start using it to find recipes based on your ingredients.

## Usage

1. **Add Ingredients**: Enter an ingredient in the text input field and click "Add Ingredient". You can add multiple ingredients to the list.
2. **Search for Recipes**: After adding your ingredients, click the "Find Recipes" button. The app will fetch matching recipes from the Spoonacular API.
3. **Explore Recipes**: Browse through the recommended recipes, including details such as used and missing ingredients, cooking time, servings, and a link to the full recipe.
4. **Adjust Recipe Count**: Use the sidebar slider to adjust the number of recipes displayed (between 1 and 20).

## Contributing

If you'd like to contribute to the project, feel free to fork the repository, submit issues, or create pull requests.

## License

This project is open-source and available under the MIT License.

---

Feel free to adjust any parts of the README as needed!
