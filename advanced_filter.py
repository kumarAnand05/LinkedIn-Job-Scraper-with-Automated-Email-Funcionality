import re

def advanced_filter(job_description,maximum_months_of_experience):
    lines = job_description.split('\n')
    years = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    collected = []
    for sentence in lines:
        if 'experience' in sentence.lower():
            for y in years:
                pattern = r"\b" + re.escape(str(y)) + r"\b"
                match = re.search(pattern, sentence)
                if match:
                    if 'month' not in sentence.lower():
                        collected.append(int(match.group())*12)
                    else:
                        collected.append(int(match.group()))

        elif 'fresher' in sentence.lower() and maximum_months_of_experience<=12:
            return True
    if len(collected) == 0 or min(collected)<=maximum_months_of_experience:
        return True
    else:
        return False

