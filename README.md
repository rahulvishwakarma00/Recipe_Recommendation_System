- `app/`: Contains the Flask application code.
  - `__init__.py`: Initializes the Flask app.
  - `routes.py`: Contains the route definitions and recommendation logic.
  - `models.py`: Placeholder for future database models.
  - `static/`: Contains static files like CSS.
  - `templates/`: Contains HTML templates.
- `data/`: Contains data files like CSVs and pickled models.
- `notebooks/`: Contains Jupyter notebooks for each step of the process.
- `app.py`: Main entry point to run the Flask app.
- `requirements.txt`: Lists the required Python packages.
- `README.md`: Project documentation.
1. Install the required packages:
  `bash
  pip install -r requirements.txt
  `
2. Run the Flask application:
  `bash
  python app.py
  `
3. Open your browser and go to `http://127.0.0.1:5000/`.
