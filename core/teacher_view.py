#!_*_coding:utf-8 _*_
# __author__:"lurkerzhang"
from conf.logger import logger
from core.func_module import *


def show_teacher_menu():
    print('''===讲师菜单===
    1.登入
    2.查看班级
    3.查看学员
    4.修改学员成绩
    5.上课
    Q.退出
    ''')


def run():
    # 登入，输入讲师姓名无密码
    teacher = None
    while True:
        show_teacher_menu()
        s = input('>>>').strip()
        if s.isdigit():
            s = int(s)
            if s == 1:
                logger.info('teacher login...')
                print('请输入讲师姓名')
                name = input('>>>').strip()
                teacher = login(name, tp='teacher')
                if not teacher:
                    print('登入失败')
            elif s == 2:
                logger.info('check grades...')
                check_grades(teacher)
            elif s == 3:
                logger.info('check grades...')
                check_grades_students(teacher)
            elif s == 4:
                logger.info('modify score...')
                modify_score(teacher)
            elif s == 5:
                logger.info('teaching...')
                teach(teacher,)
        elif s == 'q' or s == 'Q':
            # save_student(student)
            exit('bye')
        else:
            print('输入错误')
