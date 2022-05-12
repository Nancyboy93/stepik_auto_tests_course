def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
 assert substring in full_string, \
    f" expected '{substring}' to be substring of '{full_string}'"
full_string = 'fulltext, 1, some_text'
substring = 'some_value, 1, some'