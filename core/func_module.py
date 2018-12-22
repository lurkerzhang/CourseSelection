#!_*_coding:utf-8 _*_
# __author__:"lurkerzhang"
from core.class_module import Teacher, School, Course, Student
import pickle
import os
from conf.setting import DBDIR
import re


# 读取数据
def get_data_list(type):
    data_file = ''
    if type == 'school':
        data_file = os.path.join(DBDIR, 'schools.pk')
    elif type == 'teacher':
        data_file = os.path.join(DBDIR, 'teachers.pk')
    elif type == 'course':
        data_file = os.path.join(DBDIR, 'courses.pk')
    elif type == 'student':
        data_file = os.path.join(DBDIR, 'students.pk')
    else:
        print('参数未识别')
    try:
        with open(data_file, 'rb') as sc:
            data_list = pickle.load(sc)
            return data_list
    except IOError:
        with open(data_file, 'wb') as sc:
            data_list = []
            pickle.dump(data_list, sc)
            return data_list


# # 读取学校
# def get_schools():
#     try:
#         with open('schools.pk', 'rb') as sc:
#             schools = pickle.load(sc)
#             return schools
#     except IOError:
#         with open('schools.pk', 'wb') as sc:
#             schools = []
#             pickle.dump(schools, sc)
#             return schools
#
#
# # 读取讲师
# def get_teachers():
#     try:
#         with open('teachers.pk', 'rb') as sc:
#             teachers = pickle.load(sc)
#             return teachers
#     except IOError:
#         with open('teachers.pk', 'wb') as sc:
#             teachers = []
#             pickle.dump(teachers, sc)
#             return teachers


# # 打印学校信息
# def print_schools(schools):
#     if not len(schools):
#         print('无学校信息')
#     else:
#         for i, element in list(enumerate(schools, 1)):
#             print('%s.%s' % (i, element.name))

# 序列打印角色信息
def print_character(data):
    if not len(data):
        print('查询数据为空')
    else:
        for i, element in list(enumerate(data, 1)):
            print('%s.%s' % (i, element.name))


# 创建学校
def create_school():
    # 先读取已有学校信息
    schools = get_data_list('school')
    print_character(schools)
    print('输入学校信息：')
    name = input('学校名>>>').strip()
    new_school = School(name)
    # print('给%s创建班级(输入Q退出创建):' % name)
    # while True:
    #     s = input('>>>').strip()
    #     if s == 'q' or s == 'Q':
    #         break
    #     elif ' ' not in s:
    #         new_school.add_grade(s)
    #     else:
    #         print('班级输入错误')
    print('成功创建学校:%s' % new_school.name)
    schools.append(new_school)
    with open(os.path.join(DBDIR, 'schools.pk'), 'wb') as sc:
        pickle.dump(schools, sc)
    return True


# 创建讲师
def create_teacher():
    # 获取学校信息
    schools = get_data_list('school')
    if not len(schools):
        print('请先创建学校信息')
        return None
    else:
        # 获取已有讲师信息
        teachers = get_data_list('teacher')
        print('请输入要创建的讲师信息：')
        name = input('姓名>>>').strip()
        for t in teachers:
            if t.name == name:
                print('讲师%s已存在' % name)
                return
        age = input('年龄>>>').strip()
        sex = input('性别>>>').strip()
        new_teacher = Teacher(name, age, sex)
        print('为讲师%s关联学校：' % new_teacher.name)
        print_character(schools)
        while True:
            s = input('>>>').strip()
            if s.isdigit():
                s = int(s)
                if s in list(range(1, len(schools) + 1)):
                    new_teacher.set_school(schools[s - 1].name)
                    print('讲师%s关联到学校%s' % (new_teacher.name, schools[s - 1].name))
                    teachers.append(new_teacher)
                    with open(os.path.join(DBDIR, 'teachers.pk'), 'wb') as sc:
                        pickle.dump(teachers, sc)
                    return
                else:
                    print('输入错误，重新输入')
            else:
                print('输入错误，重新输入')


