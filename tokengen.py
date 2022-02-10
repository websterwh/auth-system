import uuid
text = uuid.uuid4()
count = 100
f = open('tokens.txt', 'w')
while (count > 0):
    text = uuid.uuid4()
    count = count - 1
    f.write('\n')
    f.write(str(text))