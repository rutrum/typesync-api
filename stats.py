import string
import math

# Returns stats on the lyrics
# * Number of characters
# * Number of upper case letters
# * Number of punctuation marks
# * Number of digits
# * Number of whitespace characters
def get(lyrics):
    stats = {
        'total': 0,
        'upper': 0,
        'lower': 0,
        'digit': 0,
        'white': 0,
        'punc': 0,
    }

    for lyric in lyrics:
        # For end of line
        stats['total'] += 1
        stats['white'] += 1

        for char in lyric:
            stats['total'] += 1
            if char.isspace(): 
                stats['white'] += 1
                continue
            if char.isdigit(): 
                stats['digit'] += 1
                continue
            if char in string.punctuation: 
                stats['punc'] += 1
                continue
            if char.islower(): 
                stats['lower'] += 1
                continue
            if char.isupper(): 
                stats['upper'] += 1

    stats['total'] -= 1
    stats['white'] -= 1

    return stats

def determine_difficulty(stats):
    score = stats['lower'] \
          + stats['upper'] * 4 \
          + stats['digit'] * 4 \
          + stats['white'] \
          + stats['punc'] * 6

    ratings = ['Novice', 'Apprentice', 'Adept', 'Expert', 'Master']
    # thresh = [i * 1300 for i in range(5)]

    the_rating = ratings[min(math.floor(score/1300), 4)]
    return {
        "level": the_rating,
        "raw_level": score
    }
