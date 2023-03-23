def role():
    job_role = input('Enter the Job role: ')
    return job_role.strip()


def geo():
    job_location = input('Enter your Job location: ')
    return job_location.strip()


def listing_time():
    print('\nChoose the time of Job posting from options below')
    time_list = {'1': 'Past 24 hours', '2': 'Past week', '3': 'Past month', '4': 'Any time'}
    for t in time_list:
        print(f'{t}:{time_list[t]}')
    job_post_time = input('Enter number to select the time of Job posting: ').strip()
    if int(job_post_time) in range(1, 5):
        return time_list[job_post_time]
    else:
        return time_list[4]


def job_level():
    desired_exp_level = []
    print('\nChoose experience level from the list below')
    level_list = {'1': 'Internship',
                  '2': 'Entry level',
                  '3': 'Associate',
                  '4': 'Mid-senior level',
                  '5': 'Director',
                  '6': 'Executive',
                  '7': 'Not applicable'}

    for n in level_list:
        print(f'{n}:{level_list[n]}')
    ex_input = input('Enter space separated number to select: ').strip().split(' ')

    if len(ex_input) != 0:
        for x in ex_input:
            if int(x) in range(1, 8):
                desired_exp_level.append(level_list[x])
        return desired_exp_level

    else:
        print('Invalid Input. No Experience level filter applied')
        return [level_list[val] for val in level_list]


def list_length():
    limit = input('\nEnter max number of Job Listings you want: ')
    if int(limit) != 0:
        return limit
    else:
        print('Invalid Input. Run the script again')


def filtering():
    check = input('\nTurn on Advanced filtering (Y/N)? This will make process slower and output more relevant.\n')
    if check.lower() == 'y':
        return True
    else:
        return False


def internet_speed():
    pause = input('Is your internet connection slow? (Y/N)').lower()
    if pause == 'y':
        return 2
    else:
        return 1
