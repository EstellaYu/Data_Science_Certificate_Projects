# SQL Analysis on Employee Database

## Background
Contained in [data](https://github.com/EstellaYu/Data_Science_Certificate_Projects/tree/master/SQL/data) is a research project on employees from a corporation from the 1980s and 1990s. All that remain of the database of employees from that period are six CSV files
* `employee.csv`
* `departments.csv` 
* `dept_emp.csv`
* `dept_manager.csv`
* `titles.csv`

In the following analysis, the following operations are performed:
   1) **design tables** to hold the data, 
   2) **import** the CSVs into a **SQL database**, 
   3) perform different **SQL queries** to extract insightful information, and 
   4) import SQL database to jupyter notebook using **SQLAlchemy for visulalization**
   
## Analysis

### Data Modeling (ERD of tables)
An `Entity Relationship Diagram` (`ERD`) is a snapshot of data structures. An Entity Relationship Diagram shows entities (tables) in a database and relationships between tables within that database. For a good database design it is essential to have an Entity Relationship Diagram. (QUOTE FROM [datanamic](https://www.datanamic.com/dezign/erdiagramtool.html))  
The following ERD of the tables are obtained from [QuickDatabaseDiagrams.com](http://www.quickdatabasediagrams.com)
![ERD](https://github.com/EstellaYu/Data_Science_Certificate_Projects/blob/master/SQL/RESULT/ERD.png "ERD")

### Data Analysis
-- For clearity, only the first 10 rows are shown for most of the query results

1. List the following details of each employee: employee number, last name, first name, gender, and salary.
![employee](https://github.com/EstellaYu/Data_Science_Certificate_Projects/blob/master/SQL/RESULT/1_employee_detail_and_salary.png 'employee')

2. List employees who were hired in 1986.
![employee1986](https://github.com/EstellaYu/Data_Science_Certificate_Projects/blob/master/SQL/RESULT/2_employee_hired_in_1986.png 'employee1986')

3. List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name, and start and end employment dates.
![3](https://github.com/EstellaYu/Data_Science_Certificate_Projects/blob/master/SQL/RESULT/3_managers_in_each_department.png '3')

4. List the department of each employee with the following information: employee number, last name, first name, and department name.
![4](https://github.com/EstellaYu/Data_Science_Certificate_Projects/blob/master/SQL/RESULT/4_employee_and_departments.png '4')

5. List all employees whose first name is "Hercules" and last names begin with "B."
![5](https://github.com/EstellaYu/Data_Science_Certificate_Projects/blob/master/SQL/RESULT/5_employee_named_Herculus_B.png '5')

6. List all employees in the Sales department, including their employee number, last name, first name, and department name.
![6](https://github.com/EstellaYu/Data_Science_Certificate_Projects/blob/master/SQL/RESULT/6_employee_in_Sales.png '6')

7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
![7](https://github.com/EstellaYu/Data_Science_Certificate_Projects/blob/master/SQL/RESULT/7_employee_in_Sales_and_Development.png '7')

8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
![8](https://github.com/EstellaYu/Data_Science_Certificate_Projects/blob/master/SQL/RESULT/8_employee_last_name_frequency.png '8')

## Visualization in SQLAlchemy

While the data, a creeping suspicion came up that the dataset is fake. To confirm your hunch, **`SQLAlchemy`** is used to import the database in Jupyter Notebook in order to generate a visualization of the data...

Here is a bar chart of average salary by title.
![bar](https://github.com/EstellaYu/Data_Science_Certificate_Projects/blob/master/SQL/RESULT/average_salary_entry_titles.png 'bar')
