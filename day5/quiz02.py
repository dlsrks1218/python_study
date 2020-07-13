import random
from typing import List


def get_reward(dice_num: List[int]) -> int:
    """난수를 통해 상금을 계산
    >>> 3, 3, 3 -> 13000
    >>> 3, 3, 6 -> 1300
    >>> 3, 4, 5 -> 500

    Args:
        dice_num (List[int]): 1~6 사이 3개의 난수로 이루어진 리스트

    Returns:
        int: 계산된 상금
    """
    reward = 0
    dice_num_to_set = set(dice_num)
    if len(dice_num_to_set) == 1:
        reward = 10000 + list(dice_num_to_set)[0] * 1000
    elif len(dice_num_to_set) == 2:
        tmp = dice_num
        for num in dice_num_to_set:
            tmp.remove(num)
        reward = 1000 + tmp[0] * 100
    else:
        reward = max(dice_num_to_set) * 100

    return reward


def dice_game() -> None:
    """게임 결과를 난수 : {}, 상금 {} 형태로 출력
    """
    random_numbers = [random.randrange(1, 7) for _ in range(3)]
    print('난수 : {}, '.format(random_numbers), end='')
    reward = get_reward(random_numbers)
    print('상금 : {}'.format(reward))

if __name__ == '__main__':
    for i in range(10):
        print('{}번째 게임'.format(i+1), end=' - ')
        dice_game()

