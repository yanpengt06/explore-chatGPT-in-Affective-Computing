from sklearn.metrics import classification_report

ignore_idx = [5, 6, 8, 9, 10, 16, 25, 27, 29, 31, 34, 43, 45, 48, 49, 61]

if __name__ == '__main__':
    labels = []
    targets = []
    with open('dd_act_chatgpt_label__few_shot_prpt_eng.txt', 'r') as f1:
        lines = f1.read().split('\n')[:-1]
        for line in lines:
            if line != '':
                labels += [int(label) for label in line.split(' ')[:-1]]
    with open('dd-parsed-k-label.txt', 'r') as f2:
        lines = f2.read().split('\n')[:-1]
        for idx, line in enumerate(lines):
            if idx + 1 in ignore_idx:
                continue
            else:
                targets += [int(label) for label in line.split(' ')[:-1]]
    print(len(labels))
    print(len(targets))
    print(classification_report(targets, labels))