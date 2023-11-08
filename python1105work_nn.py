'''
作业：
在现有功能基础上，需将程序运行中操作的数据保存到 data.txt 文件中
程序退出时保存数据到文件
程序启动时从文件加载数据到程序
'''

import copy


class Student:
    def __init__(self, student_lis):
        # self.student_dic = {"sid": sid, "name": name, "age": age, "gender": gender}
        self.student_lis = student_lis


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
            print("输入的编号不合法")  # 作业中要求将校验写在menu方法中，我觉得应该写在control方法里，这样在输入不合法的编号后还可以唤起菜单。

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
                self.display()
                num = self.menu()
            elif num == 8:
                self.close()
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

    def display(self):
        print("所有学生信息：")
        for stu in self.student_lis:
            print(f'学生学号：{stu["sid"]}，姓名：{stu["name"]}，年龄：{stu["age"]}，性别：{stu["gender"]}')

    def close(self):
        final_list =[]
        for stu in self.student_lis:
            final_list.append(str(stu)+"\n")  #处理回车
        with open("data.txt", "w", encoding="UTF-8") as data_txt:
            data_txt.writelines(final_list)
        print("系统退出成功")


if __name__ == "__main__":
    with open("data.txt", "r", encoding="UTF-8") as original_data:
        ori_str = original_data.read()
    ori_list = list(eval(ori_str.replace("\n",","))) #将读取的string 转为 list，作为实例属性
    StudentManager(ori_list).control()
