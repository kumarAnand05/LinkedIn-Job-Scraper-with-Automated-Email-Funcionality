def advanced_filter(job_description, maximum_months_of_experience):
    separated = job_description.split('\n')
    matching = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    collect = []
    for sentence in separated:
        if 'experience' in sentence.lower():
            for years in matching:
                if years in sentence:
                    if 'months' not in sentence:
                        collect.append(int(years)*12)
                    else:
                        collect.append(int(years))

    if len(collect) == 0 or min(collect) <= maximum_months_of_experience:
        return True
    else:
        return False




