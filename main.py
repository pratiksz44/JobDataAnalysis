import requests
from bs4 import BeautifulSoup
import xlsxwriter
import os
workbook = xlsxwriter.Workbook("ff.xlsx")
worksheet = workbook.add_worksheet()
row = 0
python = 0
html = 0
p=1
for i in range(1,11):
    url = "https://www.timesjobs.com/candidate/job-search.html?from=submit&luceneResultSize=25&postWeek=60&searchType=Home_Search&cboPresFuncArea=35&pDate=Y&sequence=%d&startPage=1"%(i)
    html_text = requests.get(url).text
    # soup = BeautifulSoup(html_text , 'lxml')
    # jobs = soup.find('li', class_= 'clearfix job-bx wht-shd-bx' )
    # comp_name  = jobs.find('h3' , class_ = 'joblist-comp-name').text.replace(' ','')
    # desc = soup.find('ul' , class_ = 'top-jd-dtl clearfix') #text.replace(' ','')
    # pack = desc.find('li').text
    # dur = pack[11]+"-"+pack[15]+" years"  
    # print(comp_name)
    # print(dur)
    soup2 = BeautifulSoup(html_text , 'lxml')
    jobes = soup2.find_all('li',class_ = 'clearfix job-bx wht-shd-bx')

    for jobs in jobes:
        job_name = jobs.find('header', class_ = 'clearfix').text.replace('  ','')
        location = jobs.find('span').text
        duration = jobs.find('ul',class_="top-jd-dtl clearfix").text.replace(' ','')
        real_du = duration[12]+duration[13]+duration[14] + " years"
        skills = jobs.find('span',class_='srp-skills').text
        job_name = job_name.strip()
        role = jobs.header.h2.a.text.strip()
        comp_name = jobs.header.h3.text.strip()

        worksheet.write(row,0,role)
        worksheet.write(row,1,comp_name)
        worksheet.write(row,2,skills)
        worksheet.write(row,3,real_du)
        worksheet.write(row,4,location)
        print("Role : "+role)
        print("Company Name : "+comp_name)
        print("Duration : " + real_du)
        print("--------------------------------------")
        row = row + 1
        if "python" in skills:
            python += 1
        if "html" in skills:
            html += 1

        # print(python)
        # print(html)
        # print("-----------------------------------------------------------")
worksheet.write(row,1,python)
worksheet.write(row,2,html)
print("python %s" ,python)
print("html %s" ,html)

workbook.close()



