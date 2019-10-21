import datetime as date

def writeLine(mess):
    f = open('log.txt', 'a', encoding='latin-1')
    f.write('\n' + mess)
    f.close()

def succes(mess):
    writeLine(str(date))
    writeLine('Success : ' + mess)

def warning(mess):
    writeLine(str(date))
    writeLine('Warinig : ' + mess)