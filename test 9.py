Y = float(input("pls enter a length: "))
X = float(input("pls enter a girth: "))

Z = X * X * Y / 800

fish_list = ["mahi","whale shark"]
weight_list = ["77.516","47419.56"]

def determine_weight_class(weight):
 if weight <= 41:
        return "Small Fish"
 elif 42 <= weight <= 99:
        return "Medium Fish"
 elif 100 <= weight <= 174:
        return "Big Fish"
 else:
        return "Giant Fish"


weight_class = determine_weight_class(Z)

print(f"The calculated weight is: {Z} lbs")
print(f"The fish is classified as: {weight_class}")




