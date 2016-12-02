import csv

print "start"
enrollments_filename = 'E:\udacity\data analyst\lesson2\enrollments.csv'
engagement_filename = 'E:\udacity\data analyst\lesson2\daily_engagement.csv'
submissions_filename = 'E:\udacity\data analyst\lesson2\project_submissions.csv'

# enrollments=[]
# f=open (enrollments_filename, 'rb')
# reader=csv.DictReader(f)
#
# for row in reader:
#     enrollments.append(row)
#
# f.close()
# print enrollments[0:2]

## Longer version of code (replaced with shorter, equivalent version below)

# enrollments = []
# f = open(enrollments_filename, 'rb')
# reader = unicodecsv.DictReader(f)
# for row in reader:
#     enrollments.append(row)
# f.close()


### Write code similar to the above to load the engagement
### and submission data. The data is stored in files with
### the given filenames. Then print the first row of each
### table to make sure that your code works. You can use the
### "Test Run" button to see the output of your code.
def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = csv.DictReader(f)
        return list(reader)

enrollments = read_csv(enrollments_filename)
daily_engagement = read_csv(engagement_filename)
project_submissions = read_csv(submissions_filename)



### For each of these three tables, find the number of rows in the table and
### the number of unique students in the table. To find the number of unique
### students, you might want to create a set of the account keys in each table.

# rename acct to account_key as same as other files
for line in daily_engagement:
    line['account_key']=line['acct']
    del[line['acct']]
# enrollment_num_rows = len(enrollments)            # Replace this with your code
# print enrollment_num_rows
#
# enrollment_num_unique_students = set()  # Replace this with your code
# for line in enrollments:
#     enrollment_num_unique_students.add(line['account_key'])
# print len(enrollment_num_unique_students)
#
#
# engagement_num_rows = 0             # Replace this with your code
# engagement_num_unique_students = 0  # Replace this with your code
#
# submission_num_rows = 0             # Replace this with your code
# submission_num_unique_students = 0  # Replace this with your code
def unique_student(data):
    unique=set()
    for line in data:
        unique.add(line['account_key'])
    return unique
def number_unique_student(filename):
    print "number of data: "+str(len(filename))
    print "number of unique students: "+str(len(unique_student(filename)))

number_unique_student(enrollments)
number_unique_student(daily_engagement)
number_unique_student(project_submissions)

#call file [data_line] [column]
#print daily_engagement[0]['utc_date']

#Identify surprising data points
#find enrollment record with no corresponding engagement data
#print unique_student(enrollments)
surprising_data =[]
for line in enrollments:
    student = line['account_key']
    if student not in unique_student(daily_engagement):
#        print line
#        break
        surprising_data.append(line)
print "number different :"+str(len(surprising_data))
#print surprising_data

# we see student join and cancel at the same days
# try to find other surprising point
# clear the same day student data
# #print surprising_data
# num_problem_students = 0
# for enrollment in enrollments:
#     student = enrollment['account_key']
#     if (student not in unique_engagement_students and
#             enrollment['join_date'] != enrollment['cancel_date']):
#         print enrollment
#         num_problem_students += 1
#
# num_problem_students

num_problem_students=0

for line in surprising_data:
    join = line['join_date']

    quit = line['cancel_date']
    if join !=quit:
        print line
        num_problem_students +=1
print "numbers of problem student "+str(num_problem_students)

#remove udacity accounts
udacity_test_accounts=set()
for line in enrollments:
    if line['is_udacity']=="True":
        udacity_test_accounts.add(line['account_key'])
print "is udacity account:"
print len(udacity_test_accounts)
def remove_udacity_accounts(data):
    non_udacity_data=[]
    for line in data:
        if line['account_key'] not in udacity_test_accounts:
            non_udacity_data.append(line)
    return non_udacity_data

non_udacity_enrollments = remove_udacity_accounts(enrollments)
non_udacity_engagement = remove_udacity_accounts(daily_engagement)
non_udacity_submissions = remove_udacity_accounts(project_submissions)

paid_students={}
for line in non_udacity_enrollments:
    if (line['is_canceled']=="False" or int(line['days_to_cancel']) > 7):
        account_key=line['account_key']
        enrollment_data=line['join_date']
        if (account_key not in paid_students or enrollment_data>paid_students[account_key]):
            paid_students[account_key]=enrollment_data
print "number of student paid"
print len(paid_students)


def within_one_week(join_date, engagement_date):
    time_delta = engagement_date - join_data
    return time_delta.days < 7

def remove_free_trial_cancels(data):
    new_data = []
    for data_point in data:
        if data_point['account_key'] in paid_students:
            new_data.append(data_point)
    return new_data

paid_enrollments = remove_free_trial_cancels(non_udacity_enrollments)
paid_engagement = remove_free_trial_cancels(non_udacity_engagement)
paid_submissions = remove_free_trial_cancels(non_udacity_submissions)

paid_engagement_in_first_week =






print "end"