# 创建课程
def create_course():
    # 读取学校
    schools = get_data_list('school')
    if len(schools) == 0:
        print('无学校信息，请先创建学校')
    else:
        while True:
            # 获取已有课程
            courses = get_data_list('course')
            print('已有课程：')
            print_character(courses)
            print('学校信息：')
            print_character(schools)
            print('选择学校开始创建课程(输入Q结束创建)')
            s = input('>>>').strip()
            if s.isdigit():
                s = int(s)
                if s in list(range(1, len(schools) + 1)):
                    print('输入待创建的课程信息：')
                    name = input('课程名>>>').strip()
                    for c in courses:
                        if c.name == name:
                            print('课程%s已存在' % name)
                            return
                    while True:
                        price = input('价格>>>').strip()
                        if not re.fullmatch('^0|[1-9][0-9]*', price):
                            print('价格格式不对')
                            continue
                        else:
                            break
                    while True:
                        peroid = input('课程周期(天)>>>').strip()
                        if not re.fullmatch('^0|[1-9][0-9]*', peroid):
                            print('周期格式不对')
                            continue
                        else:
                            break
                    new_course = Course(name, price, peroid)
                    new_course.set_school(schools[s - 1].name)
                    courses.append(new_course)
                    print('成功创建课程：%s' % new_course.name)
                    schools[s - 1].add_course(new_course.name)
                    with open(os.path.join(DBDIR, 'courses.pk'), 'wb') as sc:
                        pickle.dump(courses, sc)
                    with open(os.path.join(DBDIR, 'schools.pk'), 'wb') as sc:
                        pickle.dump(schools, sc)
            elif s == 'q' or s == 'Q':
                print('结束创建课程')
                return
            else:
                print('输入错误，重新输入')


# 创建班级
def create_grade():
    # 读取学校
    schools = get_data_list('school')
    if len(schools) == 0:
        print('无学校信息，请先创建学校')
    else:
        while True:
            schools = get_data_list('school')
            print_character(schools)
            print('选择学校开始创建班级(输入Q结束创建)')
            s = input('>>>').strip()
            if s.isdigit():
                s = int(s)
                if s in list(range(1, len(schools) + 1)):
                    print('给学校：%s创建班级(输入Q退出创建):' % schools[s - 1].name)
                    while True:
                        g = input('班级名(格式如：class-1)>>>').strip()
                        if not re.fullmatch('^class-\d*', g):
                            print('班级格式不对')
                            continue
                        if g == 'q' or g == 'Q':
                            break
                        elif g not in list(schools[s - 1].grades.keys()):
                            # 为班级关联课程和讲师
                            # 先获取已有课程和讲师
                            courses = get_data_list('course')
                            if not len(courses):
                                print('无课程信息，请先创建课程')
                                return
                            else:
                                sel_school_courses = []
                                for c in courses:
                                    if c.school == schools[s - 1].name:
                                        sel_school_courses.append(c)
                                print_character(sel_school_courses)
                                print('选择要关联的课程')
                                while True:
                                    c = input('>>>').strip()
                                    if c.isdigit():
                                        c = int(c)
                                        if c in list(range(1, len(courses) + 1)):
                                            g_course = courses[c - 1].name
                                            break
                                        else:
                                            print('输入错误')
                                    else:
                                        print('输入错误')
                                teachers_data = get_data_list('teacher')
                                teachers = []
                                for t in teachers_data:
                                    if t.school == schools[s - 1].name:
                                        teachers.append(t)
                                if not len(teachers):
                                    print('无讲师信息，请先创建讲师')
                                    return
                                else:
                                    print_character(teachers)
                                    print('选择要关联的讲师')
                                    while True:
                                        c = input('>>>').strip()
                                        if c.isdigit():
                                            c = int(c)
                                            if c in list(range(1, len(teachers) + 1)):
                                                g_teacher = teachers[c - 1].name
                                                count = 0
                                                for t in teachers_data:
                                                    if t.name == g_teacher:
                                                        teachers_data[count].add_grade(g)
                                                    count += 1

                                                break
                                            else:
                                                print('输入错误')
                                        else:
                                            print('输入错误')
                                    # 班级的结构{'grade':'','courses':'','teachers':'','students':[]}
                                    new_grade = {g: {'courses': g_course, 'teachers': g_teacher, 'students': []}}
                                    schools[s - 1].add_grade(new_grade)
                                    print(
                                        '学校：%s的班级：%s 关联了讲师：%s 和 课程：%s' % (schools[s - 1].name, g, g_teacher, g_course))
                                    with open(os.path.join(DBDIR, 'schools.pk'), 'wb') as sc:
                                        pickle.dump(schools, sc)
                                    with open(os.path.join(DBDIR, 'teachers.pk'), 'wb') as sc:
                                        pickle.dump(teachers_data, sc)
                                    return
                        elif g in list(schools[s - 1].grades.keys()):
                            print('班级已存在')
                        else:
                            print('班级输入错误')
            elif s == 'q' or s == 'Q':
                print('结束创建班级')
                return
            else:
                print('输入错误，重新输入')


# 登入
def login(name, tp='student'):
    if tp == 'teacher':
        data_list = get_data_list('teacher')
    else:
        data_list = get_data_list('student')
    if not len(data_list):
        print('%s不存在，请先注册' % name)
        return False
    else:
        for n in data_list:
            if n.name == name:
                print('%s 成功登陆' % name)
                return n
        print('%s不存在' % name)
        return False


