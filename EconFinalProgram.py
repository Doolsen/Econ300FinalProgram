"""
Drew Olsen
ECON 300
Prof Boulware
Final Project Data Collection Tool
"""

from bs4 import BeautifulSoup
import requests
import xlwt

billList = ["https://www.congress.gov/bill/113th-congress/house-bill/1435/text?q=%7B%22search%22%3A%5B%221435%22%2C%221435%22%5D%7D&r=2&s=6&format=txt", 
            "https://www.congress.gov/bill/113th-congress/house-bill/5790/text?q=%7B%22search%22%3A%5B%225790%22%2C%225790%22%5D%7D&r=15&s=7&format=txt", 
            "https://www.congress.gov/bill/113th-congress/house-bill/1086/text?q=%7B%22search%22%3A%5B%221086%22%2C%221086%22%5D%7D&r=1&s=9&format=txt",
            "https://www.congress.gov/bill/113th-congress/house-bill/2559/text?q=%7B%22search%22%3A%5B%222559%22%2C%222559%22%5D%7D&r=37&s=1&format=txt",
            "https://www.congress.gov/bill/113th-congress/house-bill/4660/text?q=%7B%22search%22%3A%5B%224660%22%2C%224660%22%5D%7D&r=2&s=3&format=txt",
            "https://www.congress.gov/bill/113th-congress/house-bill/675/text?q=%7B%22search%22%3A%5B%22675%22%2C%22675%22%5D%7D&r=7&s=5&format=txt",
            "https://www.congress.gov/bill/113th-congress/house-bill/4766/text?q=%7B%22search%22%3A%5B%224766%22%2C%224766%22%5D%7D&r=1&s=7&format=txt",
            "https://www.congress.gov/bill/113th-congress/house-bill/744/text?q=%7B%22search%22%3A%5B%22744%22%2C%22744%22%5D%7D&r=1&s=9&format=txt",
            "https://www.congress.gov/bill/113th-congress/house-bill/3591/text?q=%7B%22search%22%3A%5B%223591%22%2C%223591%22%5D%7D&r=1&s=1&format=txt",
            "https://www.congress.gov/bill/113th-congress/house-bill/3217/text?q=%7B%22search%22%3A%5B%223217%22%2C%223217%22%5D%7D&r=1&s=3&format=txt",
            "https://www.congress.gov/bill/114th-congress/house-bill/4975/text?q=%7B%22search%22%3A%5B%224975%22%2C%224975%22%5D%7D&r=1&s=2",
            "https://www.congress.gov/bill/114th-congress/house-bill/4617/text?q=%7B%22search%22%3A%5B%224617%22%2C%224617%22%5D%7D&r=2&s=5&format=txt",
            "https://www.congress.gov/bill/114th-congress/house-bill/2638/text?q=%7B%22search%22%3A%5B%222638%22%2C%222638%22%5D%7D&r=2&s=7&format=txt",
            "https://www.congress.gov/bill/114th-congress/house-bill/838/text?q=%7B%22search%22%3A%5B%22838%22%2C%22838%22%5D%7D&r=3&s=9&format=txt",
            "https://www.congress.gov/bill/114th-congress/house-bill/5839/text?q=%7B%22search%22%3A%5B%225839%22%2C%225839%22%5D%7D&r=1&s=1&format=txt",
            "https://www.congress.gov/bill/114th-congress/house-bill/4071/text?q=%7B%22search%22%3A%5B%224071%22%2C%224071%22%5D%7D&r=1&s=3&format=txt",
            "https://www.congress.gov/bill/114th-congress/house-bill/83/text?q=%7B%22search%22%3A%5B%2283%22%2C%2283%22%5D%7D&r=22&s=5&format=txt",
            "https://www.congress.gov/bill/114th-congress/house-bill/4726/text?q=%7B%22search%22%3A%5B%224726%22%2C%224726%22%5D%7D&r=1&s=7&format=txt",
            "https://www.congress.gov/bill/114th-congress/house-bill/6105/text?q=%7B%22search%22%3A%5B%226105%22%2C%226105%22%5D%7D&r=1&s=9&format=txt",
            "https://www.congress.gov/bill/114th-congress/house-bill/850/text?q=%7B%22search%22%3A%5B%22850%22%2C%22850%22%5D%7D&r=3&s=1&format=txt",
            "https://www.congress.gov/bill/115th-congress/house-bill/4618/text?q=%7B%22search%22%3A%5B%224618%22%2C%224618%22%5D%7D&r=1&s=3&format=txt",
            "https://www.congress.gov/bill/115th-congress/house-bill/1863/text?q=%7B%22search%22%3A%5B%221863%22%2C%221863%22%5D%7D&r=3&s=5&format=txt",
            "https://www.congress.gov/bill/115th-congress/house-bill/377/text?q=%7B%22search%22%3A%5B%22377%22%2C%22377%22%5D%7D&r=3&s=7&format=txt",
            "https://www.congress.gov/bill/115th-congress/house-bill/5566/text?q=%7B%22search%22%3A%5B%225566%22%2C%225566%22%5D%7D&r=1&s=9&format=txt",
            "https://www.congress.gov/bill/115th-congress/house-bill/2028/text?q=%7B%22search%22%3A%5B%222028%22%2C%222028%22%5D%7D&r=41&s=1&format=txt",
            "https://www.congress.gov/bill/115th-congress/house-bill/2560/text?q=%7B%22search%22%3A%5B%222560%22%2C%222560%22%5D%7D&r=1&s=3&format=txt",
            "https://www.congress.gov/bill/115th-congress/house-bill/2782/text?q=%7B%22search%22%3A%5B%222782%22%2C%222782%22%5D%7D&r=4&s=5&format=txt",
            "https://www.congress.gov/bill/115th-congress/house-bill/4222/text?q=%7B%22search%22%3A%5B%224222%22%2C%224222%22%5D%7D&r=1&s=7&format=txt",
            "https://www.congress.gov/bill/115th-congress/house-bill/5652/text?q=%7B%22search%22%3A%5B%225652%22%2C%225652%22%5D%7D&r=1&s=9&format=txt",
            "https://www.congress.gov/bill/115th-congress/house-bill/2607/text?q=%7B%22search%22%3A%5B%222607%22%2C%222607%22%5D%7D&r=1&s=1&format=txt",
            "https://www.congress.gov/bill/116th-congress/house-bill/4048/text?q=%7B%22search%22%3A%5B%224048%22%2C%224048%22%5D%7D&r=7&s=8&format=txt",
            "https://www.congress.gov/bill/116th-congress/house-bill/4879/text?q=%7B%22search%22%3A%5B%224879%22%2C%224879%22%5D%7D&r=2&s=4&format=txt",
            "https://www.congress.gov/bill/116th-congress/house-bill/6731/text?q=%7B%22search%22%3A%5B%226731%22%2C%226731%22%5D%7D&r=1&s=5&format=txt",
            "https://www.congress.gov/bill/116th-congress/house-bill/6774/text?q=%7B%22search%22%3A%5B%226774%22%2C%226774%22%5D%7D&r=1&s=6&format=txt",
            "https://www.congress.gov/bill/116th-congress/house-bill/1378/text?q=%7B%22search%22%3A%5B%221378%22%2C%221378%22%5D%7D&r=2&s=8&format=txt",
            "https://www.congress.gov/bill/116th-congress/house-bill/5282/text?q=%7B%22search%22%3A%5B%225282%22%2C%225282%22%5D%7D&r=2&s=9&format=txt",
            "https://www.congress.gov/bill/116th-congress/house-bill/6360/text?q=%7B%22search%22%3A%5B%226360%22%2C%226360%22%5D%7D&r=1&s=10&format=txt",
            "https://www.congress.gov/bill/116th-congress/house-bill/4502/text?q=%7B%22search%22%3A%5B%224502%22%2C%224502%22%5D%7D&r=3&s=2&format=txt",
            "https://www.congress.gov/bill/116th-congress/house-bill/2518/text?q=%7B%22search%22%3A%5B%222518%22%2C%222518%22%5D%7D&r=1&s=4&format=txt",
            "https://www.congress.gov/bill/116th-congress/house-bill/664/text?q=%7B%22search%22%3A%5B%22664%22%2C%22664%22%5D%7D&r=7&s=6&format=txt",
            "https://www.congress.gov/bill/117th-congress/house-bill/3644/text?q=%7B%22search%22%3A%5B%223644%22%2C%223644%22%5D%7D&r=1&s=7&format=txt",
            "https://www.congress.gov/bill/117th-congress/house-bill/171/text?q=%7B%22search%22%3A%5B%22171%22%2C%22171%22%5D%7D&r=14&s=8&format=txt",
            "https://www.congress.gov/bill/117th-congress/house-bill/5624/text?q=%7B%22search%22%3A%5B%225624%22%2C%225624%22%5D%7D&r=1&s=9&format=txt",
            "https://www.congress.gov/bill/117th-congress/house-bill/597/text?q=%7B%22search%22%3A%5B%22597%22%2C%22597%22%5D%7D&r=9&s=10&format=txt",
            "https://www.congress.gov/bill/117th-congress/house-bill/2840/text?q=%7B%22search%22%3A%5B%222840%22%2C%222840%22%5D%7D&r=2&s=1&format=txt",
            "https://www.congress.gov/bill/117th-congress/house-bill/3460/text?q=%7B%22search%22%3A%5B%223460%22%2C%223460%22%5D%7D&r=2&s=3&format=txt",
            "https://www.congress.gov/bill/117th-congress/house-bill/4404/text?q=%7B%22search%22%3A%5B%224404%22%2C%224404%22%5D%7D&r=1&s=4&format=txt",
            "https://www.congress.gov/bill/117th-congress/house-bill/848/text?q=%7B%22search%22%3A%5B%22848%22%2C%22848%22%5D%7D&r=6&s=5&format=txt",
            "https://www.congress.gov/bill/117th-congress/house-bill/1634/text?q=%7B%22search%22%3A%5B%221634%22%2C%221634%22%5D%7D&r=1&s=6&format=txt",
            "https://www.congress.gov/bill/117th-congress/house-bill/2807/text?q=%7B%22search%22%3A%5B%222807%22%2C%222807%22%5D%7D&r=1&s=7&format=txt"]

