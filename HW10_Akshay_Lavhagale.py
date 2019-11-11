""" Akshay Lavhagale
    Homework 10
    Build the framework for student, major and instructor project and summarize their data. """

from collections import defaultdict
from prettytable import PrettyTable
import os


def file_reading_gen(path, fields, sep='|', header=False):
    """ function to read the students, instructors, and grades files into appropriate data structures or classes. """
    try:
        file = open(path, 'r')
    except FileNotFoundError:
        raise FileNotFoundError(f'File {path} cannot be opened.')
    else:
        with file:
            for count_1, line in enumerate(file):
                line = line.rstrip('\n')
                tokens = line.split(sep)
                if fields != len(tokens):
                    raise ValueError(f'{os.path.basename(path)} has {len(tokens)} fields on line {count_1}'
                                     f'but expected {fields}')
                elif header and count_1 == 0:
                    continue  # skipping the header after checking for correct number of fields
                else:
                    yield tuple(tokens)


class Respository:
    def __init__(self, wdir, pt_tables=True):
        # In what directory we are going to find data files.
        self._wdir = wdir  # directory with students, instructors and grade files
        """As we know the we are using cwid for finding students or instructor we can use it as key and make use of
           dictionary instead of list( list will go and check every cwid from beginning till end and takes lot time) """
        self._major = dict()  # key: major(str) and  value: instance of class major
        self._students = dict()  # key = cwid and value = instance of class Student
        self._instructors = dict()  # key = cwid and value = instance of class Instructor
        self._grades = dict()  # key: student's cwid and/or instructor's cwid and value: [Grade, ..]

        try:
            # getting our data files
            self._get_major(os.path.join(wdir, 'majors.txt'))
            self._get_students(os.path.join(wdir, 'students.txt'))
            self._get_instructors(os.path.join(wdir, 'instructors.txt'))
            self._get_grades(os.path.join(wdir, 'grades.txt'))
        except ValueError:
            print(ValueError)
        except FileNotFoundError:
            print(FileNotFoundError)

        if pt_tables:

            print("\nMajor Summary")
            self.major_table()

            print("\nStudent Summary")
            self.student_table()

            print("\nInstructor Summary")
            self.instructor_table()

    def _get_major(self, path):
        for major, flag, course in file_reading_gen(path, 3, sep="\t", header=True):
            if major not in self._major:
                self._major[major] = Major(major)
            self._major[major].add_course(flag, course)

    def _get_students(self, path):
        # read students from path and add to self._students
        # Allow exceptions from reading the file to flow back to the caller
        for cwid, name, major_name in file_reading_gen(path, 3, sep=";", header=True):
            if major_name not in self._major:
                print(f"Student {cwid} '{name} has unknown major '{major}'")
            else:
                # we are storing the data in students dictionary = self._students
                self._students[cwid] = Student(cwid, name, major_name, self._major[major_name])

    def _get_instructors(self, path):
        for cwid, instructor, dept in file_reading_gen(path, 3, sep="|", header=True):
            self._instructors[cwid] = Instructor(cwid, instructor, dept)

    def _get_grades(self, path):
        # read grade files and attributes the grade to appropriate student and instructor
        for student_cwid, course, grade, instructor_cwid in file_reading_gen(path, 4, sep="|", header=True):
            if student_cwid in self._students:
                self._students[student_cwid].add_course(grade, course)
            else:
                print(f"Found grade for unknown student '{student_cwid}'")

            if instructor_cwid in self._instructors:
                # will tell instructor to note that another student taking your class = add_student(course)
                self._instructors[instructor_cwid].add_student(course)
            else:
                print(f"Found grade for unknown student '{instructor_cwid}'")

    def major_table(self):
        pt = PrettyTable(field_names=Major.pt_hdr)
        for major in self._major.values():
            pt.add_row(major.pt_row())

        print(pt)

    def student_table(self):
        # inside class repository and getting only public interface data not private or protected
        pt = PrettyTable(field_names=Student.pt_hdr)
        for student in self._students.values():
            pt.add_row((student.pt_row()))

        print(pt)

    def instructor_table(self):
        pt = PrettyTable(field_names=Instructor.pt_hdr)
        for instructor in self._instructors.values():
            # each instructor may teach many classes and results in the rows for instructor may be zero, one or many
            # instructor will inform pretty table that how many rows needed
            for row in instructor.pt_row():
                pt.add_row(row)

        print(pt)


class Major:
    pt_hdr = ["Major", "Required", "Electives"]
    PASSING_GRADES = {'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C'}

    def __init__(self, dept):
        self._dept = dept
        self._required = set()  # set of all required courses for this major
        self._electives = set()  # set of electives - only one must be taken

    def add_course(self, flag, course):
        """ flag specifies required/elective course as the name of course """
        if flag.upper() not in ('R', 'E'):
            raise ValueError(f"Unexpected flag '{flag}' encountered in majors.txt")
        else:
            if flag == 'R':
                self._required.add(course)
            elif flag == 'E':
                self._electives.add(course)

    def remaining(self, courses):
        """ Given a set of courses with passing grades, compute the set of remaining required courses
            from the courses with passing grades """
        completed_courses = {course for course, grade in courses.items() if grade in Major.PASSING_GRADES}
        remaining_required = self._required - completed_courses

        if self._electives.intersection(completed_courses):
            remaining_electives = None
        else:
            remaining_electives = self._electives

        return completed_courses, remaining_required, remaining_electives

    def pt_row(self):
        return [self._dept, sorted(self._required), sorted(self._electives)]


# Each instance of class Student represent exactly one student, as the data is going to grow with time
class Student:
    pt_hdr = ["CWID", "Name", "Major", "Completed Courses", "Remaining Required", "Remaining Electives"]

    def __init__(self, cwid, name, major_name, major):
        self._cwid = cwid
        self._name = name
        self.major_name = major_name
        self._major = major
        self._courses = dict()  # key = courses and value = str with grade

    # add_course method is public
    def add_course(self, grade, course):
        self._courses[course] = grade

    def pt_row(self):
        completed_courses, remaining_required, remaining_electives = self._major.remaining(self._courses)
        return [self._cwid, self._name, self.major_name, completed_courses, remaining_required, remaining_electives]


# Each instance of class Instructor represent exactly one Instructor
class Instructor:
    pt_hdr = ["CWID", "Name", "Dept", "Course", "Students"]

    def __init__(self, cwid, name, dept):
        self._cwid = cwid
        self._name = name
        self._dept = dept
        # to count the stuff we can defaultdict and factory in defaultdict is integer
        self._courses = defaultdict(int)  # key: course name and value: student number

    def add_student(self, course):
        # Note that another student took a course with this instructor
        self._courses[course] += 1

    def pt_row(self):
        """ Note: this class function is a generator."""
        for course, count in self._courses.items():
            yield [self._cwid, self._name, self._dept, course, count]


def main():
    wdir_1 = "/home/akshay/PycharmProjects/tensorflow"
    # wdir_2 = "/home/akshay/PycharmProjects/tensorflow"
    # dir_bad_data = "/home/akshay/PycharmProjects/tensorflow/tensorflow_BadData"

    print("Good Data")
    _ = Respository(wdir_1)


'''
    print("\nBadData")
    print("should report unknown student and unknown instructor")
    _ = Respository(dir_bad_data)

    print("\nBadData\n")
    print("should report unknown student and unknown instructor")
    _ = Respository(wdir_2)
'''

if __name__ == '__main__':
    main()
