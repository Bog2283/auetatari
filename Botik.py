

import time
import telebot

HEART = '🤍'
COLORED_HEARTS = ['💗', '💓', '💖', '💘', '❤️', '💞']
MAGIC_PHRASES = ['magic']
EDIT_DELAY = 0.01


stroka1 = '''
🤍
'''
stroka1_1 = '''
🤍🤍
'''
stroka1_2 = '''
🤍🤍🤍
'''
stroka1_3 = '''
🤍🤍🤍🤍
'''
stroka1_4 = '''
🤍🤍🤍🤍🤍
'''
stroka1_5 = '''
🤍🤍🤍🤍🤍🤍
'''
stroka1_6 = '''
🤍🤍🤍🤍🤍🤍🤍
'''
stroka1_7 = '''
🤍🤍🤍🤍🤍🤍🤍🤍
'''
stroka1_8 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍
'''
stroka1_9 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
'''
stroka1_0 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
'''

stroka2 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️
'''
stroka2_1 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍
'''
stroka2_2 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️
'''
stroka2_3 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️
'''
stroka2_4 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️
'''
stroka2_5 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍
'''
stroka2_6 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️
'''
stroka2_7 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️
'''
stroka2_8 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️
'''
stroka2_9 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍
'''
stroka2_0 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
'''

stroka3 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍
'''
stroka3_1 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️
'''
stroka3_2 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️
'''
stroka3_3 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️
'''
stroka3_4 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️
'''
stroka3_5 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️
'''
stroka3_6 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️
'''
stroka3_7 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️
'''
stroka3_8 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️
'''
stroka3_9 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️
'''
stroka3_0 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
'''

stroka4 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍
'''
stroka4_1 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️
'''
stroka4_2 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️
'''
stroka4_3 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️
'''
stroka4_4 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️
'''
stroka4_5 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️
'''
stroka4_6 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️
'''
stroka4_7 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️
'''
stroka4_8 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️
'''
stroka4_9 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️
'''
stroka4_0 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
'''

stroka5 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍
'''

stroka5_1 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️
'''

stroka5_2 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️
'''

stroka5_3 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️
'''

stroka5_4 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️
'''

stroka5_5 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️
'''

stroka5_6 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️
'''

stroka5_7 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️
'''

stroka5_8 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️
'''

stroka5_9 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️
'''

stroka5_0 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
'''

stroka6 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍
'''

stroka6_1 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️
'''

stroka6_2 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️
'''

stroka6_3 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️
'''

stroka6_4 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️
'''

stroka6_5 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️
'''

stroka6_6 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️
'''

stroka6_7 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️
'''

stroka6_8 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️
'''

stroka6_9 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍
'''

stroka6_0 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
'''

stroka7 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍
'''

stroka7_1 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍
'''

stroka7_2 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍
'''

stroka7_3 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️
'''

stroka7_4 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️
'''

stroka7_5 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️
'''

stroka7_6 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️
'''

stroka7_7 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️
'''

stroka7_8 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍
'''

stroka7_9 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍
'''

stroka7_0 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
'''

stroka8 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
🤍
'''

stroka8_1 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍️
'''

stroka8_2 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍️🤍
'''

stroka8_3 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍️🤍🤍
'''

stroka8_4 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍️🤍🤍❤️
'''

stroka8_5 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍️🤍🤍❤️❤️
'''

stroka8_6 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍️🤍🤍❤️❤️❤️
'''

stroka8_7 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍️🤍🤍❤️❤️❤️🤍
'''

stroka8_8 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍️🤍🤍❤️❤️❤️🤍🤍
'''

stroka8_9 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍️🤍🤍❤️❤️❤️🤍🤍🤍
'''

stroka8_0 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍️🤍🤍❤️❤️❤️🤍🤍🤍🤍
'''

stroka9 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍️🤍🤍❤️❤️❤️🤍🤍🤍🤍
🤍
'''

stroka9_1 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍️🤍🤍❤️❤️❤️🤍🤍🤍🤍
🤍🤍️
'''

