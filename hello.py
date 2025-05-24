from preswald import connect, get_df, query, table, text, plotly, sidebar, image
import plotly.express as px

# Branding via sidebar
sidebar()
image("images/logo.png", width=160)
text("# Kaggle Top 100 Insights")

# 1. Load data from preswald.toml
connect()
df = get_df("kaggle_top_100")

# 2. Filter: Upvote > 2000
sql = "SELECT * FROM kaggle_top_100 WHERE Upvote > 2000"
filtered_df = query(sql, "kaggle_top_100")

# 3. Display filtered table
table(filtered_df, title="Top Datasets with >2000 Upvotes")

# 4. Scatter plot: Usability vs Upvote
fig = px.scatter(
    df,
    x="Usability",
    y="Upvote",
    color="Rank",
    hover_data=["Dataset_Name", "Author"],
    title="Upvotes vs Usability by Dataset"
)
plotly(fig)
