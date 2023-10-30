'''
作业：
实现学生管理系统：
学生信息包含：
    - 编号（sid), 姓名（name), 年龄（age), 性别（gender) 四个信息
    - 每个学生信息使用字典形式保存
    - 使用列表保存所有学生的信息
1. 实现菜单函数，输出下列信息，返回用户输入的编号，并进行输入校验。
    print("****************************************")
    print("*                                学生管理系统                         *")
    print("*              1. 添加新学生信息              *")
    print("*             2. 通过学号修改学生信息                 *")
    print("*                3. 通过学号删除学生信息                 *")
    print("*                4. 通过姓名删除学生信息                 *")
    print("*             5. 通过学号查询学生信息          *")
    print("*                6. 通过姓名查询学生信息          *")
    print("*                7. 显示所有学生信息             *")
    print("*                8. 退出系统                                           *")
    print("****************************************")
    select_op = input("输入编号选择操作：")
2. 实现控制函数，用来控制菜单的输出与功能的选择，直到用户选择8，结束程序运行。
3. 实现添加学生函数，函数参数为编号，姓名，年龄，性别四个参数，返回是否添加成功的结果，要求编号不可重复。
4. 实现修改函数，参数为学号，如果学生存在，则进行修改，不存在输出提示，并返回是否修改成功
5. 实现删除函数，参数为学号，如果学生存在，则进行删除，不存在输出提示，并返回是否删除成功
6. 实现删除函数，参数为姓名，如果学生存在，则进行删除（同名学生全部删除），不存在输出提示，并返回是否删除成功
7. 实现查询函数，参数为学号，如果学生存在，则输出学生信息，不存在输出提示，并返回是否查询成功
8. 实现查询函数，参数为姓名，如果学生存在，则输出学生信息（同名学生全部输出），不存在输出提示，并返回是否删除成功
9. 实现函数，输出所有学生信息
'''

import copy


class Student:
    def __init__(self):
        # self.student_dic = {"sid": sid, "name": name, "age": age, "gender": gender}
        self.student_lis = []


class StudentManager(Student):

    def menu(self):
        print("******************************************")
        print("*                学生管理系统               *")
        print("*             1. 添加新学生信息              *")
        print("*             2. 通过学号修改学生信息         *")
        print("*             3. 通过学号删除学生信息         *")
        print("*             4. 通过姓名删除学生信息         *")
        print("*             5. 通过学号查询学生信息         *")
        print("*             6. 通过姓名查询学生信息         *")
        print("*             7. 显示所有学生信息            *")
        print("*             8. 退出系统                  *")
        print("******************************************")
        select_op = input("输入编号选择操作：")
        try:
            if int(select_op) in (1, 2, 3, 4, 5, 6, 7, 8):
                return int(select_op)
            else:
                print("输入的编号不正确")
        except:
            print("输入的编号不合法")#作业中要求将校验写在menu方法中，我觉得应该写在control方法里，这样在输入不合法的编号后还可以唤起菜单。

    def control(self):
        num = self.menu()
        while num:
            if num == 1:
                sid, name, age, gender = input("请依次输入学号、姓名、性别、年龄，以空格隔开：").split(" ")
                self.add(sid, name, age, gender)
                num = self.menu()
            elif num == 2:
                sid = input("请输入要修改学生的学号：")
                self.edit(sid)
                num = self.menu()
            elif num == 3:
                sid = input("请输入要删除学生的学号：")
                self.delete_by_sid(sid)
                num = self.menu()
            elif num == 4:
                name = input("请输入要删除学生的姓名：")
                self.delete_by_name(name)
                num = self.menu()
            elif num == 5:
                sid = input("请输入要查找学生的学号：")
                self.find_by_sid(sid)
                num = self.menu()
            elif num == 6:
                name = input("请输入要查找学生的姓名：")
                self.find_by_name(name)
                num = self.menu()
            elif num == 7:
                self.prin()
                num = self.menu()
            elif num == 8:
                print("系统退出成功")
                break

    def add(self, sid, name, age, gender):
        student_dic = {"sid": sid, "name": name, "age": age, "gender": gender}
        sid_list = [stu["sid"] for stu in self.student_lis]
        if sid in sid_list:
            print("学号已存在，添加失败")
        else:
            self.student_lis.append(student_dic)
            print("添加成功")

    def edit(self, sid):
        sid_list = [stu["sid"] for stu in self.student_lis]
        if sid not in sid_list:
            print("学号不存在")
        else:
            for stu in self.student_lis:
                if sid == stu["sid"]:
                    edit_key = input("请输入要编辑信息（如：姓名/年龄/性别）：")
                    edit_value = input("请输入想修改的对应信息的数据：")
                    if edit_key == "姓名":
                        stu["name"] = edit_value
                        print("编辑成功")
                    elif edit_key == "年龄":
                        stu["age"] = edit_value
                        print("编辑成功")
                    elif edit_key == "性别":
                        stu["gender"] = edit_value
                        print("编辑成功")
                    else:
                        print("输入信息不正确")

    def delete_by_sid(self, sid):
        sid_list = [stu["sid"] for stu in self.student_lis]
        if sid not in sid_list:
            print("学号不存在")
        else:
            for stu in self.student_lis:
                if sid == stu["sid"]:
                    self.student_lis.remove(stu)
                    print("学生信息删除成功")

    def delete_by_name(self, name):
        name_list = [stu["name"] for stu in self.student_lis]
        if name not in name_list:
            print("该学生姓名不存在")
        else:
            stu_list = copy.deepcopy(self.student_lis)
            for stu in stu_list:
                if name == stu["name"]:
                    self.student_lis.remove(stu)
            print("学生信息删除成功")

    def find_by_sid(self, sid):
        sid_list = [stu["sid"] for stu in self.student_lis]
        if sid not in sid_list:
            print("学号不存在")
        else:
            for stu in self.student_lis:
                if sid == stu["sid"]:
                    print(f'查询成功！学生学号：{stu["sid"]}，姓名：{stu["name"]}，年龄：{stu["age"]}，性别：{stu["gender"]}')

    def find_by_name(self, name):
        name_list = [stu["name"] for stu in self.student_lis]
        if name not in name_list:
            print("姓名不存在")
        else:
            for stu in self.student_lis:
                if name == stu["name"]:
                    print(f'查询成功！学生学号：{stu["sid"]}，姓名：{stu["name"]}，年龄：{stu["age"]}，性别：{stu["gender"]}')

    def prin(self):
        print("所有学生信息：")
        for stu in self.student_lis:
            print(f'学生学号：{stu["sid"]}，姓名：{stu["name"]}，年龄：{stu["age"]}，性别：{stu["gender"]}')


if __name__ == "__main__":
    StudentManager().control()
