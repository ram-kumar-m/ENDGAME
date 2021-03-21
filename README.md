# ENDGAME
## Python code from simple text

Well this has been a long time coming.

Let me take you on a step by step aproach to this problem.

Armed with a file with over 4600+ code examples.
I set out.

## Making the dataset

- Cleaning took, way maore time than expected and still a work in progress. Most of the syntax errors were fixed like prints without brackets etc.
- Used regex to seperate code from the questions (code description). Though comments fitted in new lines made that manually cumbersome to remove.
- Used autopep8 to import and fix each of the extracted code, also replacing 4 spaces with tabs.
- Though neither autopep8 nor black fixes multilevel indentation issue. Alot still had to be manually fixed. All tokenizer even I wrote couldnt fix it.

> All spaces, tabs, and newlines were left intentionally as python unlike english use spaces after every word. Allowing the model to figure it out.

>Only code < 251 chars long are used for training.
- All the cleaning and creation of csv for training can be found at [here](crc%20check.ipynb).

## Custom Embedding 

- The next big thing, glove embeddings were made using the original glove [repo](https://github.com/stanfordnlp/GloVe).
- First the corpus of python files in the lib directory of python3.8 [repo](https://github.com/python/cpython/tree/3.8/Lib).
- All white spaces and trailing charectors were converted into tokens in accordance with the input requirements of the glove package, as the package split tokens based on whitespaces.
- The lib corpus can be found as [lib_tokens.pkl](lib_tokens.pkl) which was formated with autopep8 and [lib_tokens1.pkl](lib_tokens1.pkl) which was formated using black for about 100 epochs
- An embedding dim of 256 was used for both, to match the code.
- The embeddings were imported, as per directions found [here](https://github.com/pytorch/text/issues/722#issuecomment-609880042)
- But the embeddings were found to make the predictions worse off.
- A look out for a new corpus was initiales with the view that all the files in the lib of python were a bit too complex for the simple problems found here.

- Simple repos for pythons gyms with leet code was identified and used, found [here](https://github.com/qiyuangong/leetcode) and [here](https://github.com/Garvit244/Leetcode)

- But even this prorduced worse predictions than without using custom embeddings.

>So for the moment all the pretrained embeddings were dropped.

## Better Loss
- Funnily enough I was at a loss, I tried NLLloss, KLDIVLOSS amongst others, still found cross entropy to be best.

## Inference 
- The model  works interesting well on simple functions and programs 
  for eg
  ```
  
    A good example of learning
    write a python program to find the total number of uppercase and lowercase letters in a given string

    -------------------------------------------- Given Solution --------------------------------------------

    str1 = 'TestStringInCamelCase'
    no_of_ucase, no_of_lcase = 0, 0
    for c in str1:
        if c >= 'A' and c <= 'Z':
        no_of_ucase += 1
        if c >= 'a' and c <= 'z':
        no_of_lcase += 1


    print(no_of_lcase)
    print(no_of_ucase)
    -------------------------------------------- Predicted Solution --------------------------------------------

    sentence = 'The Quick Brown Fox'
    lowercase = 0
    uppercase = 0
    for c in sentence:
        if c.isupper():
        uppercase += 1
        elif c.islower():
        lowercase += 1
        else:
        pass
    print(f'Lowercase: {lowercase}, Uppercase: {uppercase}')
  ```
- Even though there were many functions in the the training set with similar question, it corresctly figured out the most concise solution which works on the a python repl

- Simple functions are easily predicted
  ```
  36 . python funcction to find the factors of a number 

    -------------------------------------------- Given Solution --------------------------------------------
    def print_factors(x):
        print("The factors of", x, "are:")
        for i in range(1, x + 1):
        if x % i == 0:
            print(i)

    -------------------------------------------- Predicted Solution --------------------------------------------
    def print_factors(x):
        print("The factors of", x, "are:")
        for i in range(1, x + 1):
        if x % i == 0:
            print(i)
    ```
- Another interetsing case is this, where eventhough the given solution doesn't explicitly print the result. the network figured out that it needs to print using the other examples. 
 ```
 write a program to insert elemnet in the list after every nth element 

    -------------------------------------------- Given Solution --------------------------------------------


    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    i = 3
    while i < len(letters):
        letters.insert(i, 'x')
        i += 4


    letters

    -------------------------------------------- Predicted Solution --------------------------------------------


    letters = ['a', 'b', 'c', 'd', 'e']


    for i in range(len(letters)):
        letters.insert(i, 'x', i)

    letters, 'x', 'z':
        i += 1

    letters
    print(letters, 'x', 'x', i)
 ```

- or even this where the network, though the given solution, missed an indentation after an axcept satment the newtrok started figuring out an indentation level change was required after a semicolon.

```
----------------------------------------------------------------------------------------
write a python function to call a function repeatedly until an exception is raised . 

-------------------------------------------- Given Solution --------------------------------------------
def iter_except(func, exception, first=None):

	try:
	if first is not None:
        yield first()
	while True:
        yield func()
	except exception:
	pass

-------------------------------------------- Predicted Solution --------------------------------------------
def iter_except(func, exception, first=None):
	try:
	if first is None:
	yield func()
	def func():
	first()
	return True
	except exception:
except exception:
	pass
```

- Thought the network is far from perfect, and fails at complex soltuions, it learnings to predict the correct solutions pretty well. though wrong indedations errors here and there seem to thorw the model off here and there.
- But all in all the model looks pretty capable.

## Further 

- Right now the model is not that great when it comes to large fuctions or even class definitions.
- There is also some indendation errors in class problems that need to be fixed
- An idea that might be worth checking out is instaead of trying to copy pretrained embeddings. may be increasing the size of the dataset by using the leet code repos.
- As most of them also have class definitions