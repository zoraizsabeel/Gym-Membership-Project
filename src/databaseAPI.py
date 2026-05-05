import mysql.connector
from config import DB_CONFIG


def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)


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
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Members WHERE MemberID = %s", (member_id))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results


def update_member_plan(member_id, new_plan_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Members SET PlanID = %s WHERE MemberID = %s",
        (new_plan_id, member_id)
    )
    conn.commit()
    cursor.close()
    conn.close()


def update_member_contact(member_id, new_email, new_phone):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Members SET Email = %s, Phone = %s WHERE MemberID = %s",
        (new_email, new_phone, member_id)
    )
    conn.commit()
    cursor.close()
    conn.close()


def update_booking_status(booking_id, new_status):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Bookings SET Status = %s WHERE BookingID = %s",
        (new_status, booking_id)
    )
    conn.commit()
    cursor.close()
    conn.close()


def update_payment_status(payment_id, new_status):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Payments SET Status = %s WHERE PaymentID = %s",
        (new_status, payment_id)
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
