def update(journal):
    journal = journal.copy()

    journal['average'] = journal[['maths', 'physics', 'computer science']].mean(axis=1)

    journal = journal.sort_values(
        by=['average', 'name'],
        ascending=[False, True]
    )

    return journal