stroka9_2 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍️🤍🤍❤️❤️❤️🤍🤍🤍🤍
🤍🤍️🤍
'''

stroka9_3 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍️🤍🤍❤️❤️❤️🤍🤍🤍🤍
🤍🤍️🤍🤍
'''

stroka9_4 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍️🤍🤍❤️❤️❤️🤍🤍🤍🤍
🤍🤍️🤍🤍🤍
'''

stroka9_5 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍️🤍🤍❤️❤️❤️🤍🤍🤍🤍
🤍🤍️🤍🤍🤍❤️
'''

stroka9_6 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍️🤍🤍❤️❤️❤️🤍🤍🤍🤍
🤍🤍️🤍🤍🤍❤️🤍
'''

stroka9_7 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍️🤍🤍❤️❤️❤️🤍🤍🤍🤍
🤍🤍️🤍🤍🤍❤️🤍🤍
'''

stroka9_8 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍️🤍🤍❤️❤️❤️🤍🤍🤍🤍
🤍🤍️🤍🤍🤍❤️🤍🤍🤍
'''

stroka9_9 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍️🤍🤍❤️❤️❤️🤍🤍🤍🤍
🤍🤍️🤍🤍🤍❤️🤍🤍🤍🤍
'''

stroka9_0 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍️🤍🤍❤️❤️❤️🤍🤍🤍🤍
🤍🤍️🤍🤍🤍❤️🤍🤍🤍🤍🤍
'''

stroka0 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍️🤍🤍❤️❤️❤️🤍🤍🤍🤍
🤍🤍️🤍🤍🤍❤️🤍🤍🤍🤍🤍
🤍
'''

stroka0_1 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍️🤍🤍❤️❤️❤️🤍🤍🤍🤍
🤍🤍️🤍🤍🤍❤️🤍🤍🤍🤍🤍
🤍🤍
'''

stroka0_2 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍️🤍🤍❤️❤️❤️🤍🤍🤍🤍
🤍🤍️🤍🤍🤍❤️🤍🤍🤍🤍🤍
🤍🤍🤍
'''

stroka0_3 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍️🤍🤍❤️❤️❤️🤍🤍🤍🤍
🤍🤍️🤍🤍🤍❤️🤍🤍🤍🤍🤍
🤍🤍🤍🤍
'''

stroka0_4 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍️🤍🤍❤️❤️❤️🤍🤍🤍🤍
🤍🤍️🤍🤍🤍❤️🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍
'''

stroka0_5 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍️🤍🤍❤️❤️❤️🤍🤍🤍🤍
🤍🤍️🤍🤍🤍❤️🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍
'''

stroka0_6 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍️🤍🤍❤️❤️❤️🤍🤍🤍🤍
🤍🤍️🤍🤍🤍❤️🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
'''

stroka0_7 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍️🤍🤍❤️❤️❤️🤍🤍🤍🤍
🤍🤍️🤍🤍🤍❤️🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍
'''

stroka0_8 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍️🤍🤍❤️❤️❤️🤍🤍🤍🤍
🤍🤍️🤍🤍🤍❤️🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
'''

stroka0_9 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍️🤍🤍❤️❤️❤️🤍🤍🤍🤍
🤍🤍️🤍🤍🤍❤️🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
'''

stroka0_0 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍❤️❤️❤️🤍❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍️❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍️🤍❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍️🤍🤍❤️❤️❤️🤍🤍🤍🤍
🤍🤍️🤍🤍🤍❤️🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
'''

stroka10 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍💘💘💘🤍💘💘💘🤍🤍
🤍💘💘💘💘💘💘💘💘💘🤍
🤍💘💘💘💘💘💘💘💘💘🤍
🤍💘💘💘💘💘💘💘💘💘🤍
🤍🤍️💘💘💘💘💘💘💘🤍🤍
🤍🤍️🤍💘💘💘💘💘🤍🤍🤍
🤍🤍️🤍🤍💘💘💘🤍🤍🤍🤍
🤍🤍️🤍🤍🤍💘🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
'''

stroka11 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍💖💖💖🤍💖💖💖🤍🤍
🤍💖💖💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖💖💖💖🤍
🤍🤍️💖💖💖💖💖💖💖🤍🤍
🤍🤍️🤍💖💖💖💖💖🤍🤍🤍
🤍🤍️🤍🤍💖💖💖🤍🤍🤍🤍
🤍🤍️🤍🤍🤍💖🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
'''

