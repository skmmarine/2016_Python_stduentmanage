#-*- coding: utf-8 -*-
from tkinter import *
from StudentData import *
from MakeError import *
window = Tk()

allStudent = StudentData()
entInput=[Entry,Entry,Entry,Entry,Entry]
entInput[0] = Entry(window, width= 20 , bg="light green")
entInput[0].grid(row=0, column = 1, sticky = W)

def numsort():
    numSortList = allStudent.info[:]
    for i in range(0,len(numSortList)):
        if(i %3 !=0):
            continue
        for j in range(0,len(numSortList)):
            if(j %3 !=0):
                continue
            if(numSortList[i] < numSortList[j]):
                x=i ; y=j
                for z in range(0,3):
                    temp=numSortList[y]
                    numSortList[y] =numSortList[x]
                    numSortList[x] = temp
                    x +=1; y +=1
    output.delete(0.0,END)
    for i in range(0,len(numSortList)):
        if(i%3 ==0):
            output.insert(END,"%d\t%s\t%s\n" %(numSortList[i] ,numSortList[i+1] ,numSortList[i+2]))
    output2.delete(0.0,END)
    output2.insert(END,"numsort success")

def namesort():
    nameSortList = allStudent.info[:]
    for i in range(0,len(nameSortList)):
        if(i %3 !=1):
            continue
        for j in range(0,len(nameSortList)):
            if(j %3 !=1):
                continue
            if(nameSortList[i] < nameSortList[j]):
                x=i-1 ; y=j-1
                for z in range(0,3):
                    temp=nameSortList[y]
                    nameSortList[y] =nameSortList[x]
                    nameSortList[x] = temp
                    x +=1; y +=1
    output.delete(0.0,END)
    for i in range(0,len(nameSortList)):
        if(i%3 ==0):
            output.insert(END,"%d\t%s\t%s\n" %(nameSortList[i] ,nameSortList[i+1] ,nameSortList[i+2]))
    output2.delete(0.0,END)
    output2.insert(END,"namesort success")

def downsort():
    downSortList = allStudent.info[:]
    for i in range(0,len(downSortList)):
        if(i %3 !=2):
            continue
        for j in range(0,len(downSortList)):
            if(j %3 !=2):
                continue
            if(int(downSortList[i]) < int(downSortList[j])):
                x=i-2 ; y=j-2
                for z in range(0,3):
                    temp=downSortList[y]
                    downSortList[y] =downSortList[x]
                    downSortList[x] = temp
                    x +=1; y +=1
    output.delete(0.0,END)
    for i in range(0,len(downSortList)):
        if(i%3 ==0):
            output.insert(END,"%d\t%s\t%s\n" %(downSortList[i] ,downSortList[i+1] ,downSortList[i+2]))
    output2.delete(0.0,END)
    output2.insert(END,"downsort success")

def upsort():
    upSortList = allStudent.info[:]
    for i in range(0,len(upSortList)):
        if(i %3 !=2):
            continue
        for j in range(0,len(upSortList)):
            if(j %3 !=2):
                continue
            if(int(upSortList[i]) > int(upSortList[j])):
                x=i-2 ; y=j-2
                for z in range(0,3):
                    temp=upSortList[y]
                    upSortList[y] =upSortList[x]
                    upSortList[x] = temp
                    x +=1; y +=1
    output.delete(0.0,END)
    for i in range(0,len(upSortList)):
        if(i%3 ==0):
            output.insert(END,"%d\t%s\t%s\n" %(upSortList[i] ,upSortList[i+1] ,upSortList[i+2]))
    output2.delete(0.0,END)
    output2.insert(END,"upsort success")

def insert():
    output2.delete(0.0,END)
    if(entInput[0].get() == ""):
        output2.insert(END,"please input name")
    elif(entInput[0].get() in allStudent.info):
        output2.insert(END,"already exist student name")
    elif(entInput[1].get() == ""):
        output2.insert(END,"please input score")
    else:
        try:
            scoreCheck=int(entInput[1].get())

            if( scoreCheck  <=0 ):
                raise ValueError
        except ValueError:
            output2.delete(0.0,END)
            output2.insert(END,"Insert Error : use int type")
            return

        allStudent.insertInfo(entInput[0].get(), entInput[1].get())
        if(allStudent.index==0):
            allStudent.index +=1
        output.insert(END,"%d\t%s\t%s\n" %(allStudent.index , entInput[0].get() , entInput[1].get()))

        allStudent.index +=1
        output2.delete(0.0,END)
        output2.insert(END,"Insert success")
        entInput[0].delete(0,END)
        entInput[1].delete(0,END)

