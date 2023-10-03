#On the first line, you will receive a number n. On the following n lines, you will receive integers.
# You should create and print two lists:
#    • One with all the positives (including 0) numbers
#    • One with all the negatives numbers
#Finally, print the following message:
#"Count of positives: {count_positives}
#Sum of negatives: {sum_of_negatives}"

n = int(input())
positive_number = []
negative_number = []
count_of_positive_number = 0
sum_of_negative_number = 0
for i in range(n):
    number = int(input())
    if number >=0 :
        positive_number.append(number)
        count_of_positive_number += 1
    else:
        negative_number.append(number)
        sum_of_negative_number += number
print(positive_number)
print(negative_number)
print(f'Count of positives: {count_of_positive_number}')
print(f'Sum of negatives: {sum_of_negative_number}')
