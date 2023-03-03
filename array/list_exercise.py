# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

expenses = [2200,2350,2600,2130,2190]

# 1. In Feb, how many dollars you spent extra compare to January?
#diff = expenses['febuary'] - expenses['january']
jan_feb_diff = expenses[1] - expenses[0]
print(jan_feb_diff)
# 2. Find out your total expense in first quarter (first three months) of the year.
total = 0
for month in expenses:
    total = total + month
print(total)
# 3. Find out if you spent exactly 2000 dollars in any month
for month in expenses:
    if 2000 in expenses:
        print(expenses.index(month))
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expenses.append(1980)
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
expenses[3] = expenses[3] - 200


# You have a list of your favourite marvel super heros.
heroes = ['spider man','thor','hulk','iron man','captain america']
# Using this find out,

# 1. Length of the list
print(len(heroes))
# 2. Add 'black panther' at the end of this list
heroes.append("black panther")
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
heroes.remove("black panther")
heroes.insert(3,"black panther")
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heroes[1:3] = ["doctor strange"]
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heroes.sort()
print(heroes)
#Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
max_num = input()
max_num = int(max_num)
odd_nums = [num for num in range(max_num) if num % 2 != 0]
print(odd_nums)