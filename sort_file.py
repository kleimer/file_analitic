for i in open('all_file_size_2','r',errors='ignore'):
    i=i.strip()
    n=0
    for j in open(i,'r',errors='ignore'):
        if n>50:
            break
        print(j)

    reshenie=input('Y/n:')
    if reshenie=='':
        open('file_to_elastic.txt', 'a').writelines(i.strip() + '\n')
    elif reshenie=='s':
        open('file_skip.txt', 'a').writelines(i.strip() + '\n')

    else:
        open('file_email:passwd.txt', 'a').writelines(i.strip() + '\n')


