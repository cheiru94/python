class Idcard :
    def __init__(self,name,sex,age,major) :
        self.name = name 
        self.sex = sex 
        self.age = age 
        self.major = major 
        print(f"이름은 {name}이고 성별은 {sex}입니다. 나이는{age}살\
            대학에서 주전공은 {major} 전공으로 있습니다.")
student1 = Idcard("이재일","남성","29","컴퓨터")
student2 = Idcard("이재성","남성","27","삼성전자")