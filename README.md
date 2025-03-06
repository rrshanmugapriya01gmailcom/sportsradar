# Game Analytics: Unlocking Tennis Data with SportRadar API

## Overview
The **SportsRadar Event Explorer** is a data-driven web application built using **Streamlit and MySQL** that provides insights into **tennis competitions, player performance, and venue details**. It processes **SportRadar API data**, stores structured information in a relational database, and offers analytical tools to help **sports enthusiasts, analysts, and organizations** better understand competition structures and player rankings.

## Features
### 1️⃣ **Home Page**
- Provides an **overview** of the application with key statistics, including:
  - Total Players
  - Total Competitions
  - Total Venues
- Displays **Top 10 Players by Rank**.
- Includes **Tennis-related images** to enhance user experience.

### 2️⃣ **Player Performance Dashboard**
- Allows users to select a **player by name** (instead of competitor ID).
- Displays **current rank, points, and competitions played**.
- Predicts **future player rank** using a **RandomForest Regression model**.
- Provides an interactive **performance visualization**.

### 3️⃣ **Competitions Overview**
- Enables filtering **competitions by type (e.g., ATP, WTA, Grand Slams)**.
- Displays competition **names, gender categories, and levels**.

### 4️⃣ **Venue Explorer**
- Filters venues by **country**.
- Displays **venue details**, including name, city, and timezone.

### 5️⃣ **Search & Insights**
- Allows users to **search for players or competitions**.
- Displays relevant details if a match is found.
- Provides **warning messages** for no results.

## Technologies Used
- **Python** (for backend logic)
- **Streamlit** (for web app development)
- **MySQL** (for storing structured data)
- **Pandas** (for data manipulation)
- **Scikit-Learn** (for ML model)
- **Matplotlib & Plotly** (for data visualization)

## Impact & Benefits
✅ **Enhances sports analytics** by providing structured insights.
✅ **Assists analysts & coaches** in understanding player rankings.
✅ **Improves competition tracking** with real-time event data.
✅ **Offers interactive dashboards** for better decision-making.

## Future Enhancements
🚀 **Live data updates** from SportRadar API.
🚀 **Advanced machine learning models** for ranking predictions.
🚀 **Player comparison tool** for in-depth performance analysis.
🚀 **Integration with external APIs** for real-time match statistics.

## How to Run the App
1️⃣ Clone the repository.
2️⃣ Install dependencies: `pip install -r requirements.txt`
3️⃣ Run Streamlit: `streamlit run app.py`
4️⃣ Explore tennis data interactively!

---
📢 **For feedback or feature requests, reach out!** 🎾

