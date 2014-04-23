import unittest
from Student import Student
from Subject import Subject
from decimal import *

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

        j_gpa = Decimal(j.getGPA())
        m_gpa = Decimal(m.getGPA())
        b_gpa = Decimal(b.getGPA())

        print "j=" + str(j_gpa)
        print "m=" + str(m_gpa)
        print "b=" + str(b_gpa)

        assert((j_gpa > 3.67) and (j_gpa < 3.67))
        assert(m_gpa > 3.16 and m_gpa < 3.17) # fails
        assert(b_gpa < 2.01 and b_gpa > 1.99)

if __name__ == '__main__':
    unittest.main()
