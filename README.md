
<h1>🍨Recipe Recommendation System🍨</h1>

<h2>Project Overview:-</h2>
The Recipe Recommendation System is a project aimed at providing personalized recipe recommendations to users based on their preferences, dietary restrictions, and previous interactions.The system leverages machine learning algorithms to analyze user data and suggest recipes that match their tastes and nutritional needs.</br>
<h2>👍Table of Contents</h2>
<strong>👉User Profile Management:</strong> Create and manage user profiles with preferences and dietary restrictions.</br></br>
<strong>👉Recipe Database:</strong> Access a comprehensive database of recipes with detailed nutritional information.</br>
<strong>👉Personalized Recommendations:</strong>Get recipe suggestions tailored to individual user profiles.</br>
<strong>👉Search Functionality:</strong>Search for recipes based on ingredients, cuisine, and more.</br>
<strong>👉Rating and Feedback System:</strong>Users can rate recipes and provide feedback to improve recommendations.</br>
<strong>👉Nutritional Analysis:</strong>Detailed nutritional breakdown of recommended recipes.</br>
<h2>Architecture</h2></br>The system architecture is composed of several key components:</br>
<strong>👉Data Collection and Preprocessing:</strong>Collects user data and recipes, and preprocesses them for analysis.</br>
<strong>👉Recommendation Engine:</strong>Utilizes machine learning algorithms to generate personalized recommendations.</br>
<strong>👉Web Interface:</strong>A user-friendly web interface for interacting with the system.</br>
<strong>👉Database:</strong>Stores user profiles, recipes, and interaction data.</br>
<h2>Installation</h2>
<h1>To set up the Recipe Recommendation System locally, follow these steps:</h1>

<h4>Clone the Repository:</h4>

<p>bash
Copy code
git clone https://github.com/your-username/recipe-recommendation-system.git
cd recipe-recommendation-system</p>
<h4>Create a Virtual Environment:</h4>

<p>bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`</p>
<h4>Install Dependencies:</h4>

<p>bash
Copy code
pip install -r requirements.txt</p>
<h4>Set Up the Database:</h4>

<p>bash
Copy code
python setup_database.py</p>
<h4>Run the Application:</h4>
- `app/`: Contains the Flask application code.</br>
  - `__init__.py`: Initializes the Flask app.</br>
  - `routes.py`: Contains the route definitions and recommendation logic.</br>
  - `models.py`: Placeholder for future database models.</br>
  - `static/`: Contains static files like CSS.</br>
  - `templates/`: Contains HTML templates.</br>
- `data/`: Contains data files like CSVs and pickled models.</br>
- `notebooks/`: Contains Jupyter notebooks for each step of the process.</br>
- `app.py`: Main entry point to run the Flask app.</br>
- `requirements.txt`: Lists the required Python packages.</br>
- `README.md`: Project documentation.</br>
1. Install the required packages:</br>
  `bash</br>
  pip install -r requirements.txt
  `</br>
2. Run the Flask application:</br>
  `bash
  python app.py
  `</br>
3. Open your browser and go to `http://127.0.0.1:5000/`.</br>

<p>bash
Copy code
python app.py</p>
<h4>Usage</h4>
<p>Once the application is running, you can access the web interface at http://localhost:5000.<br>
 From here, you can:</p>
<p>👉Create a new user profile.</br>
👉Browse and search for recipes.</br>
👉Get personalized recipe recommendations.</br>
👉Rate and review recipes.</br></p>
<h4>Datasets</h4>
<strong>The system uses the following datasets:</strong>

<strong>Recipe Dataset:</strong> Contains detailed information about each recipe, including ingredients, instructions, and nutritional values.</br>
<strong>User Interaction Dataset:</strong> Records user interactions with recipes, such as ratings and feedback.</br>
Datasets are preprocessed and stored in a database for efficient querying and analysis.

<strong>Model Training</strong>
The recommendation engine is built using collaborative filtering and content-based filtering techniques.
<h4>To train the models:</h4>

<strong>Prepare the Training Data:</strong>

<p>bash
Copy code
python prepare_training_data.py</p>
<strong>Train the Models:</strong>

<p>bash
Copy code
python train_models.py</p>
<strong>Evaluate the Models:</strong>

<p>bash
Copy code
python evaluate_models.py</p>
<strong>Evaluation</strong>
<p>Model performance is evaluated using metrics such as Precision, Recall, and F1-Score.</br>Detailed evaluation results are logged and can be reviewed to improve the recommendation system.</p>

<strong>Contributing</strong>
<p>We welcome contributions to improve the Recipe Recommendation System!</p>
<strong>To contribute:</strong>
 <p>👉Fork the repository.</br>
👉Create a new branch.</br>
👉Make your changes.</br>
👉Submit a pull request.</br></p>
<p>Please ensure that your code adheres to the project's coding standards and includes appropriate tests.</p>
<h4>## Usage</h4>

<strong>1. **Data Scraping:**</strong> Run the `data_scraping.ipynb` notebook to scrape recipes from Allrecipes.com and save the data to `recipes.csv`.</br>
<strong>2. **Data Preprocessing:**</strong>Run the `data_preprocessing.ipynb` notebook to preprocess the scraped data.</br>
<strong>3. **Content-Based Filtering:**</strong>Run the `content_based_filtering.ipynb` notebook to implement content-based filtering.</br>
<strong>4. **Collaborative Filtering:**</strong>Run the `collaborative_filtering.ipynb` notebook to implement collaborative filtering.</br>
<strong>5. **Hybrid Recommendation:**</strong>Run the `hybrid_recommender.ipynb` notebook to implement the hybrid recommendation system.</br>

<h4>## License</h4>

<strong>This project is licensed under the MIT License.</strong>

<h4>Contact</h4>
<strong>For any questions or suggestions, please contact:</strong>

<p><strong>Name:</strong> Mr. Rahul Vishwakarma</br>
<strong>Email:</strong> rahullucky00@gmail.com</br>
<strong>GitHub:</strong> rahulvishwakarma00</br></p>
<p></p>Thank you for using the Recipe Recommendation System! We hope it helps you discover delicious and nutritious recipes tailored to your preferences.</p>
