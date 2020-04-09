import re

def getDates(track):
    fileInput = open(track, mode='r', encoding='utf8')
    fileDates = fileInput.read()

    model = re.compile(r'(\d{4})/(\d{2})/(\d{2})((\s+)?(\d{2})?(:\d{2})?(:\d{2})?)?')

    allDate = model.finditer(fileDates)

    for item in allDate:
        strItemDates = int(item.group(1))
        if strItemDates >= 1000 and strItemDates <= 2012:
            print(item.group())

if __name__ == "__main__":
    getDates("input.txt")