# 学员注册
def stu_register():
    students = get_data_list('student')
    name = input('姓名>>>').strip()
    for s in students:
        if s.name == name:
            print('学员：%s 已存在' % name)
            return False
    while True:
        age = input('年龄(10-99)>>>').strip()
        if not re.fullmatch('^[1-9]\d{1}', age):
            print('年龄格式不对')
            continue
        else:
            break
    while True:
        sex = input('性别>>>').strip()
        if not re.fullmatch('^male|femal|男|女', sex):
            print('性别格式不对')
            continue
        else:
            break
    new_student = Student(name, age, sex)
    students.append(new_student)
    with open(os.path.join(DBDIR, 'students.pk'), 'wb') as sc:
        pickle.dump(students, sc)
    print('成功创建学员:%s ' % new_student.name)
    return new_student


def select_grade(student):
    if not student:
        print('请先登陆')
        return student
    else:
        if student.grade:
            print('不能重复选择课程，已选择学校【%s】的课程【%s】 ' % (student.school, student.grade))
            return student
        else:
            schools = get_data_list('school')
            print('选择学校')
            while True:
                print_character(schools)
                s = input('>>>').strip()
                if s.isdigit():
                    s = int(s)
                    if s in list(range(1, len(schools) + 1)):
                        s_school = schools[s - 1].name
                        student.set_school(s_school)
                        for i, element in list(enumerate(schools[s - 1].grades.keys(), 1)):
                            print('%s.%s[课程：%s,讲师：%s]' % (i, element, schools[s - 1].grades[element]['courses'],
                                                          schools[s - 1].grades[element]['teachers']))
                        print('请选择班级')
                        while True:
                            c = input('>>>').strip()
                            if c.isdigit():
                                c = int(c)
                                s_grade = dict(enumerate(schools[s - 1].grades.keys(), 1))[c]
                                s_course = schools[s - 1].grades[s_grade]['courses']
                                s_teacher = schools[s - 1].grades[s_grade]['teachers']
                                student.set_grade(s_grade)
                                student.set_course(s_course)
                                # if student.name in schools[s - 1].grades[s_grade]['students']:
                                schools[s - 1].grades[s_grade]['students'].append(student.name)
                                print('成功选择了学校：%s 班级:%s 课程：%s 授课讲师：%s' % (s_school, s_grade, s_course, s_teacher))
                                with open(os.path.join(DBDIR, 'schools.pk'), 'wb') as sc:
                                    pickle.dump(schools, sc)
                                return student
                            else:
                                print('输入错误，重新选择班级')

                print('输入错误，重新选择学校')


# 获取课程价格
def get_course_price(course_name):
    courses = get_data_list('course')
    for c in courses:
        if c.name == course_name:
            return c.price
    print('未开设课程：%s' % course_name)
    return 0


def pay_tuition(student):
    if not student:
        print('未登入')
        return student
    else:
        if not student.course:
            print('你还未选择任何课程')
            return student
        else:
            if not student.payed:
                # 获取课程价格
                price = get_course_price(student.course)
                price = int(price)
                print('你选择的课程是：%s 价格：%s元' % (student.course, price))
                while True:
                    money = input('输入支付金额>>>').strip()
                    if money.isdigit():
                        money = int(money)
                        if money == price:
                            student.set_status(True)
                            print('支付成功')
                            return student
                        elif money < price:
                            print('支付金额过低')
                        else:
                            print('支付金额过多')
                    else:
                        print('金额输入错误')
            else:
                print('已付费，不能重复付费')
                return student
    pass


def learn(student):
    if not student:
        print('未登入')
        return student
    else:
        if student.payed:
            print('%s开始学习%s....（按D退出学习）' % (student.name, student.course))
            while True:
                ss = input().strip()
                if ss == 'd' or ss == 'D':
                    print('学习结束')
                    return student
        else:
            print('未选择课程或未付费')
            return student


def show_school():
    schools = get_data_list('school')
    count = 1
    if not schools:
        print('无学校信息')
        return
    else:
        for s in schools:
            print('''%s.学校【%s】
            学校名：%s''' % (count, s.name, s.name))
            for k, val in s.grades.items():
                print('''            班级【%s】课程【%s】讲师【%s】\n            学员：''' % (k, val['courses'], val['teachers']),end='')
                for sn in val['students']:
                    print(sn, end=' ')
                print('\n')
            count += 1


# 保存学员信息
def save_student(student):
    students = get_data_list('student')
    if students:
        for s in list(enumerate(students)):
            if s[1].name == student.name:
                students[s[0]] = student
                with open(os.path.join(DBDIR, 'students.pk'), 'wb') as sc:
                    pickle.dump(students, sc)
    else:
        print('无学员信息')


