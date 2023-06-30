from bs4 import BeautifulSoup

with open('home.html', 'r') as htmlFile:
    inFile = htmlFile.read()
    
    scraper = BeautifulSoup(inFile, 'lxml')
    course_cards = scraper.find_all('div', class_="card")
    for course in course_cards:
        courseName = course.h5.text
        coursePrice = course.a.text.split()[-1]
        print(f'{courseName} costs {coursePrice}')