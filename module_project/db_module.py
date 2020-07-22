""" 추후 도커에 생성한 디비 사용한다면 아래와 같은 정보로 사용
DB HOST : 127.0.0.1
DB PORT : 13306 or 23306 or 33306
DB Connection : hr madang <- root
                tododb <- gihyo
"""

import pymysql as pm
from typing import Callable
from pymysql.connections import Connection as _Connection

def get_connect(db_name: str) -> _Connection:
    """mysql db Connection 객체를 반환

    Args:
        db_name (str): database name

    Returns:
        _Connection: Callable[..., _Connection]
    """
    db = pm.connect(host='127.0.0.1', port=3306, user='root', db=db_name, charset='utf8')
    return db


def print_all_data(db: _Connection, table_name: str):
    """SELECT * FROM table_name

    Args:
        db (_Connection): Callable[..., _Connection]
    """
    try:
        cursor = db.cursor()
        sql = "SELECT * FROM {}".format(table_name)
        cursor.execute(sql)
        result = cursor.fetchall()
        for row_data in result:
            print(row_data)
    finally:
        db.close()


# CREATE DATABASE student_db default CHARACTER SET utf8;
# CREATE TABLE student (_id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(32) NOT NULL, kor INT DEFAULT 0, eng INT DEFAULT 0, mat INT DEFAULT 0, avg FLOAT DEFAULT 0);
# INSERT INTO student (name, kor, eng, mat, avg) VALUE("USER1", 100, 90, 80, 270.0);

if __name__ == '__main__':
    db = get_connect('student_db')
    print_all_data(db, 'student')