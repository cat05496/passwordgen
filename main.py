import random
import string
import os


f = open('pass.txt', 'w')
f.close()


形容詞リスト = ['strong', 'happy', 'dry', 'wet', 'hungry', 'red', 'orange', 'yellow', 'green', 'blue', 'gray', 'big', 'white', 'kind', 'busy']

print('これからパスワードを生成します')

名詞リスト = ['apple', 'tiger', 'ball', 'desk', 'goat', 'dragon', 'piano', 'duck', 'panda']

print('これからパスワードを生成します')

形容詞 = random.choice(形容詞リスト)
名詞 = random.choice(名詞リスト)
数 = random.randrange(0, 100)
記号 = random.choice(string.punctuation)

パスワード = str(数) + str(数) + 名詞 + 記号 + 形容詞

f = open('pass.txt', 'w')
f.write(' %s' %パスワード)
f.close()

print('新しいパスワードは: %s' % パスワード)
print('このプログラムの階層にtxtファイルを生成しました。その中にパスワードが書いてあります')