def delete():
    output2.delete(0.0,END)
    if(entInput[2].get() == ""):
        output2.insert(END,"please input delete num")
    else:
        try:
            deleteCheck=int(entInput[2].get())
            if( (deleteCheck in allStudent.info) == False):
                raise not_exist_error()
        except ValueError:
            output2.insert(END,"Delete Error : use int type")
            return
        except not_exist_error:
            output2.insert(END,"Delete Error : not exist number")
            return

        delnum = eval(entInput[2].get())
        allStudent.deleteInfo(delnum)
        output.delete(0.0,END)
        for i in range(0,len(allStudent.info)):
            if(i%3 ==0):
                output.insert(END,"%d\t%s\t%s\n" %(allStudent.info[i] ,allStudent.info[i+1] ,allStudent.info[i+2]))

        allStudent.index -=1
        output2.insert(END,"delete success")
        entInput[2].delete(0,END)

def save():
    F_name = str(entInput[3].get())
    if(F_name[-3:] != "txt"):
        entInput[3].delete(0,END)
        entInput[3].insert(END,"please use txt file")
    else:
        f = open(F_name,'w')    #mode W because we not need to before data
        for i in range(0,len(allStudent.info)):
            if(i != 0 ):
                if( i%3 ==0):
                    f.write(": ")
            if(i==0):
                f.write(" ")
            f.write( str(allStudent.info[i]) )
            f.write(" ")
        #f.write(str(allStudent.info))
        f.close()
        output2.delete(0.0,END)
        output2.insert(END,"save file success")

def openf():
    F_name = str(entInput[4].get())
    try:
        if(F_name[-3:] != "txt"):
            entInput[4].delete(0,END)
            entInput[4].insert(END,"please use txt file")
        else:
            allStudent.info = list()

            output.delete(0.0,END)
            f = open(F_name,'r')
            line = f.read()
            lines = line.split(':');

            allStudent.index=1
            for i in range(0,len(lines)):
                real_lines=lines[i].split(' ')
                allStudent.insertInfo(real_lines[2] , real_lines[3])
                output.insert(END,"%d\t%s\t%s\n" %(allStudent.index ,real_lines[2] ,real_lines[3]))

                allStudent.index +=1
            f.close()
            output2.delete(0.0,END)
            output2.insert(END,"load file success")
    except FileNotFoundError:
        output2.delete(0.0,END)
        output2.insert(END,"file not exist")
    except IndexError:
        output2.delete(0.0,END)
        output2.insert(END,"please check file format")

insertInfo = ["점수:","번호:","파일이름:","파일이름:"]
buttonInfo = ["추가","삭제","저장","열기"]

butFunc =[insert,delete,save,openf]                    #버튼에 쓸 키워드
sortInfo = ["번호순","이름순","점수내림차순","점수오름차순"]
sortFunc = [numsort , namesort , downsort , upsort]

insertInfo_len={"점수:" :7 , "번호:" : 5 ,"파일이름:" : 20, }
insertInfo_col={"점수:" :"light green","번호:" :"light green",\
    "파일이름:":"light blue"}
sortInfo_len={"번호순":5,"이름순":5,"점수내림차순":15,"점수오름차순":15}

Label(window, text="이름 :").grid(row=0 , column=0 , sticky = W)

makeview_num = 0
entInput_num =0

for label in buttonInfo:
    Button(window , text = str(label) , width = 5, command = butFunc[entInput_num])\
    .grid(row =makeview_num, column = 4)
    makeview_num +=1
    entInput_num +=1
makeview_num = 0
entInput_num =0

sort_F = Frame(window)
sort_F.grid(row =4, column =1,columnspan = 3)
for label in sortInfo:
    Button(sort_F, text=str(label),width = sortInfo_len[label] , command = sortFunc[entInput_num])\
    .grid(row=4,column=makeview_num)
    makeview_num+=1
    entInput_num+=1
makeview_num = 0

#define frame
output_F = Frame(window)
output2_F = Frame(window)
output_F.grid(row=5, column=0,columnspan=6)
output2_F.grid(row=6, column=0,columnspan=6)

output = Text(output_F , width = 65 , height = 6 ,wrap = WORD ,background = "light green")
output.grid()
output2 = Text(output_F , width = 65 , height = 1 ,wrap = WORD ,background = "yellow")
output2.grid()

############################make label
makeview_num=0
entInput_num =1
for label in insertInfo:
    Label(window, text=str(label)).grid(row=makeview_num,column=2, sticky = E);

    entInput[entInput_num] = Entry(window, width= insertInfo_len[label] , bg=insertInfo_col[label])
    entInput[entInput_num].grid(row=makeview_num, column = 3, sticky = W)
    makeview_num+=1
    entInput_num+=1
#########################################
if __name__=='__main__':
    test = StudentData()
    #test.insertInfo("dkdk",200)
    #test.insertInfo("akak",300)
    #test.insertInfo("dodo",400)
    #test.insertInfo("zlzl",500)
    #test.insertInfo("kkkk",600)
    test.printData()
    #test.deleteInfo(1)
    print("after del")
    print(test.index)
    test.insertInfo("user1",100)
    print(test.index)
    test.insertInfo("user2",200)
    test.printData()
    #test.deleteInfo(1)
    print("after del2")
    test.printData()