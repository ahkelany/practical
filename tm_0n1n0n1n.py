def tm_accepts_0n1n0n1n(s: str) -> bool:
    if not s:
        return True  # حالة n=0 مقبولة (السلسلة الفارغة)

    parts = []
    i = 0
    # تقسيم السلسلة إلى أجزاء من الحروف المتتالية وعددها
    while i < len(s):
        current_char = s[i]
        count = 0
        # لا حاجة لـ start_of_part_index هنا لأننا لا نستخدمه
        while i < len(s) and s[i] == current_char:
            count += 1
            i += 1
        # تأكد من أن الحرف هو '0' أو '1' فقط (إذا كانت اللغة تقتصر على هذه الرموز)
        if current_char not in ['0', '1']:
            return False # حرف غير مسموح به في اللغة
        parts.append((current_char, count))

    # 1. التأكد من أن هناك بالضبط 4 أجزاء
    if len(parts) != 4:
        return False

    # 2. استخراج الرموز والأعداد
    symbols = [p[0] for p in parts]
    counts = [p[1] for p in parts]

    # 3. التأكد من أن تسلسل الرموز هو '0', '1', '0', '1'
    if symbols != ['0', '1', '0', '1']:
        return False

    # 4. التأكد من أن جميع الأعداد (n) متساوية
    # إذا كانت جميع الأعداد متساوية، فإن المجموعة set(counts) ستحتوي على عنصر واحد فقط.
    if len(set(counts)) != 1:
        return False
    
    # إذا وصلت إلى هنا، فكل الشروط متحققة
    return True


def main():
    test_cases = [
        ("00110011", True),          # صحيح، n=2
        ("000111000111", True),      # صحيح، n=3
        ("01010101", False),         # ليس 0^n 1^n 0^n 1^n (هذا (01)^4)
        ("001101", False),           # لا يتبع النمط (الجزء الأخير قصير)
        ("0000111100001111", True),  # صحيح، n=4
        ("", True),                  # صحيح، n=0
        ("01", False),               # ناقص أجزاء
        ("0001110001111", False),    # الجزء الأخير أطول من اللازم
        ("000011110000111", False),  # الجزء الأخير أقصر
        ("0101", True)               # صحيح، n=1
    ]

    # إضافة حالات اختبار أخرى مهمة:
    test_cases.extend([
        ("0", False),                # جزء واحد فقط
        ("1", False),                # جزء واحد فقط
        ("00", False),               # جزء واحد فقط
        ("11", False),               # جزء واحد فقط
        ("010", False),              # ثلاثة أجزاء فقط
        ("1010", False),             # يبدأ بـ '1'
        ("001110011", False),        # عدد '1' في المنتصف مختلف (ليس n)
        ("0001100011", False),       # عدد '0' و '1' مختلف
        ("abc", False),              # حروف غير مسموح بها
        ("01a01", False),            # حرف غير مسموح به في المنتصف
        ("001100110", False),        # جزء خامس زائد
    ])

    all_passed = True
    for s, expected in test_cases:
        result = tm_accepts_0n1n0n1n(s)
        print(f"Test on '{s}': Expected {expected}, Got {result}")
        if result != expected:
            print(f"    ^^^^^ FAILED for input '{s}' ^^^^^")
            all_passed = False
    
    if all_passed:
        print("\nAll tests passed successfully!")
    else:
        print("\nSome tests FAILED.")


if __name__ == "__main__":
    main()