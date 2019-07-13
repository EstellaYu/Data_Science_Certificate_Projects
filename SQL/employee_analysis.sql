-- Database: employee_analysis

-- CREATE DATABASE employee_analysis;
CREATE DATABASE employee_analysis
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
	
---------------------------------------------------
----------------- CREATE TABLE --------------------
---------------------------------------------------
	
-- DROP TABLE IF NOT EXIST
DROP TABLE IF EXISTS employee CASCADE;
-- CREATE TABLE employee
----------------------
CREATE TABLE employee (
	emp_no int PRIMARY KEY,
	birth_date date,
	first_name varchar(30),
	last_name varchar(30),
	gender char(1),
	hire_date date
);

-- DROP TABLE IF NOT EXIST
DROP TABLE IF EXISTS title;
-- CREATE TABLE title
----------------------
CREATE TABLE title (
	emp_no int,
	title varchar(200),
	from_date date ,
	to_date date,
	FOREIGN KEY (emp_no) REFERENCES employee(emp_no)
);

-- DROP TABLE IF NOT EXIST
DROP TABLE IF EXISTS dept CASCADE;
-- CREATE TABLE dept (DEPARTMENT)
----------------------
CREATE TABLE dept (
	dept_no varchar(30) PRIMARY KEY,
	dept_name varchar(30)
);

-- DROP TABLE IF NOT EXIST
DROP TABLE IF EXISTS dept_m;
-- CREATE TABLE dept_m (DEPARTMENT MANAGER)
----------------------
CREATE TABLE dept_m (
	dept_no varchar(30),
	emp_no int,
	from_date date,
	to_date date,
	FOREIGN KEY (dept_no) REFERENCES dept(dept_no),
	FOREIGN KEY (emp_no) REFERENCES employee(emp_no)
);

-- DROP TABLE IF NOT EXIST
DROP TABLE IF EXISTS dept_e;
-- CREATE TABLE dept_e (DEPARTMENT EMOLOYEE)
----------------------
CREATE TABLE dept_e (
	emp_no int,
	dept_no varchar(30),
	from_date date,
	to_date date,
	FOREIGN KEY (dept_no) REFERENCES dept(dept_no),
	FOREIGN KEY (emp_no) REFERENCES employee(emp_no)
);

-- DROP TABLE IF NOT EXIST
DROP TABLE IF EXISTS salaries;
-- CREATE TABLE salary (FIRST YEAR SALARY)
----------------------
CREATE TABLE salaries (
	emp_no int PRIMARY KEY,
	salary money,
	from_date date,
	to_date date,
	FOREIGN KEY (emp_no) REFERENCES employee(emp_no)
);

---------------------------------------------------
------------------- ANALYSIS ----------------------
---------------------------------------------------
-- 1. List the following details of each employee: 
--    employee number, last name, first name, gender, and salary.
-- 1) number of employees --- ANS: 300024
	SELECT 
		COUNT(DISTINCT emp_no) 
	FROM employee;
-- 2) list employee detail
	SELECT emp.emp_no as employee_number, 
		   emp.last_name, emp.first_name, emp.gender, 
		   salaries.salary
	FROM employee as emp
	INNER JOIN salaries ON emp.emp_no = salaries.emp_no;

-- 2. List employees who were hired in 1986.
-- 1) number of employees hired in 1986 --- ANS: 36150
	SELECT COUNT(DISTINCT emp_no) 
	FROM employee
	WHERE EXTRACT(YEAR FROM hire_date) = 1986;
-- 2) list detail of employees hire in 1986
	SELECT emp_no, last_name, first_name, 
		   EXTRACT(YEAR FROM hire_date) AS hired_year
	FROM employee 
	WHERE EXTRACT(YEAR FROM hire_date) = 1986;

-- 3. List the manager of each department with the following information: 
-- department number, department name, the manager's employee number, 
-- last name, first name, and start and end employment dates.
-- NOTE: for employees with different positions, choose the last to_date in dept_e
	SELECT dept.dept_no, dept.dept_name, 
		   dept_m.emp_no, emp.last_name, emp.first_name,
		   emp.hire_date as start_employment_date,
		   end_T.end_employment_date
	FROM (((dept_m
	INNER JOIN dept ON dept.dept_no = dept_m.dept_no)
	INNER JOIN employee as emp ON emp.emp_no = dept_m.emp_no)
	INNER JOIN 
		(SELECT emp_no, MAX(to_date) as end_employment_date
		 FROM dept_e
		 GROUP BY emp_no) end_T 
		 ON end_T.emp_no = dept_m.emp_no);

-- 4. List the department of each employee with the following information: 
-- employee number, last name, first name, and department name.
	SELECT * FROM dept_e;

-- 5. List all employees whose first name is "Hercules" and last names begin with "B."
	SELECT emp_no, last_name, first_name 
	FROM employee
	WHERE first_name = 'Hercules' AND last_name like 'B%';

-- 6. List all employees in the Sales department, 
-- including their employee number, last name, first name, and department name.
-- 1) all the employees in Salse department
	SELECT emp.emp_no, emp.last_name, emp.first_name, dept.dept_name
	FROM ((dept_e
	INNER JOIN employee AS emp ON emp.emp_no = dept_e.emp_no)
	INNER JOIN dept ON dept.dept_no = dept_e.dept_no)
	WHERE UPPER(dept.dept_name) = 'SALES';
-- 2) number of employee in Sales --- ANS : 52245
	SELECT COUNT(*) FROM (
		SELECT emp.emp_no, emp.last_name, emp.first_name, dept.dept_name
		FROM ((dept_e
		INNER JOIN employee AS emp ON emp.emp_no = dept_e.emp_no)
		INNER JOIN dept ON dept.dept_no = dept_e.dept_no)
		WHERE UPPER(dept.dept_name) LIKE 'SALES'
	) SALES;

-- 7. List all employees in the Sales and Development departments, 
-- including their employee number, last name, first name, and department name.
	SELECT emp.emp_no, emp.last_name, emp.first_name, dept.dept_name
	FROM ((dept_e
	INNER JOIN employee AS emp ON emp.emp_no = dept_e.emp_no)
	INNER JOIN dept ON dept.dept_no = dept_e.dept_no)
	WHERE dept.dept_name = 'Sales' OR dept.dept_name = 'Development';
	
-- 8. In descending order, list the frequency count of 
-- employee last names, i.e., how many employees share each last name.
	SELECT COUNT(distinct emp_no), last_name FROM employee
	GROUP BY last_name
	ORDER BY COUNT(distinct emp_no) desc;
	
