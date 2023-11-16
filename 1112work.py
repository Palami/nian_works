"""
完成学生管理系统的多任务Web服务器
以面向对象方式实现，使用字典表示学生信息，不需要封装学生类
实现增删改查接口，返回 json 格式数据
请求方式：
添加： http://127.0.0.1:8888/add?sid=s09&name=lucy&age=23&gender=male
修改： http://127.0.0.1:8888/change?sid=s09&name=kevin&age=23&gender=male
查询： http://127.0.0.1:8888/query?sid=s09
删除： http://127.0.0.1:8888/del?sid=s09
数据需要使用文件 db.txt 进行持久化存储，并保证数据的有效性
"""
import socket
import threading
import json

class Student_server():

    def __init__(self):
        with open("data.txt", "r", encoding="UTF-8") as original_data:
            ori_str = original_data.read()
        self.student_lis = list(eval(ori_str.replace("\n", ",")))

    # 启动服务器
    def startServer(self):
        # 创建一个socket 对象
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置复用端口
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定IP与端口, 参数是一个元组，IP是字符串，端口是数字
        server.bind(("", 8888))
        # 启动服务器的监听
        server.listen(256)
        print("MyWebServer String On 127.0.0.1:8888")
        # 使用死循环接受客户端的请求
        while True:
            # 接收客户端的连接，返回客户端的socker对象和IP_port
            client, ip_port = server.accept()
            print(f"客户端  {ip_port[0]} 使用 { ip_port[1] } 端口连接成功")
            # 创建一个子线程去处理客户端的请求，主线程再去接受其它客户端的请求
            t = threading.Thread(target=self.handleClientRequest, args=(client,))
            # 设置守护线程
            t.daemon = True
            # 启动子线程去处理客户端请求
            t.start()

    # 用来处理用户请求的函数
    def handleClientRequest(self,client):
        # 读取客户端的请求内容
        recv_data = client.recv(4096).decode("utf-8")
        # 判断与客户端的连接是否断开
        if len(recv_data) == 0:
            client.close()
            return
        # 解析客户端请求数据
        request = self.parseRequest(recv_data)
        # 根据用户请求去做相应的处理，不同的请求使用不同的函数进行处理，这个处理函数称为接口，找接口的过程，称为路由
        response = self.router(request)
        # 服务器将响应数据返回给客户端
        client.send(response)
        # 服务器为客户端 提供一次服务完成，关闭连接
        client.close()

    # 用来解析请求报文的函数
    def parseRequest(self,recv_data):
        # 用来保存数据的字典
        request = {
            "method": "",
            "path": "",
            "values": {}
        }
        # 先获取到第一行请求行数据
        recv_data = recv_data.split()
        # 保存请求方法
        request["method"] = recv_data[0]
        # 处理请求路径 和参数
        path = recv_data[1]
        if "?" in path:
            tmp = path.split("?")
            # 保存路径
            path = tmp[0]
            # 提取参数
            params = tmp[1].split("&")
            for s in params:
                # 分解析查询参数字符串
                k, v = s.split("=")
                request["values"][k] = v
        # 保存请求路径
        request["path"] = path
        # 返回解析结果
        return request

    # 路由函数
    def router(self, request):
        # 取出客户端 的请求路径
        path = request.get("path")
        # 使用 if 实现一个简单的路由
        response_body = ""
        if path == "/add":
            response_body = self.index(request["values"])
        elif path == "/change":
            response_body = self.change(request["values"])
        elif path == "/query":
            response_body = self.query(request["values"])
        elif path == "/del":
            response_body = self.del_data(request["values"])
        # 拼装完整的响应报文
        response = "HTTP/1.1 200 OK\r\n"
        # image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8
        response += "Content-Type: text/html;charset=utf-8\r\n"
        response += "Server: MyWebServer V1.0\r\n"
        response += "\r\n"
        response += response_body
        # 因为使用的是TCP字节流传输数据，所以要对响应数据进行转换类型
        response = response.encode("utf-8")


        print(response)
        return response


    def write_data(self,student_lis):
        final_list = []
        for stu in student_lis:
            final_list.append(str(stu) + "\n")  # 处理回车
        with open("data.txt", "w", encoding="UTF-8") as data_txt:
            data_txt.writelines(final_list)

    def index(self,values):
        student_dic = {"sid": values["sid"], "name": values["name"], "age": values["age"], "gender": values["gender"]}
        sid_list = [stu["sid"] for stu in self.student_lis]
        if values["sid"] in sid_list:
            return "学号已存在，添加失败"
        else:
            self.student_lis.append(student_dic)
            self.write_data(self.student_lis)
            return "添加成功"

    def change(self,values):
        sid_list = [stu["sid"] for stu in self.student_lis]
        if values["sid"] not in sid_list:
            return "学号不存在"
        else:
            for stu in self.student_lis:
                if values["sid"] == stu["sid"]:
                    stu["name"]=values["name"]
                    stu["age"] =values["age"]
                    stu["gender"]= values["gender"]
                    return "学生信息编辑成功"


    def query(self,values):
        sid_list = [stu["sid"] for stu in self.student_lis]
        if values["sid"] not in sid_list:
            return "学号不存在"
        else:
            for stu in self.student_lis:
                if values["sid"] == stu["sid"]:
                    return json.dumps(stu)  #返回JSON数据


    def del_data(self,values):
        sid_list = [stu["sid"] for stu in self.student_lis]
        if values["sid"] not in sid_list:
            return "要删除的学生学号不存在"
        else:
            for stu in self.student_lis:
                if values["sid"] == stu["sid"]:
                    self.student_lis.remove(stu)
                    self.write_data(self.student_lis)
                    return "学生信息删除成功"



# 程序入口
if __name__ == '__main__':
    Student_server().startServer()
