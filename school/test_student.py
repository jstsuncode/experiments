import unittest
from Student import Student
from Subject import Subject

class StudentTest(unittest.TestCase):

    def test_Student(self):
        cen = Subject('English')
        cma = Subject('Math')
        cph = Subject('Physics')
        chi = Subject('History')
        cmu = Subject('Music')
        cpe = Subject('P.E.')
        j = Student('John')
        m = Student('Mary')
        b  = Student('Bob')
        c  = Student('Chris')
        
        j.setGrade(cen, 'A')
        j.setGrade(cma, 'B')
        j.setGrade(cph, 'A')
        j.setGrade(chi, 'B')
        j.setGrade(cmu, 'A')
        j.setGrade(cpe, 'A')
        
        m.setGrade(cen, 'A')
        m.setGrade(cma, 'C')
        m.setGrade(cph, 'A')
        m.setGrade(chi, 'B')
        m.setGrade(cmu, 'C')
        m.setGrade(cpe, 'A')

        b.setGrade(cen, 'C')
        b.setGrade(cma, 'F')
        b.setGrade(cph, 'D')
        b.setGrade(chi, 'B')
        b.setGrade(cmu, 'C')
        b.setGrade(cpe, 'A')

        print j.getGPA()
        print m.getGPA()
        print b.getGPA()

if __name__ == '__main__':
    unittest.main()
