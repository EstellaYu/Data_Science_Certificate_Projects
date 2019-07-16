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
The following ERD of the tables are obtained from [Quick Database Diagrams](http://www.quickdatabasediagrams.com)
![ERD](https://github.com/EstellaYu/Data_Science_Certificate_Projects/blob/master/SQL/RESULT/ERD.png "ERD")

### Data Analysis

1. List the following details of each employee: employee number, last name, first name, gender, and salary.

2. List employees who were hired in 1986.

3. List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name, and start and end employment dates.

4. List the department of each employee with the following information: employee number, last name, first name, and department name.

5. List all employees whose first name is "Hercules" and last names begin with "B."

6. List all employees in the Sales department, including their employee number, last name, first name, and department name.

7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.

8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.

## Bonus (Optional)

As you examine the data, you are overcome with a creeping suspicion that the dataset is fake. You surmise that your boss handed you spurious data in order to test the data engineering skills of a new employee. To confirm your hunch, you decide to take the following steps to generate a visualization of the data, with which you will confront your boss:

1. Import the SQL database into Pandas. (Yes, you could read the CSVs directly in Pandas, but you are, after all, trying to prove your technical mettle.) This step may require some research. Feel free to use the code below to get started. Be sure to make any necessary modifications for your username, password, host, port, and database name:

   ```sql
   from sqlalchemy import create_engine
   engine = create_engine('postgresql://localhost:5432/<your_db_name>')
   connection = engine.connect()
   ```

* Consult [SQLAlchemy documentation](https://docs.sqlalchemy.org/en/latest/core/engines.html#postgresql) for more information.

* If using a password, do not upload your password to your GitHub repository. See [https://www.youtube.com/watch?v=2uaTPmNvH0I](https://www.youtube.com/watch?v=2uaTPmNvH0I) and [https://martin-thoma.com/configuration-files-in-python/](https://martin-thoma.com/configuration-files-in-python/) for more information.

2. Create a bar chart of average salary by title.

3. You may also include a technical report in markdown format, in which you outline the data engineering steps taken in the homework assignment.

## Epilogue

Evidence in hand, you march into your boss's office and present the visualization. With a sly grin, your boss thanks you for your work. On your way out of the office, you hear the words, "Search your ID number." You look down at your badge to see that your employee ID number is 499942.

## Submission

* Create a `.sql` file of your table schemata.

* Create a `.sql` file of your queries.

* (Optional) Create a Jupyter Notebook of the bonus analysis.

* Create and upload a repository with the above files to GitHub and post a link on BootCamp Spot.
