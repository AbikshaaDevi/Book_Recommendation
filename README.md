# Book Recommendation System

This repository contains a **Book Recommendation System** built using machine learning techniques.  
The project analyzes user ratings and book data to provide personalized recommendations.

## Features
- Data preprocessing and cleaning of book datasets
- Exploratory data analysis and visualization
- Recommendation models:
  - Popularity-based recommendation
  - Collaborative filtering (user-based & item-based)
  - Matrix factorization techniques
- Interactive interface for testing recommendations

## Tech Stack
- **Python**
- **Pandas, NumPy, Matplotlib, Seaborn**
- **Scikit-learn**
- **Flask / Streamlit (if applicable)**

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AbikshaaDevi/Book_Recommendation.git
   cd Book_Recommendation
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the Jupyter notebooks for data exploration and model building:
   ```bash
   jupyter notebook
   ```
2. If the project includes a web app:
   ```bash
   python app.py
   ```
   Open the browser at `http://127.0.0.1:5000/`

## Dataset
- The dataset includes books, users, and ratings information.  
- Source: [Goodbooks-10k](https://github.com/zygmuntz/goodbooks-10k) or any other relevant dataset.

## Folder Structure
```
Book_Recommendation/
│-- data/               # Raw and processed datasets
│-- notebooks/          # Jupyter notebooks for EDA and model building
│-- models/             # Saved models (if any)
│-- app.py              # Flask/Streamlit app (if implemented)
│-- requirements.txt    # Dependencies
│-- README.md           # Project documentation
```

## Future Improvements
- Implement deep learning-based recommendation models
- Add hybrid recommendation (content + collaborative)
- Enhance UI/UX of the web app

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
