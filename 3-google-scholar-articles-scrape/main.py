# from bs4 import BeautifulSoup
# import requests

# keywords = input('Enter keyword/s to search articles in Google Scholar: ')
# start_year = int(input('Please specify the starting year for filtering the results: '))
# end_year = int(input('Please specify the ending year for filtering the results: '))

# url = f"https://scholar.google.com/scholar?start=0&q={keywords.replace(' ', '+')}&hl=en&as_sdt=0,5&as_ylo={start_year}&as_yhi={end_year}"
# response = requests.get(url)

# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, "html.parser")
#     print(soup.prettify())
# else:
#     print("Failed to retrieve data from Google Scholar.")
# print(response.status_code)

from bs4 import BeautifulSoup
import requests
import pandas as pd

keywords = input('Enter keyword/s to search articles in Google Scholar: ')
start_year = int(input('Please specify the starting year for filtering the results: '))
end_year = int(input('Please specify the starting year for filtering the results: '))

articles = []
for i in range(1):
  url = requests.get(f"https://scholar.google.com/scholar?start={i}0&q={keywords.replace(' ', '+')}&hl=en&as_sdt=0,5&as_ylo={start_year}&as_yhi={end_year}").text

  soup = BeautifulSoup(url, "lxml")

  related_articles = soup.find_all('div', class_ = 'gs_r gs_or gs_scl')

  for related_article in related_articles:
      article_name = related_article.find('div', class_='gs_ri').h3.a.text
      article_year_text = related_article.find('div', class_='gs_a').text.split()

      for year in article_year_text:
          if year.isdigit() and len(year) == 4:
              article_year = year

      article_authors = ' '.join(article_year_text[:article_year_text.index('-')])
      article_link = related_article.find('div', class_='gs_ri').h3.a['href']
      articles.append([article_name, article_year, article_authors, article_link])

      # print(f"Article Name: {article_name}\nPublished Year: {article_year}\nAuthor/s: {article_authors}\nArticle Link: {article_link}\n")

  df = pd.DataFrame(articles, columns=['Article Name', 'Published Year', 'Author/s', 'Article Link'])
  df.to_excel('articles.xlsx', index=False)