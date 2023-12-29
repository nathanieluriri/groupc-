import mysql.connector
import streamlit as st







def check_if_pk_exists(PK,YourTableName,yourPrimaryKeyColumn):


    # Establish a connection
    db_connection = mysql.connector.connect(
       host='svc-469e9a44-2c3e-4c14-a4c6-4c9474675828-dml.aws-virginia-6.svc.singlestore.com',
        
        # In your case your host is local and you are using root assuming you want to deploy the webapp alot will change but start with the db
        user='admin',
        password='zxROkpE7ch8vPiU8aGUosQaykRQI4rUc',
        database='User_profile'
    )


    cursor = db_connection.cursor()



    select_query = f"SELECT * FROM {YourTableName} WHERE {yourPrimaryKeyColumn} = %s"
    cursor.execute(select_query, (PK,))
    existing_row = cursor.fetchone()

    if existing_row:
        # Commit the changes to the database
        db_connection.commit()

    # Close the cursor and connection
        cursor.close()
        db_connection.close()

        return True
    else:
        db_connection.commit()
        cursor.close()
        db_connection.close()
        return False




def insert_into_user_reg(UserID,name,email):


    
    db_connection = mysql.connector.connect(
        host='svc-469e9a44-2c3e-4c14-a4c6-4c9474675828-dml.aws-virginia-6.svc.singlestore.com',
        
        # In your case your host is local and you are using root assuming you want to deploy the webapp alot will change but start with the db
        user='admin',
        password='zxROkpE7ch8vPiU8aGUosQaykRQI4rUc',
        database='User_profile'
    )


    cursor = db_connection.cursor()


    # Define your SQL query for insertion
    insert_query = f""" 
        INSERT INTO Users (UserID, name, email)
        VALUES (%s, %s, %s)
    """

    # Data to be inserted
    data_to_insert = (f"{UserID}", f"{name}", f"{email}")

    # Execute the query
    cursor.execute(insert_query, data_to_insert)

    # Commit the changes to the database
    db_connection.commit()

    # Close the cursor and connection
    cursor.close()
    db_connection.close()


def fk_status_profile_completeness(UID):
    db_connection = mysql.connector.connect(
      host='svc-469e9a44-2c3e-4c14-a4c6-4c9474675828-dml.aws-virginia-6.svc.singlestore.com',
    
        # In your case your host is local and you are using root assuming you want to deploy the webapp alot will change but start with the db
        user='admin',
        password='zxROkpE7ch8vPiU8aGUosQaykRQI4rUc',
        database='User_profile'
    )
    cursor = db_connection.cursor()


    select_query = "SELECT * FROM Ai_personalized_guide_for_users WHERE UserID = %s"
    cursor.execute(select_query, (UID,))
    existing_row = cursor.fetchone()
    if existing_row: 
        db_connection.commit()
        cursor.close()
        db_connection.close()
        return True  #  key exists
    else:
        db_connection.commit()
        cursor.close()
        db_connection.close()
        return False  # key doesn't exist



def insert_into_ai_personalized_guide_for_users(UserID,reading_speed,level_of_understanding,diction):


    
    db_connection = mysql.connector.connect(
        host='svc-469e9a44-2c3e-4c14-a4c6-4c9474675828-dml.aws-virginia-6.svc.singlestore.com',
        
        # In your case your host is local and you are using root assuming you want to deploy the webapp alot will change but start with the db
        user='admin',
        password='zxROkpE7ch8vPiU8aGUosQaykRQI4rUc',
        database='User_profile'
    )


    cursor = db_connection.cursor()


    # Define your SQL query for insertion
    insert_query = f""" 
        INSERT INTO Ai_personalized_guide_for_users (UserID, reading_speed, level_of_understanding,diction)
        VALUES (%s, %s, %s,%s)
    """

    # Data to be inserted
    data_to_insert = (f"{UserID}", f"{reading_speed}", f"{level_of_understanding}",f"{diction}")

    # Execute the query
    cursor.execute(insert_query, data_to_insert)

    # Commit the changes to the database
    db_connection.commit()

    # Close the cursor and connection
    cursor.close()
    db_connection.close()