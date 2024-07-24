'''
Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.

Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.

Please note that you are supposed to modify Person in place.
'''
import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # identify rows to keep: the first occurrence of each email
    idx_to_keep = person.sort_values(by="id").drop_duplicates(subset="email", keep="first").index

    # find all the indexes of the rows to drop
    idx_to_drop = person.index.difference(idx_to_keep)

    # drop the rows in-place
    person.drop(index=idx_to_drop, inplace=True)


data = {
    'id': [1,2,3,4,5],
    'email':['a@what.com', 'b@where.com', 'c@how.com', 'a@what.com', 'c@how.com']

}

df = pd.DataFrame(data)
delete_duplicate_emails(df)
print(df)
