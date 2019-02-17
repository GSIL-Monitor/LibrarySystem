
import sys
sys.path.append('tools')
from tools.tabchen_utils import * 
class SystemTools():
    def __init__(self):
        self.db = myMysql("localhost",3306,"LibrarySystem","root","12345678")
    def login(self,username,password):
        quary = "SELECT * FROM userdb where username ='{}' and password='{}'".format(username,password)
        result = self.db.execute(quary)
        if len(result)==0:
            return False
        else:
            return True        
    def regist(self,username,password):
        quary = "SELECT * FROM userdb where username ='{}'".format(username)
        result = self.db.execute(quary)
        if len(result)!=0:
            print('User name exist!')
            return False
        else:
            quary = "INSERT INTO `userdb` (`username`, `password`) VALUES ('{}', '{}')".format(username,password)
            result = self.db.execute(quary)
            return True
    def changePassword(self,username,old_password,new_password):
        login_result = self.login(username,old_password)
        if login_result:
            quary = "UPDATE `userdb` SET `password`='{}' WHERE `username`='{}';".format(new_password,username)
            result = self.db.execute(quary)
            return True
        else:
            print('原始密码错误')
            return False
class BookTools():
    def __init__(self):
        pass
    def selectOneBookByName(self,book_name):
        pass
    def selectBooksByPrice(self):
        pass
    def addOneBook(self,book_info):
        pass
    def modifyOneBookByName(self,book_name,book_info):
        pass
    def deleteOneBookByName(self,book_name):
        pass

class LibrarySystem():
    def __init__(self):
        self.system_tools = SystemTools()
        self.book_tools = BookTools()
        self.init_system()

    def init_system(self):
        init_choice = input('欢迎来到图书馆：1.登录,2.注册,3.修改密码:\n')
        try:
            init_choice = int(init_choice)
        except:
            print('选择错误请重新选择')
            self.init_system()
        if init_choice == 1:
            self.login()
        elif init_choice==2:
            self.regist()
        elif init_choice==3:
            self.changePassword()
        else:
            raise('输出错误，应该为1,2,3')
    def manage_system(self):
        num_star = 40
        print('*'*num_star,'欢迎来到图书管理中心','*'*num_star)
        text = '''
        1、查看所有图书功能
        2、通过书名查看一本书
        3、通过价格查询书籍
        4、增加一本书籍
        5、修改一本书籍
        6、删除一本书籍
        7、再也不想见你了
        '''
        system_choice = input(text)
        print('开始进行:',system_choice)

    def login(self):
        print('输入信息')
        username = str(input('username:'))
        password = str(input('password:'))
        result = self.system_tools.login(username,password)
        if result:
            print('登录成功')
            self.manage_system()
        else:
            print('登录失败')
            self.init_system()
    def regist(self):
        username = str(input('请输入用户名:')).strip()
        password = str(input('请输入密码:')).strip()
        password_2 = str(input('请确认密码:')).strip()
        if password!=password_2:
            print('两次密码不同')
            self.init_system()
        else:
            result = self.system_tools.regist(username,password)
            print(result)
            if result:
                print('注册成功')
                self.init_system()
            else:
                print('注册失败')
                self.init_system()
        
    def changePassword(self):
        username = input('请输入用户名:')
        old_password = input('请输入旧密码:')
        new_password = input('请输入新密码:')
        result = self.system_tools.changePassword(username,old_password,new_password)
        if result:
            print('密码修改成功')
            self.init_system()
        else:
            self.init_system()
    def selectOneBookByName(self):
        pass
    def selectBooksByPrice(self):
        pass
    def selectBooksByPrice(self):
        pass
    def addOneBook(self):
        pass
    def modifyOneBookByName(self):
        pass
    def deleteOneBookByName(self):
        pass
    def exit(self):
        pass

if __name__ == "__main__":
    my_lib = LibrarySystem()
