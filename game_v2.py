import numpy as np

def random_predict(number:int = None) -> int:
    """угадываем число

    Args:
        number (int, optional): загаданное число. Defaults to 1.

    Returns:
        int: чило попыток
    """
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1,101)
        if number == predict:
            break
    return(count)

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм


    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] 
    
    random_array = np.random.randint(1, 101, size=(10000)) 

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__':
    score_game(random_predict)



