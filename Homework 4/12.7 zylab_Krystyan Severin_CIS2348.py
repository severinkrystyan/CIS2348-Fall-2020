"""Name: Krystyan Severin
   PSID: 1916594"""


def get_age():
    age = int(input())
    if age < 18 or age > 75:
        raise ValueError
    return age


def fat_burning_heart_rate(age):
    # Fat Burning Heart Rate Formula
    bpm = ((70/100) * (220 - age))
    return bpm


if __name__ == '__main__':
    try:
        person_age = get_age()
        heart_rate = fat_burning_heart_rate(person_age)
    except ValueError:
        print('Invalid age.')
        print('Could not calculate heart rate info.\n')
    else:
        print(f'Fat burning heart rate for a {person_age} year-old: {heart_rate:.1f} bpm')
