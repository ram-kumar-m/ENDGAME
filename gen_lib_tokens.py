from tqdm.auto import tqdm
import glob, pickle

from tokenize_code import tokenizer_py
path = 'Lib/'
save_file = 'lib_tokens1.pkl'
tokens = []
files = glob.glob(path+'/**/*.py', recursive=True)

def do(file):
    global tokens
    try:        
        out = tokenizer_py(file=file)
        tokens += out
    except Exception as e:
        print(e, file)

pbar = tqdm(files)
for file in pbar:
    pbar.set_description(f'{file}')
    do(file)
    
with open(save_file, 'wb') as f:
    pickle.dump(tokens, f, protocol=4)
    