# 查看讲师班级
def check_grades(teacher):
    if not teacher:
        print('请先登入')
        return
    else:
        if not teacher.grades:
            print('讲师%s暂无关键班级' % teacher.name)
            return None
        else:
            grades_data = get_teacher_grades(teacher)
            if not grades_data:
                print('未查询到班级数据')
            else:
                print('讲师在学校【%s】授课的班级：' % teacher.school)
                print_grades_details(grades_data)
                return grades_data


# 获取讲师班级数据
def get_teacher_grades(teacher):
    if not teacher.grades:
        print('讲师%s暂无关键班级' % teacher.name)
    else:
        school = teacher.school
        grades = teacher.grades
        grades_data = {}
        # 连接学校数据
        schools = get_data_list('school')
        for s in schools:
            if school == s.name:
                for g in list(s.grades.keys()):
                    if g in grades:
                        grades_data[g] = s.grades[g]
        return grades_data


# 打印班级明细
def print_grades_details(grades_data):
    count = 1
    for g in list(grades_data.keys()):
        print(count, '.', g)
        count += 1


# 查看班级学员
def check_grades_students(teacher):
    if not teacher:
        print('请先登入')
        return
    else:
        print('选择班级：')
        grades_data = get_teacher_grades(teacher)
        check_grades(teacher)
        if grades_data:
            while True:
                s = input('>>>').strip()
                if s.isdigit():
                    s = int(s)
                    if 0 < s < len(grades_data) + 1:
                        k = dict((enumerate(list(grades_data.keys()), 1)))[s]
                        grade_data = grades_data[k]
                        print('班级学员：')
                        count = 1
                        for stu in grade_data['students']:
                            print(count, '.', stu)
                        return grade_data
                    else:
                        print('输入错误')
                        pass
                else:
                    print('输入错误')
        else:
            print('讲师%s无班级数据' % teacher.name)


# 修改学员分数
def set_stu_score(name, score):
    students = get_data_list('student')
    count = 0
    for s in students:
        if s.name == name:
            s.set_score(score)
            save_student(s)
            return True
        count += 1
    return False


# 获取学员分数
def get_score(name):
    students = get_data_list('student')
    for s in students:
        if s.name == name:
            return s.score
    return 0


def modify_score(teacher):
    if not teacher:
        print('请先登入')
        return
    else:
        grade_data = check_grades_students(teacher)
        s = input('选择学员>>>').strip()
        while True:
            if s.isdigit():
                s = int(s)
                if s in list(range(1, len(grade_data['students'])+1)):
                    name = grade_data['students'][s-1]
                    score = get_score(name)
                    print('学员%s当前分数为:%s' % (name, score))
                    while True:
                        new_score = input('输入新的分数(0-100)：').strip()
                        if new_score.isdigit():
                            new_score = int(new_score)
                            if new_score < 0 or new_score >100:
                                print('分数输入错误')
                                continue
                            else:
                                result = set_stu_score(name, new_score)
                                if result:
                                    print('学员%s的分数成功修改为%s分' % (name, new_score))
                                    return True
                                else:
                                    return False
                        else:
                            print('分数输入错误,重新输入')
                else:
                    print('选择错误')
            else:
                print('选择错误')


# 讲师上课
def teach(teacher):
    teacher_grade = check_grades(teacher)
    if teacher_grade:
        g = input('选择班级开始上课')
        while True:
            if g.isdigit():
                g = int(g)
                if g in list(range(1, len(teacher_grade)+1)):
                    print('开始在班级%s上课，按D结束上课....' % list(teacher_grade.keys())[g-1])
                    while True:
                        s = input().strip()
                        if s in ['d','D']:
                            print('结束上课...')
                            break
                    return
                else:
                    print('选择错误')

            else:
                print('选择错误')
    else:
        return


def check_stu_details(s):
    if s.payed:
        is_payed = '是'
    else:
        is_payed = '否'
    print('''学员%s的信息
    姓名：%s
    年龄：%s
    性别：%s
    学校：%s
    班级：%s
    课程：%s
    分数：%s
    是否已付费：%s''' % (s.name, s.name, s.age, s.sex, s.school, s.grade, s.course, s.score, is_payed))


def test():
    # students = get_data_list('student')
    # for s in students:
    #     print(s.name)
    # schools = get_data_list('school')
    # for s in schools:
    #     for g in list(s.grades.keys()):
    #         print(s.name,g,s.grades[g])
    teachers = get_data_list('teacher')
    for t in teachers:
        print(t.name, t.school, t.grades)


if __name__ == '__main__':
    test()
