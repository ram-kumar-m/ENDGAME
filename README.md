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

