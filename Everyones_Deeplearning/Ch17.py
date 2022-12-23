# %%
from keras.preprocessing.text import text_to_word_sequence
 
# 전처리할 텍스트를 정합니다.
text = '해보지 않으면 해낼 수 없다'
# %%
result = text_to_word_sequence(text)
print("\n원문:\n", text)
print("\n토큰화:\n", result)

# %%
from keras.preprocessing.text import Tokenizer
docs = ['먼저 텍스트의 각 단어를 나누어 토큰화합니다.',
        '텍스트의 단어로 토큰화해야 딥러닝에서 인식됩니다.',
        '토큰화한 결과는 딥러닝에서 사용할 수 있습니다.',
       ]
# %%
token = Tokenizer()      # 토큰화 함수 지정
token.fit_on_texts(docs) # 토큰화 함수에 문장 적용

print("\n단어 카운트:\n", token.word_counts) # 단어의 빈도수를 계산한 결과 출력

print("\n문장 카운트: ", token.document_count)  # 문장의 개수를 출력

print("\n각 단어가 몇 개의 문장에 포함되어 있는가:\n", token.word_docs)

print("\n각 단어에 매겨진 인덱스 값:\n", token.word_index)
# %%
text = "오랫동안 꿈꾸는 이는 그 꿈을 닮아간다"

token=Tokenizer()
token.fit_on_texts([text])
print(token.word_index)
# %%
x = token.texts_to_sequences([text])
print(x)
# %%
from keras.utils import to_categorical

# 인덱스 수에 하나를 추가해서 원-핫 인코딩 배열 만들기
word_size = len(token.word_index) + 1
print(word_size)

x= to_categorical(x,num_classes=word_size)
print(x)
# %%
