from connector import Connector

class Employee:

    def get_all():
        query = "SELECT * FROM employees"

        Connector.cursor.execute(query)
        result = Connector.cursor.fetchall()

        return result

        def add_employee(emp_id, lname, fname, mname):
            query = "INSERT INTO employees VALUES (%s, %s, %s, %s,)"

            try:
                Connector.cursor.execute(querey,(emp_id, lname, fname, mname))
                Connector.db.commit()

                return True
            except:
                return False