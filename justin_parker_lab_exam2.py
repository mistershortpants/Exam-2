grade = 0.0

def main():
    try:
        user_name = input('Enter your username: ')
        grade_1 = float(input('Enter the First test grade: '))
        grade_2 = float(input('Enter the Second test grade: '))
        grade_3 = float(input('Enter the Third test grade: '))
        average = calc_average(grade_1, grade_2, grade_3)
        letter_grade = determine_grade(grade)
        display_results(user_name, grade_1, grade_2, grade_3, average, letter_grade)
        write_results(user_name, grade_1, grade_2, grade_3, average, letter_grade)
        append_even()
        read_result()
    except ValueError:
        print('Please enter a valid number.')



def calc_average(grade_1, grade_2, grade_3):
    return (grade_1 + grade_2 + grade_3) / 3

def determine_grade(value):
    if value >= 90:
        grade = 'A'
    elif value >= 80:
        grade = 'B'
    elif value >= 70:
        grade = 'C'
    elif value >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade

def display_results(user_name, grd_1, grd_2, grd_3, grd_average, letter_grade):
    print('Displaying results....\n')
    print('Your username is ', user_name)
    print('First grade is ', f'{grd_1:,.2f}', sep='')
    print('Second grade is ', f'{grd_2:,.2f}', sep='')
    print('Third grade is ', f'{grd_3:,.2f}', sep='')
    print('The average of the three grades is ', f'{grd_average:,.2f}', sep='')
    print('Your letter grade is ', letter_grade, sep='')
    print('-----------------------------------------\n\n')

def write_results(user, g1, g2, g3, g_avg, lett_grade):
    outfile = open('grades.txt', 'w')
    outfile.write(user + '\n')
    outfile.write('First grade is ' + str(g1) + '\n')
    outfile.write('Second grade is ' + str(g2) + '\n')
    outfile.write('Third grade is ' + str(g3) + '\n')
    outfile.write('The average of the three grades is ' + str(g_avg) + '\n')
    outfile.write('The letter grade is ' + str(lett_grade) + '\n')
    outfile.close()

def append_even():
    outfile = open('grades.txt', 'a')
    outfile.write('I am going to display the even numbers between 1 and 50 \n')
    for number in range(1, 51):
        if number % 2 == 0:
            outfile.write(str(number) + '\n')
    outfile.close()

def read_result():
    outfile = open('grades.txt', 'r')
    contents = outfile.read()
    print(contents)
    outfile.close()

main()
