class Student:
	def __init__(self, name):
		self.name = name
		self.classes = {}

	def calculateGPA(self):
		gradeMap = {
			'A': 4.0,
			'B': 3.0,
			'C': 2.0,
			'D': 1.0,
			'F': 0.0
		}
		if not self.classes:
			return "N/A"

		iCount = 0
		total = 0
		for k in self.classes:
			v = self.classes[k]
			total += gradeMap[v]
			iCount += 1

		gpa = "%f" % (total / iCount)
		return gpa

	def getGPA(self):
		return self.calculateGPA()

	def setGrade(self, sub, letter_grade):
		self.classes[sub.name] = letter_grade
