def calories(gender, kilos, heights, age, sports):
    if gender == 'f':
        return sports * (655 + 9.6 * kilos + 1.8 * heights - 4.7 * age)
    return sports * (66 + 13.7 * kilos + 5.0 * heights - 6.8 * age)