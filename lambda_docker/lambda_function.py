# sweetsoup_bot.py
# renamed as lambda_function.py for running
from logic import juk_hak_menu, juk_kyo_menu, juk_sang_menu, chn_kyo_menu, chn_hak_menu, chn_danhol_menu


keyboard_button = {
    "keyboard": {
        "type": "buttons",
        "buttons": [
            "죽전 교직원식당",
            "죽전 학생식당",
            "죽전 생활관식당",
            "천안 교직원식당",
            "천안 학생식당",
            "천안 단우홀기숙사식당",
            "MS오피스 설치",
            "도움말"
        ]
    }
}


def lambda_handler(event, context):
    data = event
    content = data.get('content')

    if content == "죽전 교직원식당":
        result_menu = juk_kyo_menu()
        data_send = {
            "message": {
                "text": f"죽전, 오늘의 학식\n {result_menu}"
            }
        }
        result = dict(data_send, **keyboard_button)
        return result

    elif content == "죽전 학생식당":
        result_menu = juk_hak_menu()
        data_send = {
            "message": {
                "text": f"천안, 오늘의 학식\n {result_menu}"
            }
        }
        result = dict(data_send, **keyboard_button)
        return result

    elif content == "죽전 생활관식당":
        result_menu = juk_sang_menu()
        data_send = {
            "message": {
                "text": f"천안, 오늘의 학식\n {result_menu}"
            }
        }
        result = dict(data_send, **keyboard_button)
        return result

    elif content == "천안 교직원식당":
        result_menu = chn_kyo_menu()
        data_send = {
            "message": {
                "text": f"천안, 오늘의 학식\n {result_menu}"
            }
        }
        result = dict(data_send, **keyboard_button)
        return result

    elif content == "천안 학생식당":
        result_menu = chn_hak_menu()
        data_send = {
            "message": {
                "text": f"천안, 오늘의 학식\n {result_menu}"
            }
        }
        result = dict(data_send, **keyboard_button)
        return result

    elif content == "천안 단우홀기숙사식당":
        result_menu = chn_danhol_menu()
        data_send = {
            "message": {
                "text": f"천안, 오늘의 학식\n {result_menu}"
            }
        }
        result = dict(data_send, **keyboard_button)
        return result

    elif content == "MS오피스 설치":
        pc_link = 'http://cms.dankook.ac.kr/web/office'
        ios_link = 'https://itunes.apple.com/kr/developer/microsoft-corporation/id298856275'
        and_link = 'https://play.google.com/store/apps/dev?id=6720847872553662727'
        data_send = {
            "message": {
                "text": "Office365 설치를 위해, 단국대 학교 이메일과 패스워드를 알고 있어야 합니다!\n"
                        "최초로 부여받은 비밀번호(생년월일)의 경우 로그인이 불가하여\n"
                        "꼭! 비밀번호 변경 후 이용해주시길 바랍니다.\n"
                        "\n-PC설치방법-\n"
                        f"사이트: {pc_link}\n"
                        "오피스 포털 접속 -> Office364 포털 클릭 -> Office앱 설치\n\n"
                        f"Android - {and_link}\n\n"
                        f"iOS - {ios_link}"
            }
        }
        result = dict(data_send, **keyboard_button)
        return result

    elif content == "도움말":
        data_send = {
            "message": {
                "text": "피드백 보내기\n"
                        "E-mail : roamgom@gmail.com\n"
                        "SweetSoup(중고서적) : URL"
            }
        }
        result = dict(data_send, **keyboard_button)
        return result
    else:
        return keyboard_button['keyboard']


if __name__ == '__main__':
    print("Testing...")
    juk_hak_menu()
    juk_kyo_menu()
    juk_sang_menu()
    chn_kyo_menu()
    chn_hak_menu()
    chn_danhol_menu()