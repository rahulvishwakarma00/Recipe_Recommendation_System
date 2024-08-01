from flask import render_template, request
from app import app
import pandas as pd
import pickle

# Load models and data
cosine_sim = pickle.load(open('data/cosine_sim.pkl', 'rb'))
df = pd.read_pickle('data/recipes_df.pkl')
svd = pickle.load(open('data/svd_model.pkl', 'rb'))

def get_content_based_recommendations(title, cosine_sim=cosine_sim):
    idx = df[df['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    recipe_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[recipe_indices].tolist()

def get_collaborative_recommendations(user_id, svd_model=svd, num_recommendations=10):
    user_ratings = pd.read_csv('data/ratings.csv')
    already_rated = user_ratings[user_ratings['user'] == user_id]['recipe'].tolist()
    all_recipes = df['title'].tolist()
    not_rated = [recipe for recipe in all_recipes if recipe not in already_rated]

    predictions = [svd_model.predict(user_id, recipe) for recipe in not_rated]
    predictions.sort(key=lambda x: x.est, reverse=True)
    top_predictions = predictions[:num_recommendations]
    recommended_recipes = [pred.iid for pred in top_predictions]
    return recommended_recipes

def hybrid_recommendation(user_id, recipe_title, top_n=10):
    content_recs = get_content_based_recommendations(recipe_title)
    collab_recs = get_collaborative_recommendations(user_id)

    hybrid_recs = list(set(content_recs + collab_recs))[:top_n]
    return hybrid_recs

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_id = request.form['user']
    recipe_name = request.form['recipe']
    recommendations = hybrid_recommendation(user_id, recipe_name)
    return render_template('index.html', recommendations=recommendations)