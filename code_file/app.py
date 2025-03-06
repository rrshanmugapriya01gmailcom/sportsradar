import streamlit as st
import pandas as pd
import mysql.connector
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px  # Import Plotly for interactive charts

# MySQL Database Connection
def get_db_connection():
    return mysql.connector.connect(host="localhost",
    user="root",
    password="Priya09@2001",
    database="sportsradar",
    )

# Load Data from MySQL
@st.cache_data
def load_data():
    conn = get_db_connection()
    
    competitor_rankings = pd.read_sql("SELECT * FROM competitor_rankings", conn)
    competitors = pd.read_sql("SELECT * FROM competitors", conn)
    competitions = pd.read_sql("SELECT * FROM competitions", conn)
    venues = pd.read_sql("SELECT * FROM venues", conn)
    
    conn.close()
    return competitor_rankings, competitors, competitions, venues

competitor_rankings, competitors, competitions, venues = load_data()

# Load the trained RandomForest model
@st.cache_resource
def load_model():
    with open("sports_radar_model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

# Load the model
model = load_model()
print("✅ Model loaded successfully!")

# --- Sidebar Navigation ---
st.sidebar.title("🎾 Sports Analytics Dashboard")
page = st.sidebar.radio("Go to", ["🏠 Home", "📊 Player Performance", "🏆 Competitions", "📍 Venues", "🔍 Search & Insights"])

# --- 1️⃣ Home Page ---
# --- 1️⃣ Home Page ---
if page == "🏠 Home":
    st.title("🎾 Game Analytics: Unlocking Tennis Data")

    # App Introduction
    st.markdown("""
        Welcome to **Game Analytics**, your go-to platform for **tennis performance analysis**!  
        This app extracts data from the **SportRadar API**, giving sports analysts, players, and fans deep insights into **player rankings, competitions, and venues**.  
        
        Whether you're tracking player stats, predicting rankings, or exploring tournament trends – this tool has you covered! 🎾📊
    """)

    # Features of the App
    st.subheader("🔍 Key Features")
    st.markdown("""
    - **📊 Player Performance Analysis** – Check rankings, points, and trends.  
    - **📈 Predictive Model** – Forecast future rankings based on past data.  
    - **🏆 Competition Explorer** – Get details of different tournaments.  
    - **📍 Venue Insights** – Learn about tournament locations.  
    - **🔎 Search & Insights** – Find players and competitions instantly.  
    """)

    # Show quick stats
    st.subheader("📌 Quick Stats")
    col1, col2, col3 = st.columns(3)
    col1.metric("👤 Total Players", competitors["name"].nunique())  # Changed from len(competitors)
    col2.metric("🏆 Total Competitions", len(competitions))
    col3.metric("📍 Total Venues", len(venues))

    st.subheader("🎾 Top 10 Players by Rank")
    top_players = competitor_rankings.merge(competitors, on="competitor_id", how="left")[["rank", "name", "points"]].head(10)
    st.dataframe(top_players)

    # Call to Action
    st.markdown("⚡ **Start exploring player stats and predictions now!** Use the sidebar to navigate. ⏩")


# --- 2️⃣ Player Performance Page ---
elif page == "📊 Player Performance":
    st.title("📊 Player Performance Dashboard")
    
    # Replace "sr:competitor" with actual competitor name
    competitor_rankings = competitor_rankings.merge(competitors[["competitor_id", "name"]], on="competitor_id", how="left")

    # Select Player
    player_id = st.selectbox("Select Player", competitor_rankings["name"].unique())

    player_data = competitor_rankings[competitor_rankings["name"] == player_id]
    if not player_data.empty:
        st.write(f"### Player Rank: {player_data['rank'].values[0]}")
        st.write(f"**Points:** {player_data['points'].values[0]}")
        st.write(f"**Competitions Played:** {player_data['competitions_played'].values[0]}")
    
        # Predict Future Rank
        features = player_data[["points", "competitions_played", "movement"]]
        prediction = model.predict(features)
        st.success(f"📈 Predicted Future Rank: {int(prediction[0])}")

    # 🎨 **New Visualization: Top 10 Players by Points (Bar Chart)**
    st.subheader("🏆 Top Players by Points")

    # Select top 10 players based on points
    top_players = competitor_rankings.nlargest(10, "points")

    # Create Bar Chart
    fig = px.bar(top_players, x="points", y="name", 
                 orientation="h",  # Horizontal bar chart
                 text="points", 
                 title="Top 10 Players with Highest Points",
                 color="points",
                 color_continuous_scale="viridis")  # Beautiful color scheme

    # Improve layout
    fig.update_layout(xaxis_title="Points", 
                      yaxis_title="Player Name", 
                      template="plotly_dark")

    # Show the chart
    st.plotly_chart(fig, use_container_width=True)

# --- 3️⃣ Competitions Page ---
elif page == "🏆 Competitions":
    st.title("🏆 Competitions Overview")
    
    # Filter Competitions
    competition_type = st.selectbox("Filter by Type", competitions["type"].unique())
    filtered_competitions = competitions[competitions["type"] == competition_type]
    
    st.write(f"### {competition_type} Competitions")
    st.dataframe(filtered_competitions[["name", "gender", "level"]])

# --- 4️⃣ Venue Explorer ---
elif page == "📍 Venues":
    st.title("📍 Venue Explorer")
    
    country = st.selectbox("Select Country", venues["country_name"].unique())
    venues_in_country = venues[venues["country_name"] == country]
    
    st.write(f"### Venues in {country}")
    st.dataframe(venues_in_country[["venue_name", "city_name", "timezone"]])

# --- 5️⃣ Search & Insights ---
elif page == "🔍 Search & Insights":
    st.title("🔍 Search & Insights")
    
    search_term = st.text_input("Search by Player Name or Competition")
    
    if search_term:
        player_results = competitors[competitors["name"].str.contains(search_term, case=False, na=False)]
        competition_results = competitions[competitions["name"].str.contains(search_term, case=False, na=False)]
        
        st.write(f"### Search Results for '{search_term}'")
        if not player_results.empty:
            st.write("#### Players Found:")
            st.dataframe(player_results)
        if not competition_results.empty:
            st.write("#### Competitions Found:")
            st.dataframe(competition_results)
        if player_results.empty and competition_results.empty:
            st.warning("No results found.")
