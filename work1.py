'''
编写学员实体类 Student，对应成员变量包含：学号 id、姓名 name、性别 sex；
编写学员管理类 StudentManagement ，实现添加学员方法 addStudent()。
编写StudentManagement的main()方法进行学员信息的添加：
学号：1001,姓名：张三,性别：男。
学号：1002,姓名：莉丝,性别：女。
学号：1003,姓名：王武,性别：男。
编写学员管理类 StudentManagement ，实现删除学员方法 deleteStudent()，根据学员id 删除以下学员：
学号：1002,姓名：莉丝,性别：女。
控制台打印字符串界面，提示用户根据编号选择对应功能，界面功能如下： 1.根据学号查看学员信息     2.添加学员     3.查看所有学员信息
自定义异常类：添加学员传入参数不合理时抛出自定义异常
'''


class Student:
    def __init__(self, id, name, sex):
        self.id = id
        self.name = name
        self.sex = sex


class StudentManagement:

    stu_list = []

    @classmethod
    def addStudent(cls, **stu_dic):
        '''添加学员'''
        try:
            cls.stu_list.append(stu_dic)
            return cls.stu_list
        except:
            raise MyException("添加学生信息输入不合理")

    @classmethod
    def deleteStudent(cls,id):
        '''删除学员'''
        for stu in cls.stu_list:
            try:
                if stu["id"] == id:
                    cls.stu_list.remove(stu)
                    print(f"学号为{stu['id']}的学生信息已删除")
            except:
                raise MyException("输入学号信息有误")

    @classmethod
    def findStudengt(cls,id):
        '''查询学员信息'''
        if len(cls.stu_list) != 0:
            for stu in cls.stu_list:
                if stu["id"] == id:
                    print(f"学号：{stu['id']}，姓名：{stu['name']}，性别：{stu['sex']}")
        else:
            print("输入学号不存在")

    @classmethod
    def printStudent(cls):
        if len(cls.stu_list) != 0:
            for s in cls.stu_list:
                print(f"学号：{s['id']}，姓名：{s['name']}，性别：{s['sex']}")
        else:
            print("学生列表为空，请先添加学员信息")

class MyException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        repr(self.msg)


if __name__=="__main__":
    while input("是否继续选择学生信息功能 y|n：")=="y":
        order_num = input("请根据编号选择对应功能\n1.根据学号查看学员信息\n2.添加学员\n3.查看所有学员信息\n请输入对应编号：")
        if order_num == "1":
            target_id = input("请输入要查询的学生学号：")
            StudentManagement.findStudengt(target_id)
        elif order_num == "2":
            while input("是否继续录入学生信息 y|n：")=="y":
                id = input("请输入学号：")
                name = input("请输入姓名：")
                sex = input("请输入性别：")
                stu_list =StudentManagement.addStudent(id=id, name=name, sex=sex)
        elif order_num == "3":
            StudentManagement.printStudent()
        else:
            print("输入的命令编号无效，请重新输入")