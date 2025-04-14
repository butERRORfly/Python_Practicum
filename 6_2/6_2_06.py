def best(journal):
    journal = journal.copy()

    grades = journal[['maths', 'physics', 'computer science']]
    valid_grades = grades.applymap(lambda x: x in {4, 5})

    condition = (
            valid_grades.all(axis=1) &
            grades.notna().all(axis=1)
    )

    result = journal[condition].drop_duplicates(subset='name')

    return result
