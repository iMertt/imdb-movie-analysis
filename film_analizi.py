import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Read the dataset
df = pd.read_csv('imdb_top_1000.csv')

# Remove unnecessary columns
df = df[['Series_Title', 'Genre', 'IMDB_Rating', 'No_of_Votes']]

# Clean up missing values
df = df.dropna()

# Convert genre string (comma-separated) into a list
df['Genre'] = df['Genre'].apply(lambda x: [genre.strip() for genre in x.split(',')])

# Expand genres into separate rows
df = df.explode('Genre')

# Filter popular movies (more than 50,000 votes)
df = df[df['No_of_Votes'] > 50000]

# Calculate the average rating per genre
genre_ratings = df.groupby('Genre')['IMDB_Rating'].mean().sort_values(ascending=False)
print("Average ratings:", genre_ratings)  # For verification

# Streamlit interface
st.title("IMDb Movie Genres Average Rating Analysis")
st.write("This application visualizes the average ratings of movie genres from the IMDb Top 1000 dataset.")

# Plot the graph
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x=genre_ratings.index, y=genre_ratings.values, palette='viridis', ax=ax, ci=None)  # Remove error bars
plt.ylim(6, 8)  # Set y-axis range to 6-8
plt.xticks(rotation=45, ha='right')
plt.xlabel('Movie Genre')
plt.ylabel('Average IMDb Rating')
plt.title('Average Ratings by Genre')
st.pyplot(fig)

# Genre selection and details
selected_genre = st.selectbox("View details by selecting a genre:", genre_ratings.index)
st.write(f"Selected genre: {selected_genre}")
st.write(f"Average IMDb rating: {genre_ratings[selected_genre]:.2f}")

# Add GitHub link with emoji at the bottom left
st.markdown(
    """
    <div style='position: fixed; bottom: 10px; left: 10px;'>
        <a href="https://github.com/iMertt" target="_blank">
            <span style="font-size: 24px;">👉🏽📺</span> Visit my GitHub!
        </a>
    </div>
    """,
    unsafe_allow_html=True
)