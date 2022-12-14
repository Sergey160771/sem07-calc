import re
import const

def validate_num(pattern, num):
    if re.fullmatch(pattern, num):
        return True
    return False

print(validate_num(const.RATIONAL_PATTERN, '-42/88'))
print(validate_num(const.RATIONAL_PATTERN, '-4.2/+88'))
print(validate_num(const.COMPLEX_PATTERN, '3 + 10j'))
print(validate_num(const.COMPLEX_PATTERN, '-3.2-223.231j'))
print(validate_num(const.OPERATOR_PATTERN, '/'))
print(validate_num(const.OPERATOR_PATTERN, '+-'))