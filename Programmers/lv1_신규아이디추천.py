def solution(new_id):
    arr = ['-', '.', '_']
    # 1. 소문자 만들기
    new_id = new_id.lower()

    # 2. 기호 제거
    for i in new_id:
        if i.isalpha() or i.isdigit() or i in arr:
            continue
        else:
            new_id = new_id.replace(i,'')


    # 3. 하나의 마침표(.) 만들기
    if '.' in new_id:
        for i in range(new_id.count('.'),1,-1):
            new_id = new_id.replace('.'*i, '.')

    # 4. 처음 or 끝 마침표(.) 제거
    new_id = new_id.strip('.')

    # 5. 빈 문자열은 'aaa'
    if new_id == '':
        new_id = 'aaa'

    # 6. 16자 이상이면 15자까지
    # 단, 양 끝의 마침표(.)는 제거
    elif len(new_id) >= 16:
        new_id = new_id[:15].strip('.')
    
    # 7. 2자 이하라면 마지막 문자를 추가하여 3자 만들기
    elif len(new_id) <= 2:
        new_id += new_id[-1]*(3-len(new_id))
    
    answer = new_id
    return answer


    # 조건문 정규식 정리해보기



def solution(new_id):
    arr = ['-', '.', '_']
    new_id = new_id.lower()

    for i in new_id:
        if i.isalpha() or i.isdigit() or i in arr:
            continue
        else:
            new_id = new_id.replace(i,'')

    if '.' in new_id:
        for i in range(new_id.count('.'),1,-1):
            new_id = new_id.replace('.'*i, '.')

    new_id = new_id.strip('.')

    # 중첩if문 대신에 정규식 한줄로 정리할 수도 있다
    # 두줄로 정리한 거 봤음
    new_id = 'aaa' if new_id == '' else new_id + new_id[-1]*(3-len(new_id)) if len(new_id) <= 2 else new_id[:15].strip('.')
    
    answer = new_id
    return answer