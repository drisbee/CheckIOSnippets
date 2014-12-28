def checkio(text):
    text = text.lower()
    answer = dict()
    largestvalue = None
    for x in text:
        if x.isalpha():
            answer[x] = answer.get(x, 0) + 1

    return min(answer.items(), key=lambda aantal: (-aantal[1],
                                                     aantal[0]))[0]


print checkio("hello")

