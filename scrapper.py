import requests
from bs4 import BeautifulSoup
Url = 'http://results.jssstuniv.in/check.php'

file = open("results.txt","w")

def calculate_gpa(grade,credit):
        gpa = 0
        for i in range(0,8):
            if grade[i].strip() == "S":
                gpa += credit[i] * 10
            elif grade[i].strip() == "A":
                gpa += credit[i] * 9
            elif grade[i].strip() == "B":
                gpa += credit[i] * 8
            elif grade[i].strip() == "C":
                gpa += credit[i] * 7
            elif grade[i].strip() == "D":
                gpa += credit[i] * 5
            elif grade[i].strip() == "E":
                gpa += credit[i] * 4
            elif grade[i].strip() == "F":
                gpa += credit[i] * 0
        Name = soup.find('div', id='HTMLtoPDF').find('h1').text
        Data[Name] = str(gpa/25)

        file.write(Name+"\t"+str(gpa/25)+'\n')

        print(usn+"\t"+soup.find('div', id='HTMLtoPDF').find('h1').text+"\t"+str(gpa/25))

Data = {}
for i in range(1,190):
    usn = "01JST18CS"+f"{i:03d}"
    login_data = {'USN':usn}
    page = requests.post(url = Url,data = login_data)        
    soup = BeautifulSoup(page.content,'lxml')

    try:
        soup.find('div', id='HTMLtoPDF').find('h1').text
        if soup.find('table',type="result").find('td').text.strip() == "CH110":
            continue

    except:
        print("Invalid Usn")
        continue


    


    grade = []

    for i in range(1,9):
        find_grade = "grade"+str(i)
        try:
            grade.append(soup.find('table',type="result").find('td',id=find_grade).text)
        except:
            grade.append('F')
    credit = []

    
    for tr in soup.find('table',type="result").find_all('tr'):
        subject = tr.find('td')
        if subject != None:
            if subject.text.strip() == 'CS310' or subject.text.strip() == 'CS330':
                credit.append(3)
            elif subject.text[-2] == "L":
                credit.append(1.5)
            elif subject.text.strip() == 'HU320':
                credit.append(0)
            else:
                credit.append(4)

    calculate_gpa(grade,credit)

file.close()

# for Name in Data:
#     print(Name+"\t"+Data[Name])