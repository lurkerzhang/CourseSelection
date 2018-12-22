#!_*_coding:utf-8 _*_
# __author__:"lurkerzhang"
# 1. 创建北京、上海 2 所学校
# 2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开
# 3. 课程包含，周期，价格，通过学校创建课程
# 4. 通过学校创建班级， 班级关联课程、讲师
# 5. 创建学员时，选择学校，关联班级
# 5. 创建讲师角色时要关联学校，
# 6. 提供两个角色接口
# 6.1 学员视图， 可以注册， 交学费， 选择班级，
# 6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩
# 6.3 管理视图，创建讲师， 创建班级，创建课程


class School:
    """
    :class:School 学校角色
    """

    def __init__(self, name, grades=None, teachers=None, courses=None):
        if grades is None:
            grades = {}
        if teachers is None:
            teachers = []
        if courses is None:
            courses = []
        self.name = name
        self.grades = grades
        self.teachers = teachers
        self.courses = courses

    def add_grade(self, grade):
        if list(grade.keys())[0] not in self.grades.keys():
            self.grades = dict(list(self.grades.items())+list(grade.items()))
            print('班级:%s已成功加入学校:%s' % (list(grade.keys())[0], self.name))
        else:
            print('班级:%s已存在于学校:%s' % (list(grade.keys())[0], self.name))

    def add_teacher(self, teacher_name):
        if teacher_name not in self.teachers:
            self.teachers.append(teacher_name)
            print('讲师:%s已成功加入学校:%s' % (teacher_name, self.name))
        else:
            print('讲师:%s已存在于学校:%s' % (teacher_name, self.name))

    def add_course(self, course_name):
        if course_name not in self.courses:
            self.courses.append(course_name)
            print('课程:%s已成功加入学校:%s' % (course_name, self.name))
        else:
            print('课程:%s已存在于学校:%s' % (course_name, self.name))


class People:
    """
    :class:People
    """

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class Student(People):
    """
    :class:Student 学员角色
    """

    def __init__(self, name, age, sex, school=None, grade=None, course=None, score=0):
        super().__init__(name, age, sex)
        self.payed = False
        if not school:
            school = ''
        if not grade:
            grade = ''
        if not course:
            course = ''
        self.school = school
        self.grade = grade
        self.course = course
        self.score = score

    def set_school(self, school_name):
        self.school = school_name

    def set_grade(self, grade):
        self.grade = grade

    def set_course(self, course):
        self.course = course

    def set_status(self, status):
        self.payed = status

    def set_score(self, score):
        self.score = score


class Teacher(People):
    """
    :class:Teacher 讲师角色
    """

    def __init__(self, name, age, sex, school=None, grades=None):
        super().__init__(name, age, sex)
        if school is None:
            school = ''
        if grades is None:
            grades = []
        self.school = school
        self.grades = grades

    def set_school(self, school_name):
        self.school = school_name

    def add_grade(self, grade):
        self.grades.append(grade)


class Course:
    """
    :class Course 课程角色
    """

    def __init__(self, name, price, peroid, school=None):
        self.name = name
        self.price = price
        self.peroid = peroid
        if school is None:
            school = ''
        self.school = school

    def set_school(self, school_name):
        self.school = school_name
        print('课程:%s已关联学校:%s' % (self.name, school_name))


def test():
    pass


if __name__ == '__main__':
    test()
