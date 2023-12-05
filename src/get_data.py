from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
import requests


def main(num):
    # step1 scarpe all players stats in given(num) season
    step1(num)
    # step2 if year is 2023 run this to scrape salary
    if(num == 2023):
        step2()
    else:
        # scrape other given year
        step3(num)


def step1(num):
    # season end year
    end = num+1
    # create chrome driver to simulate user action (please install chrome)
    driver = webdriver.Chrome()
    url = "https://www.nba.com/stats/players/traditional?"
    # check
    try:
        driver.get(url)
    except Exception:
        raise Exception("The is a problem with input website")
    # select chooses display all pages/players' records; select2
    # chooses season; select3 chooses season type
    # display player stats
    select2(driver, num)
    select3(driver)
    select(driver)
    # locate the table container by search class attribute
    src = driver.page_source
    parser = BeautifulSoup(src, "lxml")
    table = parser.find(
        "div",
        attrs={"class": "Crom_container__C45Ti crom-container"}
    )
    # get headers
    header = [h.text.strip() for h in table.findAll('th')]

    # filter out hidden headers that we don't need
    header = [a for a in header if 'RANK' not in a][1:]
    # each row contains stats of a player and all his stats
    rows = table.findAll('tr')[1:]
    # scraping out all player's stats to a 2d array
    player_stat = [[td.getText().strip() for td in rows[i]
                    .findAll('td')[1:]] for i in range(len(rows))]
    # covert 2d array to a panda dataframe
    df = pd.DataFrame(player_stat)
    df.columns = header
    # export file to stats_start_end
    file = f"stats_{num}_{end}"
    df.to_csv(file)


def step2():
    # check website path
    url = "https://hoopshype.com/salaries/players/"

    r = requests.get(url)
    r_html = r.text

    soup = BeautifulSoup(r_html, 'html.parser')

    salary_table = soup.find('table')
    length = len(salary_table.find_all("td"))

    player_names = [salary_table.find_all("td")[i].text.strip()
                    for i in range(9, length, 8)]
    column1 = [salary_table.find_all("td")[i].text.strip()
               for i in range(10, length, 8)]
    df_dict = {'player_names': player_names, '2023/24': column1, }
    df_salary23 = pd.DataFrame(df_dict)
    df_salary23.to_csv("salary_2023_2024")
    # export season 23/24


def step3(num):
    end = num + 1  # end season year
    src2 = f"https://hoopshype.com/salaries/players/{num}-{end}/"
    try:
        response2 = requests.get(src2)
        # If the response was successful, no Exception will be raised
        response2.raise_for_status()
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success!')
    # scrape all the info needed
    soup2 = BeautifulSoup(response2.text, "html.parser")
    header2 = soup2.find('tr', attrs={"class": "table-index"})
    # get header
    index = [i.text.strip() for i in header2.find_all("td")[1::2]]
    table2 = soup2.find('tbody')
    row = table2.find_all('tr')
    player_salary = [[td.getText(strip=True)for td in row[i]
                      .findAll('td')[1::2]] for i in range(len(row))]
    df2 = pd.DataFrame(player_salary)
    df2.columns = index
    # export to csv as salary_num_end
    file = f"salary_{num}_{end}"
    df2.to_csv(file)


def select(driver):
    select = Select(
        driver.find_element(
            By.XPATH,
            r"/html/body/div[1]/div[2]/div[2]/div[3]/section[2]/div"
            "/div[2]/div[2]/div[1]/div[3]/div/label/div/select"
        )
    )
    select.select_by_index(0)  # choose display all players


def select2(driver, num):
    select2 = Select(
        driver.find_element(
            By.XPATH,
            r"/html/body/div[1]/div[2]/div[2]/div[3]/section"
            "[1]/div/div/div[1]/label/div/select"
        )
    )
    select2.select_by_index((2023-num))  # choose season (2023-num)=index


def select3(driver):
    select3 = Select(
        driver.find_element(
            By.XPATH,
            r"/html/body/div[1]/div[2]/div[2]/div[3]/"
            "section[1]/div/div/div[2]/label/div/select"
        )
    )
    select3.select_by_index(1)  # choose regular season


if __name__ == "__main__":
    main(2019)
    main(2020)
    main(2021)
    main(2022)
    main(2023)
