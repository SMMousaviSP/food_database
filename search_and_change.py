# import pymysql
#
# HOST = '127.0.0.1'
# USER = 'mohammad'
# PASSWORD = 'mA6678Am'
# DB = 'Food'
#
# connection = pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=DB)
#
# a1 = connection.cursor()
a = ['bacon', 'chicken', 'tomato']
# sql1 = 'SELECT * FROM `dish` WHERE ingredients LIKE "%' + a[0] + '%" AND ingredients LIKE "%' + a[1] + '%" AND ingredients LIKE "%' + a[2] + '%";'
#
# b1 = connection.cursor()
b = ['xxxxx', 'chicken', 'tomato']
# sql2 = 'SELECT * FROM `dish` WHERE ingredients LIKE "%' + a[1] + '%" AND ingredients LIKE "%' + a[2] + '%";'
#
# a1.execute(sql1)
# x = a1.fetchall()
#
# b1.execute(sql2)
# y = b1.fetchall()

# Matched
x = ((7, 'Grilled Chicken Tomato salad', 'chicken, tomato, avocado, bacon, egg, cheese, bean.', 'Heat grill to medium-high heat. Brush chicken with oil; season with salt and pepper, to taste. Grill 8 to 12 minutes or until no longer pink in the center, turning once. Cool chicken enough to handle; slice into thin strips. Combine salad blend, tomatoes from the pouch, cooked sliced chicken, avocado, bacon, egg, and blue cheese in a large bowl. Toss with blue cheese dressing, to taste'), (9, 'Chicken Salad tomato', 'bacon, chicken, tomato, celery, lemon,  lettuce, avocado', 'Place bacon in a large skillet and cook over medium-high heat, turning occasionally, until evenly browned about 10 minutes. Drain bacon slices on paper towels; crumble. Stir chicken, bacon, tomato, and celery together in a bowl. Whisk mayonnaise, parsley, green onions, lemon juice, Worcestershire sauce, salt, and black pepper together in a bowl until dressing is smooth. Pour dressing over chicken mixture; toss to coat. Refrigerate until chilled, at least 30 minutes. Stir the chicken mixture and serve over romaine lettuce leaves; garnish with avocado slices.'))

# Not matched and should be replaced with xxxxx
y = ((6, 'Tomato Chicken', 'chicken, tomato, garlic, ginger, chili, turmeric, avocado.', 'Combine the chicken, tomatoes, garlic, ginger, chili powder, turmeric, and salt in a large, heavy pot over high heat; cook and stir until the chicken begins to brown; reduce heat to medium-low and allow mixture to simmer until the chicken is no longer pink in the center and the juices run clear about 45 minutes. Sprinkle with coconut oil to serve.'), (7, 'Grilled Chicken Tomato salad', 'chicken, tomato, avocado, bacon, egg, cheese, bean.', 'Heat grill to medium-high heat. Brush chicken with oil; season with salt and pepper, to taste. Grill 8 to 12 minutes or until no longer pink in the center, turning once. Cool chicken enough to handle; slice into thin strips. Combine salad blend, tomatoes from the pouch, cooked sliced chicken, avocado, bacon, egg, and blue cheese in a large bowl. Toss with blue cheese dressing, to taste'), (8, 'Spicy Tomato Chicken', 'chicken, avocado, onion, ginger, cinnamon, cardamom, tomato,', 'Heat the oil in a large skillet over medium-high heat. Brown the chicken in the hot oil until golden on all sides. Remove the chicken from the skillet and set aside. Remove excess oil from the skillet, leaving about 1 tablespoon. Cook and stir the chili paste with the cinnamon, star anise, cloves, cardamom seeds until fragrant. Return the chicken to the skillet. Stir in the water, adding more if needed. Toss in the tomatoes and stir in the ketchup and sugar. Bring to a boil then reduce heat to medium-low and simmer until no the chicken longer pink at the bone and the juices run clear about 15 minutes.'), (9, 'Chicken Salad tomato', 'bacon, chicken, tomato, celery, lemon,  lettuce, avocado', 'Place bacon in a large skillet and cook over medium-high heat, turning occasionally, until evenly browned about 10 minutes. Drain bacon slices on paper towels; crumble. Stir chicken, bacon, tomato, and celery together in a bowl. Whisk mayonnaise, parsley, green onions, lemon juice, Worcestershire sauce, salt, and black pepper together in a bowl until dressing is smooth. Pour dressing over chicken mixture; toss to coat. Refrigerate until chilled, at least 30 minutes. Stir the chicken mixture and serve over romaine lettuce leaves; garnish with avocado slices.'), (10, 'Grilled Pesto Chicken Kabobs', 'sherry, pesto, chicken, mushroom, zucchini, onion,tomato', 'Whisk oil, sherry, pesto, lemon juice, salt, and pepper together in a glass bowl. Add chicken pieces and stir to coat. Cover and refrigerate for 4 hours to overnight. Preheat an outdoor grill for medium-high heat and lightly oil the grate. Thread marinated chicken, mushrooms, zucchini, red onion, and tomatoes alternately onto skewers. Reserve remaining marinade. Place kabobs onto the preheated grill, and cook, turning occasionally and brushing with the reserved marinade until chicken is cooked and juices run clear 10 to 15 minutes.'), (18, 'One Pot Spicy Eggs and Potatoe', 'onion, garlic, chicken, tomato, egg, potato, carrot.', 'Heat one tablespoon oil in a deep pot over medium heat. Add the onions and saute until very soft. Add the garlic, salt, two teaspoons of the ancho chili powder, vegetable broth, and tomatoes. Simmer for 10-15 minutes. Transfer to a blender and puree until smooth. In the same pot that the sauce was in, heat the remaining one tablespoon oil over medium heat. Add the potatoes and the remaining one teaspoon of ancho chili powder. Saute the potatoes for a few minutes until browned out the outside. Add the sauce back to the pot (be careful – it might splatter if it’s too hot) and simmer for another 10 minutes to cook the potatoes.'))

print(type(x))
print("--------------------")
print(x)
for i in x:
    print("------------------")
    print(i[2])
    print("------------------")


print(type(y))
print("--------------------")
print(y)
for i in y:
    print("------------------")
    print(i[2])
    print("------------------")
