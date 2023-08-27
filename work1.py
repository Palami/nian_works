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

class StudentManagement(Student):
    def __init__(self, id, name, sex, stu_list):
        super().__init__(id, name, sex)
        self.stu_list = stu_list

    def addStudent(self, **stu_dic):
        '''添加学员'''
        self.stu_dic = stu_dic
        self.stu_list.append(self.stu_dic)
        return self.stu_list

    def deleteStudent(self):
        '''删除学员'''
        pass


if __name__=="__main__":
    stu_list = []
    while input("是否继续录入学生信息 y|n：")=="y":
        id = input("请输入学号：")
        name = input("请输入姓名：")
        sex = input("请输入性别：")
        student = StudentManagement(id, name, sex, stu_list)
        stu_list =student.addStudent(id=student.id, name=student.name, sex=student.sex)
    for s in stu_list:
        print(f"学号：{s['id']}，姓名：{s['name']}，性别：{s['sex']}")