import pymysql

# 创建连接
def create_connection():
    connection = pymysql.connect(
        host='123.207.255.20',  # 数据库主机地址
        port='47222',
        user='root',   # 数据库用户名
        password=']W5zjg@+Z6khF7',  # 数据库密码
        db='database_name',  # 数据库名
        charset='utf8mb4'   # 字符集
    )
    return connection

# 使用连接
def use_connection():
    connection = create_connection()

    with connection.cursor() as cursor:
        # 示例SQL查询
        sql = "SELECT * FROM table_name"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            print(row)

    # 关闭连接
    connection.close()

if __name__ == "__main__":
    use_connection()