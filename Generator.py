x = input('The Table Should Be of: ')
y = input('Till what number you want the table to be :')
for i in range(int(y) + 1):
  j = int(x) * int(i)
  print(x + ' x ' +  str(i) + ' = ' + str(j))