stroka12 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍💗💗💗🤍💗💗💗🤍🤍
🤍💗💗💗💗💗💗💗💗💗🤍
🤍💗💗💗💗💗💗💗💗💗🤍
🤍💗💗💗💗💗💗💗💗💗🤍
🤍🤍️💗💗💗💗💗💗💗🤍🤍
🤍🤍️🤍💗💗💗💗💗🤍🤍🤍
🤍🤍️🤍🤍💗💗💗🤍🤍🤍🤍
🤍🤍️🤍🤍🤍💗🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
'''

stroka13 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍💞💞💞🤍💞💞💞🤍🤍
🤍💞💞💞💞💞💞💞💞💞🤍
🤍💞💞💞💞💞💞💞💞💞🤍
🤍💞💞💞💞💞💞💞💞💞🤍
🤍🤍️💞💞💞💞💞💞💞🤍🤍
🤍🤍️🤍💞💞💞💞💞🤍🤍🤍
🤍🤍️🤍🤍💞💞💞🤍🤍🤍🤍
🤍🤍️🤍🤍🤍💞🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
'''

stroka14 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍💓💓💓🤍💓💓💓🤍🤍
🤍💓💓💓💓💓💓💓💓💓🤍
🤍💓💓💓💓💓💓💓💓💓🤍
🤍💓💓💓💓💓💓💓💓💓🤍
🤍🤍️💓💓💓💓💓💓💓🤍🤍
🤍🤍️🤍💓💓💓💓💓🤍🤍🤍
🤍🤍️🤍🤍💓💓💓🤍🤍🤍🤍
🤍🤍️🤍🤍🤍💓🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
'''



x = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍💓💓💓🤍💓💓💓🤍🤍
🤍💓💓💓💓💓💓💓💓💓🤍
🤍💓💓💓💓💓💓💓💓💓🤍
🤍💓💓💓💓💓💓💓💓💓🤍
🤍🤍️💓💓💓💓💓💓💓🤍🤍
🤍🤍️🤍💓💓💓💓💓🤍🤍🤍
🤍🤍️🤍🤍💓💓💓🤍🤍🤍🤍
🤍🤍️🤍🤍🤍💓🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
'''

x_1 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍💓💓💓🤍💓💓💓🤍🤍
🤍💓💓💓💓💓💓💓💓💓🤍
🤍💓💓💓💓💓💓💓💓💓🤍
🤍💓💓💓💓💓💓💓💓💓🤍
🤍🤍️💓💓💓💓💓💓💓🤍🤍
🤍🤍️🤍💓💓💓💓💓🤍🤍🤍
🤍🤍️🤍🤍💓💓💓🤍🤍🤍🤍
🤍🤍️🤍🤍🤍💓🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
'''
x_2 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍💓💓💓🤍💓💓💓🤍🤍
🤍💓💓💓💓💓💓💓💓💓🤍
🤍💓💓💓💓💓💓💓💓💓🤍
🤍💓💓💓💓💓💓💓💓💓🤍
🤍🤍️💓💓💓💓💓💓💓🤍🤍
🤍🤍️🤍💓💓💓💓💓🤍🤍🤍
🤍🤍️🤍🤍💓💓💓🤍🤍🤍🤍
🤍🤍️🤍🤍🤍💓🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
'''

