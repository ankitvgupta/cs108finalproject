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
    - Run `python model_test.py <tweet_file> <K>`, where `<tweet_file>` is the relative path to a file in the data folder (for example, ../data/Harvard.csv), and `K` designates how big your K-mer will be. K must be at least 2.

# Important files
- [main.py](src/main.py): Contains code to generate sentences given a list of Twitter handles at the command line.
- [model_generator.py](src/model_generator.py): Contains functions to generate the Markov model for a user. This includes getting tweets from a file, extracting K-mers, forming the model, and determining next words given the current K-1 words.
- [model_test.py](src/model_test.py): Contains functions generate sentences from a model, and test their similarity to the original tweets. Note that when run as driver program, this file will default to determining sentence accuracy.
- [twitter_extractor.py](src/twitter_extractor.py): Contains functions to connect to Twitter API and extract tweets for user or users.
- [comparison.py](src/comparison.py): Contains functions to compare words/sentences for quantitative analysis.

# Dependencies
[numpy](http://www.numpy.org), [scipy](http://scipy.org), [Tweepy](http://www.tweepy.org), [NLTK](http://www.nltk.org)

