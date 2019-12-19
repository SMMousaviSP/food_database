import pymysql

def search(ingredients):
    # Change HOST, USER, PASSWORD and DB to yours
    HOST = '127.0.0.1'
    USER = 'your_username'
    PASSWORD = 'your_password'
    DB = 'your_database'

    connection = pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=DB)
    cursor = connection.cursor()
    result = [x for x in range(4)]

    # SQL code to check if there is a record with all three ingredients
    sql0 = 'SELECT * FROM `dish` WHERE ingredients LIKE "%' + ingredients[0] + \
           '%" AND ingredients LIKE "%' + ingredients[1] + \
           '%" AND ingredients LIKE "%' + ingredients[2] + '%";'
    cursor.execute(sql0)
    result[0] = cursor.fetchall()
    # If there's any record then return it
    if len(result[0]) > 0:
        print(f"{len(result[0])} Record Found with all 3 ingredients.")
        return result[0]

    mostFrequentList = [{"count": 0} for x in range(3)]

    sql1 = 'SELECT * FROM `dish` WHERE ingredients LIKE "%' + ingredients[0] + \
           '%" AND ingredients LIKE "%' + ingredients[1] + '%";'
    cursor.execute(sql1)
    result[1] = cursor.fetchall()
    result[1] = tuple_to_list(result[1])
    if len(result[1]) > 0:
        mostFrequentList[0] = most_frequent(ingredient1=ingredients[0],
                                            ingredient2=ingredients[1],
                                            ingredient3=ingredients[2],
                                            li=result[1],
                                            index=1)


    sql2 = 'SELECT * FROM `dish` WHERE ingredients LIKE "%' + ingredients[0] + \
           '%" AND ingredients LIKE "%' + ingredients[2] + '%";'
    cursor.execute(sql2)
    result[2] = cursor.fetchall()
    result[2] = tuple_to_list(result[2])
    if len(result[2]) > 0:
        mostFrequentList[1] = most_frequent(ingredient1=ingredients[0],
                                            ingredient2=ingredients[2],
                                            ingredient3=ingredients[1],
                                            li=result[2],
                                            index=2)


    sql3 = 'SELECT * FROM `dish` WHERE ingredients LIKE "%' + ingredients[1] + \
           '%" AND ingredients LIKE "%' + ingredients[2] + '%";'
    cursor.execute(sql3)
    result[3] = cursor.fetchall()
    result[3] = tuple_to_list(result[3])
    if len(result[3]) > 0:
        mostFrequentList[2] = most_frequent(ingredient1=ingredients[1],
                                            ingredient2=ingredients[2],
                                            ingredient3=ingredients[0],
                                            li=result[3],
                                            index=3)

    maxFrequent = max(mostFrequentList, key=lambda x: x["count"])
    if maxFrequent["count"] == 0:
        print("Not Found")
        return([])
    print(f"{maxFrequent['count']} Record " \
          f"Found By {maxFrequent['ingredient1']} and " \
          f"{maxFrequent['ingredient2']}. " \
          f"{maxFrequent['maxIngredients']} should be changed to " \
          f"{maxFrequent['changeIngredient']}")
    return change(li=result[maxFrequent["index"]],
                  defaultIngredient=maxFrequent["maxIngredients"],
                  changeIngredient=maxFrequent["changeIngredient"])


def most_frequent(ingredient1, ingredient2, ingredient3, li, index):
    countDict = {}
    for i in li:
        for j in i[2]:
            if j == ingredient1 or j == ingredient2:
                continue
            if j in countDict:
                countDict[j] += 1
            else:
                countDict[j] = 1


    maxIngredients = max(countDict, key=countDict.get)
    # maxIngredients should change to changeIngredient
    return {"count": countDict[maxIngredients], "index": index,
            "maxIngredients": maxIngredients, "changeIngredient": ingredient3,
            "ingredient1": ingredient1, "ingredient2": ingredient2}


def change(li, defaultIngredient, changeIngredient):
    for i in li:
        for j in range(len(i[2])):
            if i[2][j] == defaultIngredient:
                i[2][j] = changeIngredient
    return li


def tuple_to_list(tu):
    li = [list(x) for x in tu]
    for i in range(len(li)):
        li[i][2] = [x.strip() for x in li[i][2].split(',')]
    return li


# Program Starts From HERE:
a1 = ['bacon', 'chicken', 'tomato']
a2 = ['XXXXX', 'chicken', 'tomato']
print("---------------FIRST----------------")
print(search(a1))
print("--------------SECOND----------------")
print(search(a2))
