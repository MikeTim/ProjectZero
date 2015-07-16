def read_file(fname):
    f = open(fname)
    s= f.read()
    f.close
    return s

def get_csv_list(fname):
    text=read_file(fname)
    lines=text.split('\n')
    line_list=[]
    for line in lines:
        line_list.append(line.split(','))
    return line_list

def get_csv_dict(fname):
    no={}
    row=get_csv_list(fname)
    for i in range(4):
        no[row[i][0]]=row[i][1:]
    return no
    
if __name__=='__main__':
    text = read_file('wordlist.csv')
    lines = get_csv_list('wordlist.csv')
    dictionary=get_csv_dict('wordlist.csv')
    #print text
    #print lines
    print dictionary

