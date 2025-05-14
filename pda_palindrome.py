def is_odd_palindrome(string: str) -> bool:
    # التأكد من أن طول السلسلة فردي
    if len(string) % 2 == 0:
        return False  

    # استخدام مكدس للمقارنة من الجانبين
    stack = []
    mid = len(string) // 2

    # إضافة الأحرف قبل المنتصف إلى المكدس
    for i in range(mid):
        stack.append(string[i])

    # مقارنة الأحرف بعد المنتصف مع العناصر الموجودة في المكدس
    for i in range(mid + 1, len(string)):
        if not stack or string[i] != stack.pop():
            return False

    # إذا تم استهلاك جميع العناصر في المكدس، تكون السلسلة هي باليندروم
    return not stack 

def main():
    test_cases = [
        "aba",     # True
        "abba",    # False
        "abcba",   # True
        "a",       # True
        "abcda",   # False
    ]
    # اختبار السلسلة وطباعة النتيجة
    for test in test_cases:
        result = is_odd_palindrome(test)
        print(f"{test} → {result}")

if __name__ == "__main__":
    main()
