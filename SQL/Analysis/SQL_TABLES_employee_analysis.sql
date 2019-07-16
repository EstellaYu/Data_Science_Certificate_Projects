-------------------------------------------------------
----------------- CREATE DATA BASE --------------------
-------------------------------------------------------
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
	
-- CREATE TABLE employee
----------------------
DROP TABLE IF EXISTS employee CASCADE;
CREATE TABLE employee (
	emp_no int PRIMARY KEY,
	birth_date date,
	first_name varchar(30),
	last_name varchar(30),
	gender char(1),
	hire_date date
);

-- CREATE TABLE dept (DEPARTMENT)
----------------------
DROP TABLE IF EXISTS dept CASCADE;
CREATE TABLE dept (
	dept_no varchar(30) PRIMARY KEY,
	dept_name varchar(30)
);


-- CREATE TABLE title
----------------------
DROP TABLE IF EXISTS title;
CREATE TABLE title (
	emp_no int,
	title varchar(200),
	from_date date,
	to_date date,
	FOREIGN KEY (emp_no) REFERENCES employee(emp_no)
);


-- CREATE TABLE dept_m (DEPARTMENT MANAGER)
----------------------
DROP TABLE IF EXISTS dept_m;
CREATE TABLE dept_m (
	dept_no varchar(30),
	emp_no int,
	from_date date,
	to_date date,
	FOREIGN KEY (dept_no) REFERENCES dept(dept_no),
	FOREIGN KEY (emp_no) REFERENCES employee(emp_no)
);

-- CREATE TABLE dept_e (DEPARTMENT EMOLOYEE)
----------------------
DROP TABLE IF EXISTS dept_e;
CREATE TABLE dept_e (
	emp_no int,
	dept_no varchar(30),
	from_date date,
	to_date date,
	FOREIGN KEY (dept_no) REFERENCES dept(dept_no),
	FOREIGN KEY (emp_no) REFERENCES employee(emp_no)
);

-- CREATE TABLE salary (FIRST YEAR SALARY)
----------------------
DROP TABLE IF EXISTS salaries;
CREATE TABLE salaries (
	emp_no int PRIMARY KEY,
	salary money,
	from_date date, -- Note: same as hire_date
	to_date date,
	FOREIGN KEY (emp_no) REFERENCES employee(emp_no)
);
