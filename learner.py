from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict


class Learner:
    def __init__(self, ignore_singletons=False):
        self.classes = set()
        self.word_counters = dict()
        self.word_probs = defaultdict(lambda: 0)
        self.ignore_singletons = ignore_singletons

    def lex(input_text) -> list:
        stop_words = set(stopwords.words('english'))
        return [
            w for w in word_tokenize(
                input_text.lower()) if w not in stop_words]

    def train(self, records):
        self.update_word_counters(records)
        self.update_word_probs()

    def extract_features(lexed_input, ns=(1, 2, 3), skip_grams=False) -> set:
        result = []
        if not skip_grams:
            for n in ns:
                for i in range(len(lexed_input)):
                    result.append(tuple(lexed_input[i:i + n]))
        else:
            for n in ns:
                for index, item in enumerate(lexed_input):
                    try:
                        result.append((item, lexed_input[index + n]))
                    except IndexError:
                        pass
        return set(result)

    def lex_and_parse(self, text):
        return Learner.extract_features(Learner.lex(text))

    def update_word_counters(self, records):    
        self.classes.update({r[0] for r in records})
        for r in records:
            for word_tuple in self.lex_and_parse(r[1]):
                if word_tuple not in self.word_counters:
                    self.word_counters[word_tuple] = defaultdict(lambda: 0)
                counter_for_tuple = self.word_counters[word_tuple]
                counter_for_tuple.update({r[0]: counter_for_tuple[r[0]] + 1})
        # self.word_counters = {
        #     k: v for k, v in self.word_counters.items() if sum(v.values()) > 1}
        return

    def update_word_probs(self):
        # for words, counter in word_sender_counter.items():
        #     s = sum(counter.values())
        #     for k, v in counter.items():
        #         counter[k] = v / s
        self.word_probs = defaultdict(lambda: 0)
        if self.ignore_singletons:
            filtered_word_counters = {k: v for k, v in self.word_counters.items() if sum(v.values()) > 1}
            self.word_probs.update(filtered_word_counters)
        else:
            self.word_probs.update(self.word_counters)
        return

    def classify(self, text):
        prob_map = {k: [0] for k in self.classes}
        words = self.lex_and_parse(text)
        for w in words:
            if w in self.word_probs:
                for k, v in self.word_probs[w].items():
                    prob_map[k].append(v)
        results = defaultdict(lambda: 0)
        for k, v in prob_map.items():
            prod = 1
            for x in v:
                prod *= x + 1
            results[k] = prod
        sorted_classes = sorted(
            results.items(),
            key=lambda t: t[1],
            reverse=True)
        return sorted_classes[0]

    def test(self, test_data):
        count = 0
        for test in test_data:
            if self.classify(test[1])[0] == test[0]:
                count += 1
        return count / len(test_data)
