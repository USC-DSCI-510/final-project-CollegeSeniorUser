[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/h_LXMCrc)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12857349&assignment_repo_type=AssignmentRepo)
# DSCI 510 Final Project

## Name of the Project
* NBA Player Salary Prediction Using Deep Learning
## Team Members (Name and Student IDs)
* Chuanzhou Zhang: 8165737934
* Kenneth Chan: 5772665598
## Instructions to create a conda environment
* One of the packages requires Python 3.10 for stable execution
* Demo to create conda environment (copy below code to terminal):
  - conda create -n autogluon python=3.10
  - conda activate autogluon
## Instructions on how to install the required libraries
<p>Please run all terminal commend line stated in the () </p>
<p>If there is trouble installing <b>AutoGluon</b>, please have all dependency installed
and contact author or refer to its website listed below</p>

1. selenium (1st line)
   - pip install selenium
   - https://pypi.org/project/selenium/
2. requests (1st line)
   - pip install requests
   - https://pypi.org/project/requests/
3. beautifulsoup (1st line)
   - pip install beautifulsoup4
   - https://pypi.org/project/beautifulsoup4/
4. pandas (1st line)
   - pip install pandas
   - https://pypi.org/project/pandas/
5. Scikit-learn (1st line)
   - pip install scikit-learn
   - https://pypi.org/project/scikit-learn/ 
6. Tqdm (1st line)
   - conda install -c conda-forge tqdm
   - https://pypi.org/project/tqdm/ 
7. autogluon (First 2 lines) (MacOS)
   - conda install -c conda-forge mamba
   - mamba install -c conda-forge autogluon
   - For problem please refer to the website below
   - https://auto.gluon.ai/stable/install.html
   - Note: Please create an environment with Python 3.10 for the most stable run
8. lxml
   -  pip install lxml
   -  https://pypi.org/project/lxml/
9. seaborn
   - pip install seaborn
   - https://seaborn.pydata.org/installing.html

## Instructions on how to download the data (get_data.py)
<p> The get_data.py program uses the <b>Selenium</b> module to simulate user actions such 
  as tapping and changing the page. Once starts running, the program will 
  initiate the driver to open the Chrome browser. Running time varies during testing. 
  Once the page opens please <b>close</b> any <b>advertisement</b> or "<b>accept cookies</b>" pop-ups. 
</p>

<p>
  There were times we had trouble initiating Chrome driver. Please run once again to solve the problem. 
</p>

* Output data: all scraped raw data will be stored to raw data
  - stats_2019_2020  
  - stats_2020_2021  
  - stats_2021_2022  
  - stats_2022_2023  
  - stats_2023_2024
  - salary_2019_2020  
  - salary_2020_2021  
  - salary_2021_2022  
  - salary_2022_2023  
  - salary_2023_2024  
* Please have all raw and processed data downloaded to one single folder along with the source code
  
## Instructions on how to clean the data
* run clean_data.py to get processed data
* Output: 
  - merged dataset contains processed data for the first five seasons
    - merged2019_2020.csv
    - merged2020_2021.csv
    - merged2021_2022.csv
    - merged2022_2023.csv
    - merged2023_2024.csv
  - meta_data contains all processed data for all five seasons
    - meta_data

## Instructions on how to run analysis code
<p>
  <b>run_analysis.py</b>: execute this program for training ml model and get analysis data</l>
</p>
<p>
  By default, training time is limited to 1 minute for the demo. For better results, please follow the comments within to
  increase training time. We recommend using jupyter notebook for this part but .py format is also provided
</p>

* We also have uploaded it in jupyternote book format. Please follow the instructions within to run the program
* We included the above demo data in the processed_data folder for anyone interested to see the comparison
* Output:
  - original_prediction: two columns, 1st column actual salary data, 2nd column predicted salary
  - model: folder includes all trained models
    
## Instructions on how to create visualizations
<p>
  Run <b>visualize_results.py</b> to get vsualizations included in the <b>final_report.pdf<b>
</p> 

## Note: 
<p>
  For run_analysis and visualizations, We recommend using jupyter notebook for this part, but .py format is also provided. All jupyterNotebook files are within <b>src/utils/</b>
</p>

*  If any problem or specfiation needed, please don't hesitate and contact me

