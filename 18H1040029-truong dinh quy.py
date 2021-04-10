import cmath
import random
class person:
    def __init__(self,STT,Name,Age,Gender):
        self.STT=STT
        self.Age=Age
        self.Name=Name
        self.Gender=Gender
    def ho_ten(self):
         for i in range(0,self.STT):
            hoten=str(input("nhập họ tên SV thứ {}: ".format(i+1)))
            self.Name.append(hoten)
         return self.Name
    def tuoi(self):
        for i in range(0,self.STT):
            sotuoi=int(random.randrange(17,25))
            self.Age.appennd(sotuoi)
        return self.Age
    def gioi_tinh(self):
        for i in range(0,self.STT):
            gt=str("SV thu {}: ".format(i+1))
            self.Gender.append(gt)
        return self.Gender
class student(person):
    def __init__(self,n):
        super().__init__(n)
        self.Id=[]
        self.Class=[]
        self.grade=[]
        self.Danhsach=[]
    def nhapId(self):
        for i in range(0,self.STT):
            Idsv=int(input("nhập số Id cho SV thứ {} : ".format(i+1)))
            self.Id.append(IDsv)
        return self.Id
    def lop_hoc(self):
        for i in range(0,self.STT):
            lhoc=str(input("nhập tên lớp cho SV thứ {} : ".format(i+1)))
            self.Class.append(lhoc)
        return self.Class
    def diem(self):
        for i in range(0,self.STT):
            dso=int(input("nhập điểm cho SV thứ {} : ".format(i+1)))
            self.grade.append(dso)
        return self.grade
    def sothutu(self):
        for i in range(0,self.STT):
            A={"H&T của SV thu {} : ".format(i):self.Name}
            self.Danhsach.update(A)
            B={"tuổi của SV {} : ".format(i):self.Age}
            self.Danhsach.update(B)
            C={"gt của SV {} : ".format(i):self.Age}
            self.Danhsach.update(C)
            D={"mã số của SV {} : ".format(i):self.Id}
            self.Danhsach.update(D)
            E={"lớp của SV {} : ".format(i):self.Class}
            self.Danhsach.update(E)
            F={"điểm của SV {} : ".format(i):self.grade}
            self.Danhsach.update(F)
class text:
    def __init__(self,n):
        super.__init__(self,n)
class complex:
    def __init__(self,n,real,image):
        super.__init__(real,image)
        self.real=real
        self.image=image
    def module_complex(self):
        a=cmath.sqrt(comlplex(self.real,self.image))
        return a