x_3 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍💓💓💓🤍💓💓💓🤍🤍
🤍💓💓💓💓💓💓💓💓💓🤍
🤍💓💓💓💓💓💓💓💓💓🤍
🤍💓💓💓💓💓💓💓💓💓🤍
🤍🤍️💓💓💓💓💓💓💓🤍🤍
🤍🤍️🤍💓💓💓💓💓🤍🤍🤍
🤍🤍️🤍🤍💓💓💓🤍🤍🤍
🤍🤍️🤍🤍🤍💓🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍
'''
x_4 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍💓💓💓🤍💓💓💓🤍🤍
🤍💓💓💓💓💓💓💓💓💓🤍
🤍💓💓💓💓💓💓💓💓💓🤍
🤍💓💓💓💓💓💓💓💓💓🤍
🤍🤍️💓💓💓💓💓💓💓🤍🤍
🤍🤍️🤍💓💓💓💓💓🤍🤍
🤍🤍️🤍🤍💓💓💓🤍🤍
🤍🤍️🤍🤍🤍💓🤍🤍
🤍🤍🤍🤍🤍🤍🤍
'''
x_5 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍💓💓💓🤍💓💓💓🤍🤍
🤍💓💓💓💓💓💓💓💓💓🤍
🤍💓💓💓💓💓💓💓💓💓🤍
🤍💓💓💓💓💓💓💓💓💓🤍
🤍🤍️💓💓💓💓💓💓💓🤍
🤍🤍️🤍💓💓💓💓💓🤍
🤍🤍️🤍🤍💓💓💓🤍
🤍🤍️🤍🤍🤍💓🤍
🤍🤍🤍🤍🤍🤍
'''
x_6 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍💓💓💓🤍💓💓💓🤍🤍
🤍💓💓💓💓💓💓💓💓💓🤍
🤍💓💓💓💓💓💓💓💓💓🤍
🤍💓💓💓💓💓💓💓💓💓
🤍🤍️💓💓💓💓💓💓💓
🤍🤍️🤍💓💓💓💓💓
🤍🤍️🤍🤍💓💓💓
🤍🤍️🤍🤍🤍💓
🤍🤍🤍🤍🤍
'''
x_7 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍💓💓💓🤍💓💓💓🤍🤍
🤍💓💓💓💓💓💓💓💓💓🤍
🤍💓💓💓💓💓💓💓💓💓
🤍💓💓💓💓💓💓💓💓
🤍🤍️💓💓💓💓💓💓
🤍🤍️🤍💓💓💓💓
🤍🤍️🤍🤍💓💓
🤍🤍️🤍🤍🤍
🤍🤍🤍🤍
'''
x_8 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍💓💓💓🤍💓💓💓🤍🤍
🤍💓💓💓💓💓💓💓💓💓
🤍💓💓💓💓💓💓💓💓
🤍💓💓💓💓💓💓💓
🤍🤍️💓💓💓💓💓
🤍🤍️🤍💓💓💓
🤍🤍️🤍🤍💓
🤍🤍️🤍🤍
🤍🤍🤍
'''
x_9 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍💓💓💓🤍💓💓💓🤍
🤍💓💓💓💓💓💓💓💓
🤍💓💓💓💓💓💓💓
🤍💓💓💓💓💓💓
🤍🤍️💓💓💓💓
🤍🤍️🤍💓💓
🤍🤍️🤍🤍
🤍🤍️🤍
🤍🤍
'''
x_10 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍💓💓💓🤍💓💓💓
🤍💓💓💓💓💓💓💓
🤍💓💓💓💓💓💓
🤍💓💓💓💓💓
🤍🤍️💓💓💓
🤍🤍️🤍💓
🤍🤍️🤍
🤍🤍️
🤍
'''
x_11 = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍💓💓💓🤍💓💓
🤍💓💓💓💓💓💓
🤍💓💓💓💓💓
🤍💓💓💓💓
🤍🤍️💓💓
🤍🤍️🤍
🤍🤍️
🤍
'''
x_12 = '''
🤍🤍🤍🤍🤍🤍🤍🤍
🤍️🤍💓💓💓🤍💓
🤍💓💓💓💓💓
🤍💓💓💓💓
🤍💓💓💓
🤍🤍️💓
🤍🤍️
🤍
'''
x_13 = '''
🤍🤍🤍🤍🤍🤍🤍
🤍️🤍💓💓💓🤍
🤍💓💓💓💓
🤍💓💓💓
🤍💓💓
🤍🤍️
🤍
'''
x_14 = '''
🤍🤍🤍🤍🤍🤍
🤍️🤍💓💓💓
🤍💓💓💓
🤍💓💓
🤍💓
🤍
'''
x_15 = '''
🤍🤍🤍🤍🤍
🤍️🤍💓💓
🤍💓💓
🤍💓
🤍
'''
x_16 = '''
🤍🤍🤍🤍
🤍️🤍💓
🤍💓
🤍
'''
x_17 = '''
🤍🤍🤍
🤍️🤍
🤍
'''
x_18 = '''
🤍🤍
🤍️
'''
x_19 = '''
🤍
'''
x_20 = '''

