#!_*_coding:utf-8 _*_
# __author__:"lurkerzhang"
from conf.logger import logger
from core.func_module import *


def show_stu_menu():
    print('''===学员菜单===
    1.登入
    2.注册
    3.选择班级
    4.交学费
    5.去上课
    6.查看个人详细信息
    Q.退出
    ''')


def run():
    # 学员登陆注册，模拟无学员账号密码登陆操作
    student = None
    while True:
        show_stu_menu()
        s = input('>>>').strip()
        if s.isdigit():
            s = int(s)
            if s == 1:
                logger.info('student login...')
                print('请输入你的姓名')
                name = input('>>>').strip()
                student = login(name)
                if not student:
                    continue
            elif s == 2:
                logger.info('student register...')
                student = stu_register()
            elif s == 3:
                logger.info('select grade...')
                student = select_grade(student)
            elif s == 4:
                logger.info('pay tuition...')
                pay_tuition(student)
            elif s == 5:
                logger.info('learning...')
                student = learn(student)
            elif s == 6:
                logger.info('check student info...')
                check_stu_details(student)
        elif s == 'q' or s == 'Q':
            save_student(student)
            exit('bye')
        else:
            print('输入错误')
