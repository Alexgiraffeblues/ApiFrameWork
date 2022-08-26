import logging
import logging.handlers

def init_log_config(filename,when='midnight',interval=1,backup_count=7):
    # when 字符串，指定日志切分间隔时间的耽误。midnight: 凌晨 12点
    #interval 是间隔时间的耽误的个数，指等待多少个when 后 继续进行日志记录
    #backupCount 是保留日志文件的个数
    # 1.创建日志器对象
    logger = logging.getLogger()
    # 2.设置日志打印级别
    logger.setLevel(logging.INFO)
    # logging.DEBUG 调试级别
    # logging.INFO 信息级别
    # logging.WARNING 警告级别
    # logging.ERROR 错误级别
    # logging.CRITICAL 严重错误级别

    # 3.1创建 输出到控制台 处理器对象
    st = logging.StreamHandler()
    # 3.2 创建 输出到日志文件 处理器对象
    fh = logging.handlers.TimedRotatingFileHandler(filename, when=when, interval=interval, backupCount=backup_count,
                                                   encoding='utf-8')

    # 4. 创建日志信息格式
    formatter = logging.Formatter(
        "%(asc_time)s %(level_name)s [%(name)s] [%(file_name)s(%(func_Name)s:%(line_no)d)] - %(message)s")

    # 5.给处理器设置日志信息格式
    st.setFormatter(formatter)
    fh.setFormatter(formatter)

    # 6 给日志器添加处理器
    logger.addHandler(st)
    logger.addHandler(fh)


if __name__ == '__main__':
    # 初始化日志
    init_log_config("test.log",interval=3,backup_count=5)
    logging.debug("XXXXX-debug 日志信息")
