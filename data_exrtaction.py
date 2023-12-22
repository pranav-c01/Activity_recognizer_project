import os,shutil,csv
parent_dir = os.getcwd()
path_er = [i for i in os.listdir() if os.path.isdir(i)]
le = ["time,avg_rss12,var_rss12,avg_rss13,var_rss13,avg_rss23,var_rss23\n"]
ke,je = [],[]
try:
    for i in path_er:
        er=os.path.join(parent_dir,i)
        for j in os.listdir(er):
            file_path = os.path.join(er,j)
            if file_path==r"C:\Users\Pranav_coding\Desktop\Logistic_reg_project\AReM\bending2\dataset4.csv":
                count=1
                reader = csv.reader(open("bending2\dataset4.csv", "r"), delimiter=' ')
                for r in reader:
                    if count>5:
                        le.append(r[:6])
                    count+=1
                
            else:
                with open(file_path) as f:
                    le.extend(f.readlines()[5:])
        
    with open("net_dataset.csv",'w') as f:
        f.writelines(le)

    # sending all other files into another dir
    # os.mkdir("scrap_data")
    # for i in path_er:
    #     shutil.move(i,'scrap_data')
except Exception as e:
    print(e)