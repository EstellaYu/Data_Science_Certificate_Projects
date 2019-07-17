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
		   dept_m.from_date as "Start Employment Date",
		   dept_m.to_date as "End Employment Date"
	FROM ((dept_m
	INNER JOIN dept ON dept.dept_no = dept_m.dept_no)
	INNER JOIN employee as emp ON emp.emp_no = dept_m.emp_no);

-- 4. List the department of each employee with the following information: 
-- employee number, last name, first name, and department name.
-- 1) with all record of possible repeated departments history
	SELECT dept_e.emp_no, emp.last_name, emp.first_name,
		   dept.dept_name
	FROM ((dept_e
	INNER JOIN employee as emp ON emp.emp_no = dept_e.emp_no)
	INNER JOIN dept ON dept.dept_no = dept_e.dept_no)
	ORDER BY emp_no;
-- 2) with only the most up-to-date department info for each employee	
	SELECT dept_e.emp_no, emp.last_name, emp.first_name, dept.dept_name
	FROM (((dept_e
		INNER JOIN 
				(SELECT emp_no, MAX(to_date) as lastest_to_date FROM dept_e
				GROUP BY emp_no) dept_e_up_to_date
			ON dept_e.to_date = dept_e_up_to_date.lastest_to_date
			AND dept_e.emp_no = dept_e_up_to_date.emp_no)
		INNER JOIN employee AS emp ON emp.emp_no = dept_e.emp_no)
		INNER JOIN dept ON dept.dept_no = dept_e.dept_no)
	ORDER BY dept_e.emp_no;

-- 5. List all employees whose first name is "Hercules" and 
-- last names begin with "B."
	SELECT emp_no, last_name, first_name 
	FROM employee
	WHERE first_name = 'Hercules' AND last_name like 'B%'
	ORDER BY emp_no;

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
	SELECT COUNT(distinct emp_no) as "Repeated Last Name Frequency",
		   last_name FROM employee
	GROUP BY last_name
	ORDER BY COUNT(distinct emp_no) desc;
	
