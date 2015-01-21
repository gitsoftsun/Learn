#coding=utf8
#test python object

class Employee:
	'所有员工的基类'
	empCount =0; #the number of employee
	def __init__(self, name, salary):
		self.name = name;
		self.salary = salary;
		Employee.empCount += 1;
	def displayEmployee(self):
		print 'employee name %s, salary %d' %(self.name, self.salary);
	def displayEmpCount(self):
		print 'the number of employee is :', format(Employee.empCount, '5');
	def work(self):
		print 'my job is coding';
	def __del__(self):
		class_name = self.__class__.__name__;
		print class_name, " destoryed";

		

# create an object
# emp1 = Employee('ls', 20003);
# emp2 = Employee('zs', 88000);

# emp2.age = 23;
# emp2.displayEmployee();
# emp2.displayEmpCount();

# print getattr(emp2, 'age');

print Employee.__doc__;
print Employee.__name__
print Employee.__bases__;

print Employee.__dict__


#析构函数
emp3 = Employee('ww', 6000);
emp4 = emp3;
emp5 = emp3;
print id(emp3), id(emp4), id(emp5);
# del emp3;

#对象调用非类方法
emp6 = Employee('sl', 4500);
emp6.work();