project_data = {
    "Customer Churn Prediction Pipeline": {
        "skills": ["python", "machine learning", "pandas", "sql"],
        "description": """
Built an end-to-end churn prediction system to identify customers likely to stop using a service.
Performed data cleaning, feature engineering, and exploratory analysis on customer behavior data.
Trained classification models and evaluated performance using precision-recall metrics.
"""
    },

    "Real-Time Sales Performance Dashboard": {
        "skills": ["power bi", "sql", "excel"],
        "description": """
Designed an interactive business dashboard to monitor sales performance across regions and products.
Built data models using SQL and created DAX measures for KPIs like revenue growth and profit margin.
Enabled drill-down analysis for business decision-making.
"""
    },

    "Housing Price Prediction Model": {
        "skills": ["python", "machine learning", "pandas"],
        "description": """
Developed a regression model to predict housing prices based on multiple features.
Performed data preprocessing, feature engineering, and model comparison using regression algorithms.
Improved prediction accuracy through hyperparameter tuning.
"""
    },

    "A/B Testing Analysis Framework": {
        "skills": ["python", "statistics", "sql"],
        "description": """
Built a statistical framework to analyze A/B testing experiments.
Calculated conversion rates, confidence intervals, and performed hypothesis testing.
Provided insights for data-driven decision making in product optimization.
"""
    },

    "Time Series Forecasting System": {
        "skills": ["python", "statistics", "machine learning"],
        "description": """
Developed forecasting models to predict future trends in sales and demand.
Applied ARIMA and Prophet models to capture seasonality and trends.
Evaluated models using RMSE and MAPE metrics.
"""
    },

    "Web Scraping Market Intelligence System": {
        "skills": ["python", "nlp", "sql"],
        "description": """
Automated data extraction from websites to monitor competitor pricing and trends.
Cleaned and structured data for analysis and applied basic NLP for sentiment insights.
Generated reports for business intelligence use cases.
"""
    },

    "ML Model Deployment Pipeline": {
        "skills": ["python", "machine learning"],
        "description": """
Built and deployed a machine learning model using FastAPI and Docker.
Created REST APIs for real-time predictions and integrated CI/CD pipeline for automation.
Monitored model performance in production environment.
"""
    }
}

def recommend_projects(skills):

    results = []

    for project, data in project_data.items():

        project_skills = data["skills"]

        # check if user has at least one matching skill
        if any(skill in skills for skill in project_skills):

            results.append({
                "project": project,
                "skills": project_skills,
                "desc": data["description"]
            })

    # fallback if no match
    if len(results) == 0:
        results.append({
            "project": "Beginner Data Analysis Project",
            "skills": ["python"],
            "desc": "Start with basic data analysis and visualization."
        })

    return results