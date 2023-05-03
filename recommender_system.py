import streamlit as st
import pandas as pd
import numpy as np
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.model_selection import train_test_split

# Loading the dataset
df = pd.read_csv("IndianFoodRecipesDataset.csv")

# Vectorizing the ingredients
tfidf = TfidfVectorizer(stop_words="english")
df['TranslatedIngredients'] = df['TranslatedIngredients'].fillna("")
tfidf_matrix = tfidf.fit_transform(df['TranslatedIngredients'])

# Cosine similarity measure
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(df.index, index=df['TranslatedRecipeName'].str.lower()).drop_duplicates()

# Recommendation function
def get_recommendations(TranslatedRecipeName, cosine_sim=cosine_sim):
    idx = indices[indices.index.str.contains(TranslatedRecipeName, case=False)].values
    if len(idx) == 0:
        return None
    else:
        sim_scores = list(enumerate(cosine_sim[idx[0]]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:6]
        sim_index = [i[0] for i in sim_scores]
        return list(df['TranslatedRecipeName'].iloc[sim_index])

# Initializing the page
def app():
    st.title(':shallow_pan_of_food: Recipe Recommender System')
    st.write('Enter the recipes you have:')
    # text box to take input recipes
    recipes = st.text_input('For example : Spicy Tomato Rice')
    if not recipes:
        st.warning('Please enter some recipes.')
    else:
        recommended_recipes = get_recommendations(recipes)
        # Displays the recipe details
        if recommended_recipes:
            st.write('Recommended Recipes:')
            for recipe_name in recommended_recipes:
                recipe = df[df['TranslatedRecipeName'] == recipe_name].iloc[0]
                st.write('**Recipe Name:**', recipe['TranslatedRecipeName'])
                st.write('**Ingredients:**', recipe['TranslatedIngredients'])
                st.write('**Instructions:**', recipe['TranslatedInstructions'])
                st.write('**URL:**', recipe['URL'])
                
                st.write('---')
            
            # Saving input and output to CSV
            data = pd.DataFrame({
                'Input Recipe': [recipes],
                'Recommended Recipes': [', '.join(recommended_recipes)]
            })
            
            # Creating the csv file
            if not os.path.exists('recommendations.csv'):
                data.to_csv('recommendations.csv', index=False)
            else:
                data.to_csv('recommendations.csv', mode='a', header=False, index=False)
        else:
            st.warning('No recipes found with the given ingredients. Please try again with different ingredients.')
