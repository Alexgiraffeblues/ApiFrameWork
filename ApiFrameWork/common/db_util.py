import pymysql

class DBUtil:
    # 定义类属性
    conn = None
    
    # 数据库连接方法 注：将方法声明为私有（在方法名前面加两个下划线）可以让调用时不显示 
    @classmethod
    def get_conn(cls):
        # 创建数据库链接
        cls.conn = pymysql.connect(host = 'localhost', port = 3306, user = 'root', password = '123456',
                                   database = 'test_db',charset = 'utf8')
        return cls.conn
        
    # 数据库关闭方法
    @classmethod
    def close_conn(cls):
        # 关闭连接
        cls.conn.close()
    
    # 数据库查询方法
    @classmethod
    def query_db(cls, sql):
        cursor = None
        result = None
        try:
            # 创建数据库链接
            cls.conn = cls.get_conn()
            # 获取游标
            cursor = cls.conn.cursor()
            # 执行sql，返回查询结果
            cursor.execute(sql)
            result = cursor.fetchone()
        except Exception as e:
            print('读取数据库报错：', str(e))
        
        finally:
            cursor.close()
            cls.close_conn()
            return result
    
    # 数据库增删改方法
    @classmethod
    def uid_db(cls, sql):
        cursor = None
        try:
            cls.conn = cls.get_conn()
            cursor = cls.conn.cursor()
            cursor.execute(sql)
            affect_rows = cls.conn.affected_rows()
            print('影响数据库的行数：', affect_rows)
            cls.conn.commit()
        except Exception as e:
            print('增删改操作数据库时出错', str(e))
            cls.conn.rollback()
        finally:
            cursor.close()
            cls.close_conn()


