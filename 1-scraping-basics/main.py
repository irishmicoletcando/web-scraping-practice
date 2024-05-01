from bs4 import BeautifulSoup

# to open a file and read the content of the file
with open('home.html', 'r') as html_file:
  content = html_file.read()
  # print(content)

  # instance of BeautifulSoup
  # pass the parse method (lxml) as string
  soup = BeautifulSoup(content, 'lxml')
  
  # print html in prettier way
  # print(soup.prettify())

  # grab all h5 tags
  # .find() -> searches the first element
  courses_html = soup.find_all('h5')
  # print(courses_html)

  # for course in courses_html:
    # print(course.text)

  # grab all the course card
  # need to place an underscore in class since there is a class method in python
  course_cards = soup.find_all('div', class_='card')
  print(course_cards)
  for course in course_cards:
    course_name = course.h5.text
    course_price_text = course.a.text.split()[-1]
    print(f"{course_name} costs for {course_price_text}.")