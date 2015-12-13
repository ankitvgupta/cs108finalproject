This directory is for experimental parts of the project. Various attempts at querying data, text processing, etc, will occur here.

# Usage
1. Get Twitter API keys.
    - Create a file called APIKeys.json, and store your API keys in there. You can use [APIkeyexample.txt](data/APIkeyexample.txt) as a reference.
    - Note that this .json will not be pushed to git, unless you change the .gitignore.
2. Generate tweets for a user or set of users
    - Navigate to the `src` directory
    - Run `python main.py --names <NAME1> <NAME2> ...` where each of the `NAMEi` can be replaced with a twitter handle.
    - The code will pull tweets and save them to the `data` directory
3. Determine sentence similarity
    - Navigate to the `src` directory
    - Run `python model_test.py <tweet_file> <K>`, where `<tweet_file>` is the relative path to a file in the data folder (for example, ../data/Harvard.csv), and `K` designates how big your K-mer will be.

# Important files
- [main.py](src/main.py)
- [model_generator.py](src/model_generator.py)
- [model_test.py](src/model_test.py)
- [twitter_extractor.py](src/twitter_extractor.py)
- [comparison.py](src/comparison.py)

# Dependencies
numpy, scipy, tweepy

