# Load master_2009.json through master_2018.json, analyze the tweets, and make a bar chart.
# Follow the linked course assignment in README.md.
import json
import matplotlib.pyplot as plt

def load_tweets():
    tweets = []
    for year in range(2009, 2019):
        with open(f'master_{year}.json', encoding='utf-8') as f:
            tweets.extend(json.load(f))
    return tweets


def count_phrase(tweets, phrase):
    count = 0
    phrase = phrase.lower()
    for tweet in tweets:
        if 'full_text' in tweet:
            tweet_text = tweet['full_text']
        else:
            tweet_text = tweet['text']
        tweet_text = tweet_text.lower()

        if phrase in tweet_text:
            count += 1
    return count

def count_list (tweets, plist):
    counts = {}
    for phrase in plist:
        counts[phrase] = count_phrase(tweets, phrase)
    return counts

tweets = load_tweets()
print ('Total Tweets:', len(tweets))

plist = ['Obama', 'Trump', 'Mexico', 'Russia', 'Fake News', 'wall', 'jobs', 'MAGA']
counts = count_list(tweets, plist)
print(counts)

sum = 0
for phrase in plist:
    sum += counts[phrase]

percentage = {}
for phrase in plist:
    percentage[phrase] = (counts[phrase] / sum)*100

print(f'| {"Phrase":<12} | {"Percent of Tweets":>} |')
print(f'|{"-"*14}|{"-"*19}|')
for phrase, n in counts.items():
    print(f'| {phrase:>12} | {percentage[phrase]:<17.2f} |')

def make_bar_chart(counts, filename='phrase_counts.png'):
    plt.figure(figsize=(10, 5))
    plt.bar(list(plist), [percentage[phrase] for phrase in plist])
    plt.xlabel('Phrase')
    plt.ylabel('Percent of Tweets')
    plt.title('Tweets containing each phrase')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()

make_bar_chart(counts)


