# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataframes
df_2019 = pd.read_csv('merged2019_2020.csv')
df_2020 = pd.read_csv('merged2020_2021.csv')
df_2021 = pd.read_csv('merged2021_2022.csv')
df_2022 = pd.read_csv('merged2022_2023.csv')
df_2023 = pd.read_csv('merged2023_2024.csv')
df_all = pd.read_csv('meta_data')

# Select columns of interest
selected_columns = ['salary', 'Age', 'GP', 'Min', 'PTS', 'FGM',
                    'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM',
                    'FTA', 'FT%', 'OREB', 'DREB', 'REB', 'AST',
                    'TOV', 'STL', 'FP', 'BLK']
selected_df = df_all[selected_columns]

# Create the correlation matrix
correlation_matrix = selected_df.corr()

# Select only the row corresponding to 'salary' for the heatmap
salary_correlation = correlation_matrix.loc[['salary']]

# Plot a heatmap for 'salary' against other columns
# Adjust the height based on the number of columns
heatmap_fig, heatmap_ax = plt.subplots(figsize=(15, 2))
sns.heatmap(salary_correlation, annot=True, cmap='coolwarm',
            fmt=".2f", linewidths=.5, ax=heatmap_ax)
heatmap_ax.set_title('Correlation Heatmap: Salary vs Other Columns')

# Save the heatmap figure to a variable
heatmap_plot = (heatmap_fig, heatmap_ax)

# Display the heatmap
plt.show()

# Sort the dataframe by 'Player_x'
sorted_df = df_all.sort_values(by='Player')

# Plotting for 'Andrew Wiggins'
player_rows_aw = sorted_df[sorted_df['Player'] == 'Andrew Wiggins']
player_rows_aw = player_rows_aw.sort_values(by='season')
fig_aw, ax1_aw = plt.subplots(figsize=(10, 6))
# Plotting 'salary' on the first y-axis
color = 'tab:red'
ax1_aw.set_xlabel('Season')
ax1_aw.set_ylabel('Salary', color=color)
ax1_aw.plot(player_rows_aw['season'], player_rows_aw['salary'],
            color=color, marker='o', label='Salary')
ax1_aw.tick_params(axis='y', labelcolor=color)

# Creating a secondary y-axis for 'PTS'
ax2_aw = ax1_aw.twinx()
color = 'tab:blue'
ax2_aw.set_ylabel('Points (PTS)', color=color)
ax2_aw.plot(player_rows_aw['season'], player_rows_aw['FTA'],
            color=color, marker='o', label='FTA')
ax2_aw.plot(player_rows_aw['season'], player_rows_aw['FTM'],
            color='orange', marker='o', label='FTM')
ax2_aw.tick_params(axis='y', labelcolor=color)

# Adding labels and title
plt.title('Salary, FTA, and FTM Over Seasons for Andrew Wiggins')

# Display the legend
ax1_aw.legend(loc='upper left')
ax2_aw.legend(loc='upper right')

# Save the Andrew Wiggins figure to a variable
aw_plot = (fig_aw, ax1_aw)

# Display the Andrew Wiggins plot
plt.show()

# Plotting for 'Jordan Poole'
player_rows_jp = sorted_df[sorted_df['Player'] == 'Jordan Poole']
player_rows_jp = player_rows_jp.sort_values(by='season')
fig_jp, ax1_jp = plt.subplots(figsize=(10, 6))
# ... (rest of the plotting code)
# Plotting 'salary' on the first y-axis
color = 'tab:red'
ax1_jp.set_xlabel('Season')
ax1_jp.set_ylabel('Salary', color=color)
ax1_jp.plot(player_rows_jp['season'],
            player_rows_jp['salary'], color=color, marker='o')
ax1_jp.tick_params(axis='y', labelcolor=color)

# Creating a secondary y-axis for 'PTS'
ax2_jp = ax1_jp.twinx()
color = 'tab:blue'
ax2_jp.set_ylabel('Points (PTS)', color=color)
ax2_jp.plot(player_rows_jp['season'],
            player_rows_jp['PTS'], color=color, marker='o')
ax2_jp.tick_params(axis='y', labelcolor=color)

# Adding labels and title
plt.title('Salary and Points (PTS) Over Seasons for Jordan Poole')

# Save the Jordan Poole figure to a variable
jp_plot = (fig_jp, ax1_jp)

# Display the Jordan Poole plot
plt.show()
