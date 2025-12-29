tp_digit_word = ( 'ศูนย์(soon)', 'หนึ่ง(neong) ' , 'สอง(song)', 'สาม(saam)' , 'สี่(see)', 'ห้า(haa)' , 'หก(hok)', 'เจ็ด(jed)' , 'แปด(paed)', 'เก้า(kaow)' )
digit = ( 'สิบ(sib)' , 'ร้อย(roi)' , 'พัน(pan)', 'หมื่น(meon)' , 'แสน(san)' , 'ล้าน(lann)' )

SPE = ('ยี่(yii)', 'เอ็ด(ed)')

def convert_2_digit(n):
    tens = n // 10
    ones = n % 10
    result = ''

    if tens > 1:
        if tens == 2:
            result += 'ยี่(yii)'
        
        else:
            result += tp_digit_word[tens]
        result += 'สิบ(sib)'
    elif tens == 1:
        result += 'สิบ(sib)'

    if ones == 1 and tens >= 1:
        result += 'เอ็ด(ed)'
    elif ones > 0 or (tens == 0 and ones == 0):
        result += tp_digit_word [ones]

    return result

def convert_number_to_thai (number):
    if number == 0:
        return tp_digit_word[0]
    result = ''
    segments = [ ]

    while number > 0:

        segments.append(number % 1000000)
        number //= 1000000

    for i in range(len(segments) - 1, -1, -1):
        segment = segments[i]
        if segment == 0:
            continue

        x = segment
        Hk = x // 100000; x %= 100000
        Tk = x // 10000; x %= 10000
        k= x //1000; x %= 1000
        h =x//100; x %= 100
        T = x // 10
        n = x % 10

        part = ''
        if Hk > 0:
            part += tp_digit_word[Hk] + 'แสน(san)'
    
        if Tk > 0:
            part += tp_digit_word[Tk] + 'หมื่น(meon)'

        if k > 0:
            part += tp_digit_word[k] + 'พัน(pan)'

        if h > 0:
            part += tp_digit_word[h] + 'ร้อย(roi)'

        if T > 0 or n > 0:
            part += convert_2_digit(T * 10 + n)

        result += part
        if i>0:
            result += 'ล้าน(lann)'

    return result

def arabic_to_thai_digits(number):
    tp_thai_digits = ('๐','๑','๒','๓','๔','๕','๖','๗','๘','๙')
    return ''.join(tp_thai_digits[int(d)] for d in str(number))

number = int(input("Enter Z+: "))

thai_word = convert_number_to_thai(number)
thai_digits = arabic_to_thai_digits(number)

print(f'Thai number: {thai_digits}')
print(f'Thai pronunciation: {thai_word}')