saveSheet = xlwt.Workbook()
dataSheet = saveSheet.add_sheet("Use of gendered language")

headerFont = xlwt.Font()
headerFont.name = "Arial"
headerFont.bold =True

headerStyle = xlwt.XFStyle()
headerStyle.font = headerFont

dataSheet.write(0, 0, "Father Count", headerStyle)
dataSheet.write(0, 1, "Mother Count", headerStyle)
dataSheet.write(0, 2, "He Count", headerStyle)
dataSheet.write(0, 3, "She Count", headerStyle)
dataSheet.write(0, 4, "Him Count", headerStyle)
dataSheet.write(0, 5, "Her Count", headerStyle)
dataSheet.write(0, 6, "His Count", headerStyle)
dataSheet.write(0, 7, "Hers Count", headerStyle)
dataSheet.write(0, 8, "Mr. Count", headerStyle)
dataSheet.write(0, 9, "Ms. Count", headerStyle)
dataSheet.write(0, 10, "Mrs. Count", headerStyle)
dataSheet.write(0, 11, "Total", headerStyle)

iterationCount = 1
for i in billList:
    page = requests.get(i) #NOTE: Bill has to be in txt format
    print(page.status_code)


    scraper = BeautifulSoup(page.content, "html.parser")
    scraperX = str(scraper.find("pre", id="billTextContainer"))
    x = scraperX.split(" ")

    for l in range(len(x)):
        x[l] = x[l].lower()
   
    DadCounter = 0
    MomCounter = 0
    HeCounter = 0
    SheCounter = 0
    HimCounter = 0
    HerCounter = 0
    HisCounter = 0
    HersCounter = 0
    MrCounter = 0
    MsCounter = 0
    MrsCounter = 0
    totalCounter = 0
   
    for jobFind in x:
        if(jobFind is None):
            continue
        if(jobFind == "father"):
            DadCounter += 1
            totalCounter += 1
            print(jobFind)
        elif(jobFind == "mother"): 
            MomCounter += 1
            totalCounter += 1
            print(jobFind)
        elif(jobFind == "he"): 
            HeCounter += 1
            totalCounter += 1
            print(jobFind)
        elif(jobFind == "she"): 
            SheCounter += 1
            totalCounter += 1
            print(jobFind)
        elif(jobFind == "him"): 
            HimCounter += 1
            totalCounter += 1
            print(jobFind)
        elif(jobFind == "her"): 
            HerCounter += 1
            totalCounter += 1
            print(jobFind)
        elif(jobFind == "his"): 
            HisCounter += 1
            totalCounter += 1
            print(jobFind)
        elif(jobFind == "hers"): 
            HersCounter += 1
            totalCounter += 1
            print(jobFind)
        elif(jobFind == "mr."): 
            MrCounter += 1
            totalCounter += 1
            print(jobFind)
        elif(jobFind == "ms."): 
            MsCounter += 1
            totalCounter += 1
            print(jobFind)
        elif(jobFind == "mrs."): 
            MrsCounter += 1
            totalCounter += 1
            print(jobFind)
    print(totalCounter)
    dataSheet.write(iterationCount, 0, DadCounter)
    dataSheet.write(iterationCount, 1, MomCounter)
    dataSheet.write(iterationCount, 2, HeCounter)
    dataSheet.write(iterationCount, 3, SheCounter)
    dataSheet.write(iterationCount, 4, HimCounter)
    dataSheet.write(iterationCount, 5, HerCounter)
    dataSheet.write(iterationCount, 6, HisCounter)
    dataSheet.write(iterationCount, 7, HersCounter)
    dataSheet.write(iterationCount, 8, MrCounter)
    dataSheet.write(iterationCount, 9, MsCounter)
    dataSheet.write(iterationCount, 10, MrsCounter)
    dataSheet.write(iterationCount, 11, totalCounter)
    iterationCount += 1

saveSheet.save("ECON300FinalData.xls") #NOTE: Don't have file open when code is run otherwise error will be thrown

