import mysql.connector
from mysql.connector import Error

from config import DB_CONFIG

# main connection point for the python code to connect to the database


def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

# SELECTS


def get_all_members():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Members")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results


def get_member_by_id(member_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Members WHERE MemberID = %s", (member_id,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results


def get_member_by_email(email):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Members WHERE Email = %s", (email,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results


def get_member_by_name(name):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Members WHERE Name = %s", (name,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

# Updates


def update_member_plan(member_id, new_plan_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Members SET PlanID = %s WHERE MemberID = %s",
        (new_plan_id, member_id),
    )
    conn.commit()
    cursor.close()
    conn.close()


def update_member_contact(member_id, new_email, new_phone):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Members SET Email = %s, Phone = %s WHERE MemberID = %s",
        (new_email, new_phone, member_id),
    )
    conn.commit()
    cursor.close()
    conn.close()


def update_booking_status(booking_id, new_status):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Bookings SET Status = %s WHERE BookingID = %s",
        (new_status, booking_id),
    )
    conn.commit()
    cursor.close()
    conn.close()


def update_payment_status(payment_id, new_status):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Payments SET Status = %s WHERE PaymentID = %s",
        (new_status, payment_id),
    )
    conn.commit()
    cursor.close()
    conn.close()


def update_class_schedule(class_id, new_schedule, new_capacity):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Classes SET Schedule = %s, Capacity = %s WHERE ClassID = %s",
        (new_schedule, new_capacity, class_id)
    )
    conn.commit()
    cursor.close()
    conn.close()


def delete_booking(booking_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "DELETE FROM Bookings WHERE BookingID = %s", (booking_id,))
        conn.commit()
    except mysql.connector.Error as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

# Inserts:


def add_member(member_id, name, email, phone, dob, join_date, plan_id, zipcode):
    if not all([member_id, name, email, phone, dob, join_date, plan_id, zipcode]):
        return "Error: All member fields are mandatory. No NULL values allowed."
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = """
            INSERT INTO Members (MemberID, Name, Email, Phone, DOB, JoinDate, PlanID, Zipcode)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (member_id, name, email, phone,
                       dob, join_date, plan_id, zipcode),)
        conn.commit()
        return f"{name} added"
    except Error as e:
        conn.rollback()
        return f"Database Error: {e}"
    finally:
        cursor.close()
        conn.close()


def delete_payment(payment_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "DELETE FROM Payments WHERE PaymentID = %s", (payment_id,))
        conn.commit()
    except mysql.connector.Error as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()


def book_class(booking_id, member_id, class_id, booking_date):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT Capacity FROM Classes WHERE ClassID = %s", (class_id,))
        capacity_row = cursor.fetchone()
        cursor.execute(
            "SELECT COUNT(*) FROM Bookings WHERE ClassID = %s", (class_id,))
        current_bookings = cursor.fetchone()[0]
        if not capacity_row:
            return f"Error: Class {class_id} does not exist."
        if current_bookings >= capacity_row[0]:
            return f"Booking Failed: Class {class_id} is at maximum capacity."

        query = """
            INSERT INTO Bookings (BookingID, MemberID, ClassID, BookingDate, Status)
            VALUES (%s, %s, %s, %s, 'Confirmed')
        """
        cursor.execute(query, (booking_id, member_id, class_id, booking_date))
        conn.commit()
        return f"Class {class_id} booked successfully."
    except Error as e:
        conn.rollback()
        return f"Database Error: {e}"
    finally:
        cursor.close()
        conn.close()


def delete_class(class_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM Classes WHERE ClassID = %s", (class_id,))
        conn.commit()
    except mysql.connector.Error as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()


def record_payment(payment_id, member_id, amount, pay_date, method, status):
    if float(amount) <= 0:
        return f"Error: Payment amount {amount} must be greater than zero."
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = """
            INSERT INTO Payments (PaymentID, MemberID, Amount, PayDate, Method, Status)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (payment_id, member_id,
                       amount, pay_date, method, status))
        conn.commit()
        return f"Payment {payment_id} recorded successfully."
    except Error as e:
        conn.rollback()
        return f"Database Error: {e}"
    finally:
        cursor.close()
        conn.close()


def delete_member(member_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "DELETE FROM Bookings WHERE MemberID = %s", (member_id,))
        cursor.execute(
            "DELETE FROM Payments WHERE MemberID = %s", (member_id,))
        cursor.execute("DELETE FROM Members WHERE MemberID = %s", (member_id,))
        conn.commit()
    except mysql.connector.Error as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()


def add_staff(staff_id, name, role, email, phone, zipcode):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = """
            INSERT INTO Staff (StaffID, Name, Role, Email, Phone, Zipcode)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (staff_id, name, role, email, phone, zipcode))
        conn.commit()
        return f"Staff {name} added successfully."
    except Error as e:
        conn.rollback()
        return f"Database Error: {e}"
    finally:
        cursor.close()
        conn.close()
