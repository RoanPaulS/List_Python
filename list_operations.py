square = [1,2,3,4];
print(square);
print(square[0]);
square.append(0);
print(square);
square.append(121**2);
print(square);
print();
print();

# removing list elements

letter = ["a","b","c","d","e","f","g","a"];
print(letter);
print("Length is ",len(letter));
letter[2:5] = [];
print(letter);
print("Length is ",len(letter));
print();
print();


# finding length

alpha = ["a","b","c"];
num = [1,2,3];


both = alpha + num;
print("Both are : ",both);
print("Length is : ",len(both));
print();

both = [alpha , num];
print("Both are : ",both);
print("Length is : ",len(both));
print();

both = [alpha + num];
print("Both are : ",both);
print("Length is : ",len(both));
print();

