-- 1. Create the DEPARTMENTS table (Assuming location is here)
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL,
    location VARCHAR(50)
);

-- 2. Create the EMPLOYEES table (using 'staff' later as per task #45)
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    salary INT,
    hire_date DATE,
    dept_id INT,
   
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);
-- Insert data into DEPARTMENTS
INSERT INTO departments (dept_id, dept_name, location) VALUES
(10, 'IT', 'Bangalore'),
(20, 'Sales', 'Mumbai'),
(30, 'HR', 'Bangalore'),
(40, 'Finance', 'New Delhi'),
(50, 'Marketing', NULL); -- For query #19 (Find departments with no employees)

-- Insert data into EMPLOYEES
INSERT INTO employees (emp_id, first_name, last_name, salary, hire_date, dept_id) VALUES
(101, 'Amit', 'Sharma', 65000, '2019-06-15', 10), -- IT, > 50000, Starts with 'A'
(102, 'Ravi', 'Kumar', 45000, '2021-01-20', 20), -- Sales, Hired after 2020, Dept change target
(103, 'Priya', 'Verma', 72000, '2018-03-10', 10), -- IT, Highest paid
(104, 'Anjali', 'Gupta', 51000, '2020-09-01', 30), -- HR, Starts with 'A'
(105, 'Deepak', 'Singh', 38000, '2022-04-05', 40), -- Finance, Lowest paid, Delete target
(106, 'Kavya', 'Reddy', 58000, '2023-11-28', 20), -- Sales, Most recent
(107, 'Rahul', 'Jain', 68000, '2019-07-22', 10), -- IT, Second highest (for now)
(108, 'Sunita', 'Yadav', 54000, '2020-05-01', 30), -- HR
(109, 'Bhavana', 'Patil', 64000, '2020-02-14', 10), -- IT
(110, 'John', 'Doe', 67000, '2018-08-25', NULL); -- No department (for query #18)