import csv
import json
import _csv
from hash_identific import identify_hashes



def is_csv(file):
    serps = [':', ';', ',', ' ', '|', '\t']
    for serp in serps:
        local_array=[]
        with open(file, newline='') as csvfile:
            try:
                spamreader = csv.reader(csvfile, delimiter=serp, quotechar='"')
                for i in spamreader:
                    local_array.append(len(i))
            except _csv.Error:
                return None
        if len(set(local_array))==1 and local_array[0]>1:
            return serp,local_array[0]
    return None

def is_json(file):
    for i in open(file,'r'):
        try:
            #print(i.strip())
            json.loads(i.strip())
            return True
        except json.decoder.JSONDecodeError:
            return False

def is_sql(file):
    keyword=['oracle','mysql','sql','database','dump','host','version','mysqldumper','create', 'table','server']
    all_string=' '.join(open(file,'r').readlines())
    all_string=all_string.lower()
    tmp=0
    for i in keyword:
        if i in all_string:
            tmp+=1
    if tmp >=2:
        return True
    else:
        return False














def create_test_file(file, n=10):
    open('tmp_file','w').close()
    num_string = 0
    try:
        for i in open(file,'r',errors='ignore'):
            if num_string==n:
                break
            num_string+=1
            open('tmp_file','a').writelines(i)
    except UnicodeDecodeError:
        print(file)
        exit(0)

def file_struct_detect(file):
    create_test_file(file=file)
    tmp_file='tmp_file'

    sep=is_csv(tmp_file)


    if sep:
        return {'type':'csv','serp':sep[0],'size':sep[1]}
    if is_json(tmp_file):
        return {'type':'json'}
    if is_sql(tmp_file):
        return {'type':'sql'}
    return None





def main():
    file='/media/liks/ssd/BD/BD/nulled.io.sql/nulled.cr.sql'
    print(file_struct_detect(file))



if __name__ == '__main__':
    main()


