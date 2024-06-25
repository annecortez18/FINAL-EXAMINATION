from connector import Connector

class Employee:
    
    @staticmethod
    def get_all():
         query = "SELECT * FROM employees"
         try:
               Connector.cursor.execute(query)
               result = Connector.cursor.fetchall()
               return result
         except Exception as e:
               print(f"Error in get_all: {e}")
               return []

    @staticmethod
    def add_employee(emp_id, lname, fname, mname):
        query = "INSERT INTO employees (employee_id, lname, fname, mname) VALUES (%s, %s, %s, %s,)"
        try:
               Connector.cursor.execute(querey,(emp_id, lname, fname, mname))
               Connector.db.commit()
               print("Employee added successfully")
               return True
        except Exception as e:
            print(f"Error in add_employee:")
            return False

    @staticmethod
    def get_employee(emp_id):
        query = "SELECT * FROM employees WHERE employee_id = %s"
        try:
            Connector.cursor.execute(query, (emp_id,))
            result = Connector.cursor.fetchone()
            return result
        except Exception as e:
            print(f"Error in get_employee: {e}")
            return None

    @staticmethod
    def update_employee(emp_id, lname, fname, mname):
        query = "UPDATE employees SET lname = %s, fname = %s, mname = %s WHERE employee_id = %s"
        try:
            Connector.cursor.execute(query, (lname, fname, mname, emp_id))
            Connector.db.commit()
            print(f"Employee {emp_id} updated successfully")
            return True
        except Exception as e:
            print(f"Error in update_employee: {e}")
            return False

    @staticmethod
    def delete_employee(emp_id):
        query = "DELETE FROM employees WHERE employee_id = %s"
        try:
            Connector.cursor.execute(query, (emp_id,))
            Connector.db.commit()
            print(f"Employee {emp_id} deleted successfully")
            return True
        except Exception as e:
            print(f"Error in delete_employee: {e}")
            return False

