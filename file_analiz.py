import magic
import os
import time
import hashlib
import argparse






def get_type_of_file(file):
    try:
        return magic.from_file(file, mime=True)
    except IsADirectoryError:
        return 'directory:'
    except FileNotFoundError:
        return 'file_not_found'


def md5(fname):
    try:
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except IsADirectoryError:
        return '0'
    except FileNotFoundError:
        return 'file_not_found'

def get_size_of_file(file):
    try:
        return os.path.getsize(file)
    except FileNotFoundError:
        return 'file_not_found'



def get_data_created_of_file(file):
    try:
        return time.ctime(os.path.getctime(file))
    except FileNotFoundError:
        return 'file_not_found'


def get_last_modified_of_file(file):
    try:
        return time.ctime(os.path.getmtime(file))
    except FileNotFoundError:
        return 'file_not_found'

def get_data_in_archive(file):
    a = os.popen("7z l "+file).read()
    try:
        return "".join(a.split('\n')[14:-1])
    except FileNotFoundError:
        return 'file_not_found'



def file_inf(file):
    archives = ['application/gzip', 'application/x-xz', 'application/x-7z-compressed', 'application/zlib',
                'application/zip', 'application/x-bzip2']
    obj={}
    obj['file']=file
    try:
        obj['type']=get_type_of_file(file)
    except RecursionError:
        obj['type']='not identific'
    obj['size']=get_size_of_file(file)
    obj['data_created']=get_data_created_of_file(file)
    obj['data_last_mod']=get_last_modified_of_file(file)
    obj['md5']=md5(file)
    obj['7z']=None
    if obj['type'].strip() in archives:
        obj['7z'] =get_data_in_archive(file)

    for i in obj.keys():
        obj[i]=str(obj[i])
        obj[i]='"'+obj[i]+'"'

    return obj['file']+';'+obj['size']+';'+obj['type']+';'+obj['7z']+';'+obj['md5']+';'+obj['data_created']+';'+obj['data_last_mod']+'\n'


def create(file_for_read,file_for_out):
    first_string='file;size;type;7z;md5;data_created;data_last_mod\n'
    #open(file_for_out, 'a').writelines(first_string)
    for i in open(file_for_read,'r'):
        open(file_for_out,'a').writelines(file_inf(i.strip()))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--input', help='file for input',default='this_file.txt')
    parser.add_argument('-o','--output', help='file for output',default='out.csv')
    parser.add_argument('-d','--dir',help='dirictory for analitics',default='./')
    args = parser.parse_args()

    if args.input=='this_file.txt':
        os.popen("find " + args.dir+' >this_file.txt').read()

        time.sleep(3)

    create(file_for_read=args.input,file_for_out=args.output)

if __name__ == '__main__':
    main()