##请把下面numpy改成你自己的包
import numpy as modue_name

write_list = dir(modue_name)

##这是保存文件的位置
##
file_where = open("d:/numpy.txt","w")
allnum = len(write_list)
lennum = 0
file_where.write("***这个(库/包)共有\000\000"+str(allnum)+"\000\000个函数***\n\n")
##
for write_list_num in write_list:
    lennum=lennum+1
    write_num=str(lennum)
    file_where.write(write_num.rjust(5,"-")+"\000\000"+"-\000"+write_list_num+"\n")
    
file_where.close()
