
# Load coding libraries
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import pandas as pd

# If error occur when loads autogluon package,
# exccute below commend to fix the problem
from tqdm import tqdm

# For any problems related to download autogluon
# please refer to https://auto.gluon.ai/stable/install.html
# For ARM(Apple M Chips), please use conda comment to install autogluon
from autogluon.tabular import TabularDataset, TabularPredictor

# Load combined 5 seasons records, salary is adjusted for inflation
data = TabularDataset('meta_data')
# Drop unnecessary column and prepare for training
data = data.drop(columns=['Player']).drop(
    columns=['first_name']).drop(columns=['last_name'])
# Random split data into two groups. 80% for trainning
# and 20% for test/validation. Set seed for reproducible results
train_data, val_data = train_test_split(
    data, test_size=0.2, shuffle=True, random_state=25
)
# For validation and test group, we drop predicting
# columns to isolate model and answer key.
val_data_noLabel = val_data.drop(columns=['salary'])

# Peak into statistic spread of our preidicting value
label = 'salary'

# Before training, please change path to your
# desired directory. (stores trained model)
save_path = '/Users/main/Desktop/dsci510/project'

# Please check and adjust model parameters to fit your need.
# Higher accuracy requires longer time and higher computing power
# Training time limit to 1 minuates
time_limit = 1*60
predictor = TabularPredictor(
    label=label,
    path=save_path,
    eval_metric="mean_absolute_error"
).fit(
    train_data,
    time_limit=time_limit,
    auto_stack=True,
    presets="best_quality"
)

# 1st run  we used medium quality model for fast testing.
# Both rmsq and absolute mean error
# 2nd run, good quality, autostack,num_bag_folds=3
# "mean_absolute_error": -3630347,"root_mean_squared_error": -5654671,
# "mean_squared_error": -31975306135268,
# "r2": 0.68088,"median_absolute_error": -2755374
# 3rd run, feed all 5 years of data to model,
# "mean_absolute_error": -2845665,"root_mean_squared_error": -4370963,
# "mean_squared_error": -19105321713508,"r2": 0.81100,
# "median_absolute_error": -1652856
# 4th run, without name
# "mean_absolute_error": -3351819,root_mean_squared_error": -5365244,
# "mean_squared_error": -28785851392114, "r2": 0.75558,
# "median_absolute_error": -1753217

# no need just incase path missing
predictor = TabularPredictor.load(save_path)
# Test trained model on val/test data set
val_pred = predictor.predict(val_data_noLabel)
print("Predicted salary is: \n", val_pred)
perf = predictor.evaluate_predictions(
    y_true=val_data['salary'], y_pred=val_pred, auxiliary_metrics=True)
print("val data is \n", val_data['salary'])


# Example data (replace with your actual and predicted values)
players = range(532)
actual_salary = val_data['salary']
predicted_salary = val_pred

# Calculate residuals
residuals = actual_salary - predicted_salary

# Plot the residual plot
plt.figure(figsize=(10, 6))
plt.scatter(range(len(actual_salary)), residuals, marker='o', color='red')

# Add a horizontal line at y=0 for reference
plt.axhline(y=0, color='black', linestyle='--')

# Customize the plot
plt.title('Residual Plot: Actual Salary vs. Predicted Salary')
plt.xlabel('Data Points')
plt.ylabel('Residuals')
plt.grid(True)

# will export csv conatins two columns actual salary and predicted salary
df_submission = pd.DataFrame(columns=["original", "prediction"])
df_submission["original"] = val_data['salary']
df_submission["prediction"] = val_pred
df_submission.to_csv("original_prediction")

# Show the plot
plt.show()

predictor.feature_importance(val_data)

a = predictor.feature_importance(val_data)


# Create a bar chart with index as x-axis
plt.bar(a.index, a['importance'])
plt.xticks(rotation='vertical')
# Add labels and title
plt.xlabel('Index')
plt.ylabel('Importance')
plt.title('Bar Chart of Importance')

# Show the plot
plt.show()

results = predictor.fit_summary()

predictor.leaderboard(val_data)
