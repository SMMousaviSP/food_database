import pymysql

def search(ingredients):
    # Change HOST, USER, PASSWORD and DB to yours
    HOST = '127.0.0.1'
    USER = 'mohammad'
    PASSWORD = 'mA6678Am'
    DB = 'Food'

    connection = pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=DB)
    cursor = connection.cursor()

    # SQL code to check if there is a record with all three ingredients
    sql0 = 'SELECT * FROM `dish` WHERE ingredients LIKE "%' + ingredients[0] +
           '%" AND ingredients LIKE "%' + ingredients[1] +
           '%" AND ingredients LIKE "%' + ingredients[2] + '%";'
    cursor.execute(sql0)
    result = cursor.fetchall()
    # If there's any record then return it
    if len(result) > 0:
        print("Found with all 3 ingredients.")
        return result


    sql1 = 'SELECT * FROM `dish` WHERE ingredients LIKE "%' + ingredients[0] +
           '%" AND ingredients LIKE "%' + ingredients[1] + '%";'
    cursor.execute(sql1)
    result = cursor.fetchall()
    most_frequent1 = most_frequent(ingredients[0], ingredients[1], list(result[2]))


    sql2 = 'SELECT * FROM `dish` WHERE ingredients LIKE "%' + ingredients[0] +
           '%" AND ingredients LIKE "%' + ingredients[2] + '%";'
    cursor.execute(sql2)
    result = cursor.fetchall()
    most_frequent2 = most_frequent(ingredients[0], ingredients[2], list(result[2]))


    sql3 = 'SELECT * FROM `dish` WHERE ingredients LIKE "%' + ingredients[1] +
           '%" AND ingredients LIKE "%' + ingredients[2] + '%";'
    cursor.execute(sql3)
    result = cursor.fetchall()
    most_frequent1 = most_frequent(ingredients[1], ingredients[2], list(result[2]))



def most_frequent(ingredients1, ingredients2, li):
    pass
