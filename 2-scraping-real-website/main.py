from bs4 import BeautifulSoup
import requests
import re
import time

most_proficient_skill = input('Please enter your most proficient skill or programming language: ')
keywords = '+'.join(most_proficient_skill.split())

def find_jobs():
    # to avoid response [200] write .text at the end of the requests.get
    html_text = requests.get(f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords={keywords}&txtLocation=').text

    print("Filtering out results...")

    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        # filtering only the job posts that are posted today
        job_posted_date = job.find('span', class_='sim-posted').span.text

        if job_posted_date == 'Posted today':
            # since the company name is inside the li element
            job_name = job.find('h2').a.text.title()
            company_name = re.sub(r'\s+', ' ', job.find('h3', class_='joblist-comp-name').text.title().strip())
            
            # Split skills by comma, strip whitespace, and join with comma
            skills = job.find('span', class_='srp-skills').text.strip()
            skills = ', '.join(skill.strip() for skill in skills.split(','))

            job_link = job.header.h2.a['href']
            with open(f'posts/{index}.txt', 'w') as f:
                f.write(f"Job Title: {job_name.strip()}\n")
                f.write(f"Company Name: {company_name.strip()}\n")
                f.write(f"Skills Required: {skills.strip()}\nMore info: {job_link}")
            print(f"File saved!")

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)
