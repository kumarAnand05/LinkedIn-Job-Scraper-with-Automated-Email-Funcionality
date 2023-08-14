def role():
    job_role = input('Enter the Job role (eg. Data Analyst): ')
    if len(job_role)!=0:
        return job_role.strip()
    else:
        print('No Job Role Entered. Run the script again')
        exit()


def geo():
    job_location = input('Enter your Job location: ')
    if len(job_location)!=0:
        return job_location.strip()
    else:
        print('No Job Location provided. Run the script again')
        exit()


def listing_time():
    print('\nChoose the time of Job posting from options below')
    time_list = {'1': 'Past 24 hours', '2': 'Past week', '3': 'Past month', '4': 'Any time'}
    for t in time_list:
        print(f'{t}:{time_list[t]}')
    job_post_time = input('Enter number to select the time of Job posting: ').strip()
    try:
        if int(job_post_time) in range(1, 5):
            return time_list[job_post_time]
        else:
            print("Invalid Input. Choosing default listing time, 'Any Time'.")
            return time_list['4']
    except ValueError:
        print("Invalid Input. Choosing default listing time, 'Any Time'.")
        return time_list['4']


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

    if len(ex_input) == 0:
        print('Invalid Input. No Experience level filter applied')
        return [level_list[val] for val in level_list]
    else:
        for x in ex_input:
            try:
                if int(x) in range(1, 8):
                    desired_exp_level.append(level_list[x])
            except ValueError:
                pass
        if len(desired_exp_level)!=0:
            return desired_exp_level
        else:
            print('Invalid Input. No Experience level filter applied')
            return [level_list[val] for val in level_list]


def list_length():
    limit = input('\nEnter max number of Job Listings you want (eg. 50): ').strip()
    try:
        if int(limit) > 0:
            return limit
        else:
            print('Invalid Input. Run the script again')
            exit()
    except ValueError:
        print('Invalid Input. Run the script again')
        exit()



def filtering():
    check = input('\nTurn on Advanced filtering (Y/N)? This will make process slower and output more relevant.\n')
    if check.lower() == 'y':
        return True
    else:
        return False


def internet_speed():
    pause = input('Is your internet connection slow? (Y/N)\n').lower()
    print('\n\nPlease Wait. Scraper is starting...')
    if pause == 'y':
        return 2        # This value multiplies the pause time by this much value (Increase this value if internet is too slow, this can decrease scraping speed)
    else:
        return 1        # Normal pause time, in case the internet speed is fast
