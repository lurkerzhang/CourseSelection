#!_*_coding:utf-8 _*_
# __author__:"lurkerzhang"
from conf.logger import logger
from core.func_module import *


def show_admin_menu():
    print('''===管理员菜单===
    1.增加学校
    2.创建讲师
    3.创建班级
    4.创建课程
    5.显示学校信息
    Q.退出
    ''')


def run():
    while True:
        show_admin_menu()
        s = input('>>>').strip()
        if s.isdigit():
            s = int(s)
            if s == 1:
                logger.info('create school')
                create_school()
            elif s == 2:
                logger.info('create teacher')
                create_teacher()
            elif s == 3:
                logger.info('create grade')
                create_grade()
            elif s == 4:
                logger.info('create course')
                create_course()
            elif s == 5:
                logger.info('school_details')
                show_school()
        elif s == 'q' or s == 'Q':
            exit('bye')
        else:
            print('输入错误')