import rpa as r
import urllib as urllib
import re
import datetime
import csv


def GoToWeb():
    r.init()

    # listPigs = []

    i = 1000
    chunk = 20
    RunUntil = i + chunk

    GTG = True
    while GTG == True:
        listPigs = []
        try:
            newUrl = f'https://www.cpspedigrees.com/poland/pigs/show/{i}'
            r.url(newUrl)

            pigInstance = Pig()

            pigInfo = r.read('ul')

            if pigInfo == '':
                GTG = False

            regNum = re.search('Registration#:\n(.*)\n', pigInfo)
            regNum = regNum.group(1).strip()
            pigInstance.regNum = regNum

            Sex = re.search('Sex:\n(.*)\n', pigInfo)
            Sex = Sex.group(1).strip()
            pigInstance.Sex = Sex

            pigInstance.FullName = r.read('show-pig-fullname')

            DOB = re.search('Farrow Date:\n(.*)\n', pigInfo)
            DOB = DOB.group(1).strip()
            pigInstance.DOB = DOB

            Owner = re.search('Owner:\n(.*)\n', pigInfo)
            Owner = Owner.group(1).strip()
            pigInstance.Owner = Owner

            Breeder = re.search('Breeder:\n(.*)\n', pigInfo)
            Breeder = Breeder.group(1).strip()
            pigInstance.Breeder = Breeder

            TotalBorn = re.search('Total Born:\n(.*)\n', pigInfo)
            TotalBorn = TotalBorn.group(1).strip()
            pigInstance.TotalBorn = TotalBorn

            BornAlive = re.search('Born Alive:\n(.*)\n', pigInfo)
            BornAlive = BornAlive.group(1).strip()
            pigInstance.BornAlive = BornAlive

            SireRegNum = r.read(
                '/html/body/div[1]/div[4]/div/div[2]/div[2]/div/div/strong[1]')
            pigInstance.SireRegNum = SireRegNum

            DamRegNum = r.read(
                '/html/body/div[1]/div[4]/div/div[2]/div[6]/div/div/strong[1]')
            pigInstance.DamRegNum = DamRegNum

            listPigs.append(pigInstance)

            # if i >= chunk
            if i >= RunUntil:
                ExportPigListToCSV(listPigs, "Pigs.csv")
                listPigs.clear()
                RunUntil = i + chunk
            i += 1

        except Exception:
            GTG == False
    try:
        ExportPigListToCSV(listPigs, "Pigs.csv")
    except BaseException as e:
        print(f'BaseException: {e}')
    else:
        print('Data has been loaded successfully !')


def ExportPigListToCSV(listPigs, filename):
    with open(filename, 'a') as f:
        writer = csv.writer(f)
        j = 0
        for item in listPigs:
            j += 1
            writer.writerow([j, item.FullName, item.regNum, item.Sex, item.DOB, item.Owner,
                             item.Breeder, item.TotalBorn, item.BornAlive, item.SireRegNum, item.DamRegNum])
    return filename


def StringToFile(text, output):
    f = open(output, "a")
    f.write(text)
    f.close()


def IngestWebContent(urlPath):
    fp = urllib.urlopen(urlPath)
    myBytes = fp.read()

    myStr = myBytes.decode('utf8')

    fp.close()
    StringToFile(myStr, )

    ###main entry point###


class Pig:
    def __init__(self):
        self.regNum = 0
        self.Sex = ""
        self.DOB = datetime.datetime.now()
        self.Owner = ""
        self.Breeder = ""
        self.TotalBorn = 0
        self.BornAlive = 0
        self.SireRegNum = 0
        self.DamRegNum = 0
        self.FullName = ""
###KEEP AT BOTTOM###


def main():
    GoToWeb()


if __name__ == "__main__":
    main()
###End of main entry###
