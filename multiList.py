alpha = ["a","b","c"];
num = [1,2,3];

both = [alpha , num];
print("Both is : ",both);
print("Length is : ",len(both));
print(both[0]);
print(both[0][0]);
print();

print(both[1]);
print(both[1][0]);
print();


for inner_list in both:
   print(inner_list,end=" ");
print();


for inner_list in both:
    for list_item in inner_list:
        print(list_item,end=" ");
print();
