from calculate_calories.models import Food


def calories(gender, kilos, heights, age, sports):
    if gender == 'f':
        return sports * (655 + 9.6 * kilos + 1.8 * heights - 4.7 * age)
    return sports * (66 + 13.7 * kilos + 5.0 * heights - 6.8 * age)


def can_combine_with(food1_type, food2_type):
    if food1_type == food2_type:
        return True
    if food1_type == 'fruit' and food2_type == 'dairy':
        return True
    if food1_type == 'fruit' and food2_type == 'grain':
        return True
    if food1_type == 'vegetable' and food2_type == 'grain':
        return True
    if food1_type == 'vegetable' and food2_type == 'protein':
        return True
    if food1_type == 'vegetable' and food2_type == 'dairy':
        return True
    if food1_type == 'grain' and food2_type == 'protein':
        return True
    if food1_type == 'grain' and food2_type == 'dairy':
        return True
    else:
        return False


def calculate_calories(calories_in_100gr, amount):
    return calories_in_100gr / 100 * amount


def can_combine(food_amount, food_calories, calories_left):
    if calories_left < 100 or food_amount < 100:
        return False
    else:
        return True


def combine(food1_type, calories_food1,
            amount_food1, food2_type,
            calories_food2, amount_food2, calories_left):
    if can_combine_with(food1_type, food2_type) or can_combine_with(food2_type, food1_type):
        if amount_food1 < 100 and amount_food2 < 100:
            return []
        else:
            if calculate_calories(calories_food1, amount_food1) <= calories_left:
                calories_left -= calculate_calories(calories_food1,
                                                    amount_food1)
                if calculate_calories(calories_food2,
                                      amount_food2) <= calories_left:
                    return [food1_type, amount_food1, food2_type, amount_food2]
                elif calories_left > 100:
                    return [food1_type, amount_food1,
                            food2_type, calories_left / calories_food2]
                else:
                    return [food1_type, amount_food1]
            else:
                return []
    else:
        if calculate_calories(calories_food1, amount_food1) <= calories_left:
            return [(food1_type, amount_food1)]
        elif calculate_calories(calories_food2, amount_food2) <= calories_left:
            return [(food2_type, amount_food2)]
        else:
            return []


def get_2_combinations(food1_type, calories_food1,
                       amount_food1, food2_type, calories_food2,
                       amount_food2, calories_left):
    combinations = []
    if can_combine(amount_food1, calories_food1, calories_left):
        while (combine(food1_type, calories_food1, amount_food1, food2_type,
                       calories_food2, amount_food2, calories_left) == [] and
               amount_food1 > 100):
            amount_food1 -= 100
        combinations.append(combine(food1_type, calories_food1,
                                    amount_food1, food2_type,
                                    calories_food2, amount_food2,
                                    calories_left))
    if can_combine(amount_food2, calories_food2, calories_left):
        while (combine(food2_type, calories_food2, amount_food2,
                       food1_type, calories_food1, amount_food1,
                       calories_left) == [] and amount_food2 > 100):
            amount_food2 -= 100
        combinations.append(combine(food2_type, calories_food2, amount_food2,
                                    food1_type, calories_food1, amount_food1,
                                    calories_left))
    return combinations


def add_food_in_db():
    pass
#     food1 = Food("yogurt", "dairy", 63)
#     food1.save()
#     food2 = Food("tomato", "vegetable", 12)
#     food2.save()
#     food3 = Food("apple", "fruit", 30)
#     food3.save()
#     food4 = Food("baked chicken", "protein", 100)
#     food4.save()
#     food5 = Food("cheese", "dairy", 100)