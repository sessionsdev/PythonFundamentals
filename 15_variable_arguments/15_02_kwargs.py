'''
Write a script with a function that demonstrates the use of **kwargs.

'''

def dog(**kwargs):
    print(kwargs)

dog(name='James', breed='Yorki', age=5, color='brown')