class StudentData:
    def __init__(self):
        self.info = list()
        self.index=1

    def insertInfo(self,name,score):
        self.info.append(self.index)
        self.info.append(name)
        self.info.append(score)
        print(self.info)

    def deleteInfo(self,delnum):
        if(len(self.info)==3):
            for i in range(0,3):
                self.info.pop(0)
            self.index=1
            print(self.index)

        else:
            print(delnum)
            dnum=self.info.index(delnum)
            print(delnum)
            # 삭제값 이전의 번호를 1 증가시킴
            for i in range(0,dnum):
                if(i % 3 ==0):
                    self.info[i] +=1
            # 번호 이름 점수 (3개 삭제)
            for i in range(0,3):
                self.info.pop(dnum)

            #모든 번호를 1 감소
            leng = len(self.info)
            for i in range(0,leng):
                if(i % 3 ==0):
                    self.info[i] -=1
            if(self.info.index==0):
                self.info.index=1
            #print(self.info[0])

    def printData(self):
        last = len(self.info)
        for i in range (0,last):
            if(i % 3 ==0):
                print("%d ,%s , %d " % (self.info[i], self.info[i+1],self.info[i+2] ) )
"""
if __name__=='__main__':
    test = StudentData()
    test.insertInfo("ho",100)

    #test.insertInfo("dkdk",200)
    #test.insertInfo("akak",300)
    #test.insertInfo("dodo",400)
    #test.insertInfo("zlzl",500)
    #test.insertInfo("kkkk",600)
    test.printData()
    test.deleteInfo(0)
    test.printData()
"""
