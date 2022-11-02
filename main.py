from deepface import DeepFace
import json


# Сравнивает лица
def face_verify(img_1, img_2):
    try:
        result_dict = DeepFace.verify(
            img1_path=img_1,
            img2_path=img_2,
        )
        with open('result.json', 'w') as file:
            json.dump(result_dict, file, indent=4, ensure_ascii=False)

        if result_dict.get('verified'):
            return 'Проверка пройдена. Пропустить.'
        return 'Нарушитель! Задержать!!!'

    except Exception as _ex:
        return _ex


# Распознавание лиц
def face_recogn():
    try:
        result = DeepFace.find(
            img_path='faces/7_Henry_Cavill.jpg',
            db_path='faces'
        )
        result.values.tolist()
        return result

    except Exception as _ex:
        return _ex


# Пол, возраст, национальность, эмоция
def face_analyze():
    try:
        result_dict = DeepFace.analyze(
            img_path='faces/i.jpg',
            actions=['age', 'gender', 'race', 'emotion']
        )
        with open('face_analyze.json', 'w') as file:
            json.dump(result_dict, file, indent=4, ensure_ascii=False)

        print(f'[+] Age: {result_dict.get("age")}')
        print(f'[+] Gender: {result_dict.get("gender")}')
        print('[+] Race:')

        for k, v in result_dict.get('race').items():
            print(f'{k} - {round(v, 2)}%')

        print('[+] Emotions:')

        for k, v in result_dict.get('emotion').items():
            print(f'{k} - {round(v, 2)}%')

    except Exception as _ex:
        return _ex


def main():
    # print(face_verify(
    #     img_1='faces/1_Yael_Shelbia.jpeg',
    #     img_2='faces/7_Henry_Cavill.jpg'
    #     )
    # )

    # print(face_recogn())

    face_analyze()


if __name__ == '__main__':
    main()
