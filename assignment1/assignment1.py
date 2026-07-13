# Task 1
def hello():
    return "Hello!"
 
 
# Task 2
def greet(name):
    return f"Hello, {name}!"
 
 
# Task 3
def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
 
 
# Task 4
def data_type_conversion(value, data_type):
    try:
        if data_type == "float":
            return float(value)
        elif data_type == "int":
            return int(value)
        elif data_type == "str":
            return str(value)
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {data_type}."
 
 
# Task 5
def grade(*args):
    try:
        average = sum(args) / len(args)
    except (TypeError, ZeroDivisionError):
        return "Invalid data was provided."
 
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
 
 
# Task 6
def repeat(string, count):
    result = ""
    for _ in range(count):
        result += string
    return result
 
 
# Task 7
def student_scores(mode, **kwargs):
    if mode == "best":
        best_name = None
        best_score = None
        for name, score in kwargs.items():
            if best_score is None or score > best_score:
                best_score = score
                best_name = name
        return best_name
    elif mode == "mean":
        return sum(kwargs.values()) / len(kwargs)
 
 
# Task 8
def titleize(string):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = string.split()
    result = []
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            result.append(word.capitalize())
        elif word in little_words:
            result.append(word)
        else:
            result.append(word.capitalize())
    return " ".join(result)
 
 
# Task 9
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result
 
 
# Task 10
def pig_latin(text):
    vowels = "aeiou"
    words = text.split()
    result = []
    for word in words:
        if word[0] in vowels:
            result.append(word + "ay")
        else:
            i = 0
            while i < len(word) and word[i] not in vowels:
                if word[i] == "q" and i + 1 < len(word) and word[i + 1] == "u":
                    i += 2
                    break
                i += 1
            result.append(word[i:] + word[:i] + "ay")
    return " ".join(result)
 