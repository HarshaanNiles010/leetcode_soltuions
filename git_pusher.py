import subprocess
import logging
import datetime
from random import randrange
import file_maker

def generate_date():
    start = datetime.date(2023,1,1)
    # initializing K 
    k = 245
    res = []
    for day in range(k):
        date = (start + datetime.timedelta(days = day)).isoformat()
        res.append(date)
    # printing result
    return res


def git_puuuuuush(random_date,date_as_string):
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    repo_path = '/Users/harshaanbabra/Desktop/Code/Python/leetcode_soltuions'
    try:
        subprocess.run(['git','add','.'], cwd=repo_path, check=True)
        logging.info('git add success')
        subprocess.run( ['git','commit', '--date= ' + "\"" + date_as_string + "00:00:00" + "\"" ,'-m','working'], cwd=repo_path, check = True)
        logging.info('git commit success')
        subprocess.run(['git','push'], cwd=repo_path, check=True)
        logging.info('git push success')
        print("Success")
    except subprocess.CalledProcessError as e:
        print(f"Error during push: {e}")
        logging.info(f"Error: {e}")

if __name__=='__main__':
    #git_puuuuuush()
    chosen_dates = [randrange(1,365) for i in range(1,365)]
    #print(chosen_dates)
    for i in range(len(chosen_dates) - 1):
        file_maker.chaos()
        res = generate_date()[i]
        date_as_string = datetime.datetime.strptime(res,'%Y-%m-%d')
        date_time_format = '%a %b %d %H:%M:%S %Y %z'
        date_as_string = date_as_string.strftime(date_time_format)
        git_puuuuuush(str(res),date_as_string)
    