'''


bot = telebot.TeleBot("6792765009:AAGXaxQHPv2zIuiqzZ5wUtgs8Q2-BIco2gA")




@bot.message_handler(commands=['start'])
def handle_magic_message(message):
    message1 = bot.send_message(message.chat.id, 'I')
    time.sleep(0.3)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text='I L')
    time.sleep(0.3)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text='I Lo')
    time.sleep(0.3)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text='I Lov')
    time.sleep(0.3)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text='I Love')
    time.sleep(0.3)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text='I Love Y')
    time.sleep(0.3)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text='I Love Yo')
    time.sleep(0.3)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text='I Love You')
    time.sleep(0.9)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text='Y')
    time.sleep(0.2)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text='Yo')
    time.sleep(0.2)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text='You')
    time.sleep(0.2)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text='You a')
    time.sleep(0.2)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text='You ar')
    time.sleep(0.2)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text='You are ')
    time.sleep(0.2)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text='You are B')
    time.sleep(0.2)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text='You are Be')
    time.sleep(0.2)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text='You are Bes')
    time.sleep(0.2)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text='You are Best')
    time.sleep(0.2)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text='You are Best o')
    time.sleep(0.2)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text='You are Best of')
    time.sleep(0.2)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text='You are Best of T')
    time.sleep(0.2)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text='You are Best of Th')
    time.sleep(0.2)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text='You are Best of The')
    time.sleep(0.2)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text='You are Best of The B')
    time.sleep(0.2)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text='You are Best of The Be')
    time.sleep(0.2)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text='You are Best of The Bes')
    time.sleep(0.2)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text='You are Best of The Best')
    time.sleep(0.2)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text='You are Best of The Best G')
    time.sleep(0.2)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text='You are Best of The Best Gi')
    time.sleep(0.2)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text='You are Best of The Best Gir')
    time.sleep(0.2)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text='You are Best of The Best Girl')
    time.sleep(1.6)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka1)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text=stroka1_1)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text=stroka1_2)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text=stroka1_3)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text=stroka1_4)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text=stroka1_5)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text=stroka1_6)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text=stroka1_7)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text=stroka1_8)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text=stroka1_9)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text=stroka1_0)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka2)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka2_1)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka2_2)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka2_3)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka2_4)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka2_5)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka2_6)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka2_7)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka2_8)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka2_9)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka2_0)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka3)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka3_1)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka3_2)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka3_3)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka3_4)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka3_5)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka3_6)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka3_7)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka3_8)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka3_9)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka3_0)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka4)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka4_1)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka4_2)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka4_3)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka4_4)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka4_5)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka4_6)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka4_7)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka4_8)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka4_9)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka4_0)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka5)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka5_1)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka5_2)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka5_3)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka5_4)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka5_5)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka5_6)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka5_7)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka5_8)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka5_9)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka5_0)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka6)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka6_1)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka6_2)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka6_3)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka6_4)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka6_5)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka6_6)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka6_7)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka6_8)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka6_9)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka6_0)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka7)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka7_1)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka7_2)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka7_3)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka7_4)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka7_5)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka7_6)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka7_7)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka7_8)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka7_9)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka7_0)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka8)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka8_1)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka8_2)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka8_3)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka8_4)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka8_5)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka8_6)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka8_7)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka8_8)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka8_9)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka8_0)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka9)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka9_1)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka9_2)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka9_3)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka9_4)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka9_5)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka9_6)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka9_7)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka9_8)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka9_9)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka9_0)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka0)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka0_1)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka0_2)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka0_3)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka0_4)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka0_5)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka0_6)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka0_7)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka0_8)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka0_9)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka0_0)
    time.sleep(0.7)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka10)
    time.sleep(0.7)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text= stroka11)
    time.sleep(0.7)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text=stroka12)
    time.sleep(0.7)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text=stroka13)
    time.sleep(0.7)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text=stroka14)
    time.sleep(0.7)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.id, text=stroka0_0)
    time.sleep(0.7)
    message2 = bot.send_message(message.chat.id, 'Э')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Эт')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Это')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Г')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Го')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год с')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год ст')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год ста')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал д')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал дл')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для м')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для ме')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для мен')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для меня')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для меня с')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для меня са')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для меня сам')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для меня самы')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для меня самым')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для меня самым л')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для меня самым лу')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для меня самым луч')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для меня самым лучш')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для меня самым лучши')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для меня самым лучшим')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для меня самым лучшим,')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для меня самым лучшим, л')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для меня самым лучшим, ли')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для меня самым лучшим, лиш')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для меня самым лучшим, лишь')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для меня самым лучшим, лишь б')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для меня самым лучшим, лишь бл')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для меня самым лучшим, лишь бла')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для меня самым лучшим, лишь благ')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для меня самым лучшим, лишь благо')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для меня самым лучшим, лишь благод')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для меня самым лучшим, лишь благода')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для меня самым лучшим, лишь благодар')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для меня самым лучшим, лишь благодаря')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для меня самым лучшим, лишь благодаря т')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для меня самым лучшим, лишь благодар те')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для меня самым лучшим, лишь благодар теб')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для меня самым лучшим, лишь благодаря тебе')
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Этот Год стал для меня самым лучшим, лишь благодаря тебе💘')
    time.sleep(1.5)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Я')
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Я т')
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Я те')
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Я теб')
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Я тебя')
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Я тебя о')
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Я тебя оч')
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Я тебя оче')
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Я тебя очен')
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Я тебя очень')
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Я тебя очень с')
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Я тебя очень си')
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Я тебя очень сил')
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Я тебя очень силь')
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Я тебя очень сильн')
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Я тебя очень сильно')
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Я тебя очень сильно л')
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Я тебя очень сильно лю')
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Я тебя очень сильно люб')
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Я тебя очень сильно любл')
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Я тебя очень сильно люблю')
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Я тебя очень сильно люблю, ')
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Я тебя очень сильно люблю, з')
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Я тебя очень сильно люблю, за')
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Я тебя очень сильно люблю, зай')
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Я тебя очень сильно люблю, зайк')
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Я тебя очень сильно люблю, зайка')
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Я тебя очень сильно люблю, зайка💘')
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Я тебя очень сильно люблю, зайка💘💘')
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text='Я тебя очень сильно люблю, зайка💘💘💘')
    time.sleep(1.5)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text=x)
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text=x_1)
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text=x_2)
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text=x_3)
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text=x_4)
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text=x_5)
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text=x_6)
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text=x_7)
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text=x_8)
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text=x_9)
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text=x_10)
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text=x_11)
    time.sleep(0.01)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text=x_12)
    time.sleep(0.02)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text=x_13)
    time.sleep(0.03)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text=x_14)
    time.sleep(0.05)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text=x_15)
    time.sleep(0.08)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text=x_16)
    time.sleep(0.13)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text=x_17)
    time.sleep(0.19)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text=x_18)
    time.sleep(0.3)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text=x_19)
    time.sleep(0.5)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message2.id, text=x_20)
    time.sleep(0.6)





bot.polling()
