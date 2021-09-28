def calc(sum_of_all, max_credit_hour):
    cwa = (sum_of_all / max_credit_hour)
    return cwa


def calc_full_cwa(ocwa, och, ncwa, nch):
    total_ch = och + nch
    full_marks_old = (ocwa*och)
    full_marks_new = (ncwa*nch)
    full_cwa = (full_marks_new + full_marks_old)/total_ch
    return full_cwa


def get_old_cwa():
    try:
        oldcwa = float(input("enter your old cwa: "))

    except ValueError:
        print("invalid input. enter a number...")
        return get_old_cwa()

    return oldcwa


def get_old_ch():
    try:
        oldch = int(input("enter your total previous credit hours: "))

    except ValueError:
        print("invalid input. enter a number...")
        return get_old_ch()

    return oldch


def get_number_of_courses():
    try:
        n_o_c = int(input("enter the number of courses you do? "))

    except ValueError:
        print("invalid input. enter a number...")
        return get_number_of_courses()

    return n_o_c


def get_marks():
    try:
        m_k = int(input("enter your scores: "))

    except ValueError:
        print("invalid input. enter a number...")
        return get_marks()

    return m_k


def get_credit_hours():
    try:
        c_h = int(input("enter the credit hours for this course: "))

    except ValueError:
        print("invalid input. enter a number...")
        return get_credit_hours()

    return c_h


def previous_cwa():
    choice = input("do you have a previous cwa? (y/n)\n").upper()
    if choice == 'Y':
        old_cwa = get_old_cwa()
        old_ch = get_old_ch()

        total = calc_full_cwa(old_cwa, old_ch, cwa, max_credit_hour)
        print(f"recent cwa = {cwa}")
        print(f'cumulative cwa = {total}')

    elif choice == 'N':
        print(f"cwa = {cwa}")
    else:
        print("invalid input. enter (y)es / (n)o...")
        return previous_cwa()


courses = {}
max_credit_hour = 0
sum_of_all = 0

number_of_courses = get_number_of_courses()


for num in range(number_of_courses):
    subject = input('enter the course name: ')
    marks = get_marks()
    credit_hours = get_credit_hours()

    max_credit_hour += credit_hours
    acc_marks = marks*credit_hours
    courses[subject] = acc_marks


sum_of_all = sum(courses.values())
cwa = calc(sum_of_all, max_credit_hour)


previous_cwa()


print(sum_of_all)
print(len(courses))

