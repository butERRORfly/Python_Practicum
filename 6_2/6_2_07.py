def need_to_work_better(journal):
    grades = journal[['maths', 'physics', 'computer science']]
    condition = (grades == 2).any(axis=1)

    return journal[condition].copy()