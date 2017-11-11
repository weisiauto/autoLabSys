import pickle
import os
'''
使用pickle模块存取示例
pickle模块采用2禁止快速存取数据

'''
str1=os.getcwd()
file=str1+'\\mylist.pkl'

def pickleSave(pickle_file):
    pickle_file=open(file,'wb')
    mylist=[1231,3.1415926,'魏智勇',["Henry","Joanna","John"]]    
    pickle.dump(mylist,pickle_file)
    pickle_file.close()

def pickleLoad(pickle_file):
    pickle_file=open(file,'rb')
    my_list=pickle.load(pickle_file)
    pickle_file.close()
    return my_list


if __name__=='__main__':
    
    pickleSave(file)
    print(pickleLoad(file))
