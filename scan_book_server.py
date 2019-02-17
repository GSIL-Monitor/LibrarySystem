from flask import Flask
from flask import request
import sys
sys.path.append('tools')
from tools.tabchen_utils import * 
import json
app = Flask(__name__)
db = myMysql("localhost",3306,"LibrarySystem","root","12345678")
@app.route("/")
def hello():
    return "你好"
@app.route('/saveBook',methods=['POST'])
def saveBook():
    book_info = request.data.decode()
    book_info = json.loads(book_info)
    try:
        quary = "INSERT INTO `bookdb` (`bookname`, `author`, `category`, `price`, `desc`,`publish_date`) VALUES ('{}', '{}', '{}', '{}', '{}','{}');".format(
        book_info['bookname'],
        book_info['author'],
        book_info['category'],
        book_info['price'],
        book_info['desc'],
        book_info['publish_date'])
        db.execute(quary)
        return "保存成功"
    except:
        return "保存失败"
    


if __name__ == '__main__':
    app.run(debug=True,port=8001,host='0.0.0.0')