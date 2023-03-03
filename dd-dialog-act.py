import random
import re


def sample_k_dd(k=64):
    with open('./dailydialog/dialogues_text.txt', 'r', encoding='utf-8') as f:
        dlgs = f.read().split('\n')
        dlgs = dlgs[:-1]
    result = []
    chosen = []
    for dlg in dlgs:
        utts = dlg.split('__eou__')
        utts = [utt.strip() for utt in utts if utt != '']
        utts_apd = []
        for idx, utt in enumerate(utts):
            if idx % 2 == 0:
                utts_apd.append('A:' + utt)
            else:
                utts_apd.append('B:' + utt)
        result.append(utts_apd)
    idxs = random.sample(range(len(result)), k)
    for idx in idxs:
        chosen.append(result[idx])
    return chosen, idxs


if __name__ == '__main__':
    result, idxs = sample_k_dd()
    print(idxs)
    with open('dd-parsed-k.txt', 'w', encoding='utf-8') as f:
        for idx, dlg in enumerate(result):
            f.write(f'#{idx + 1}\n')
            for utt in dlg:
                f.write(utt + '\n')
    # get the act labels
    with open('./dailydialog/dialogues_act.txt', 'r') as f1:
        labels = f1.read().split('\n')[:-1]
    with open('dd-parsed-k-label.txt', 'w') as f2:
        for idx in idxs:
            f2.write(labels[idx] + '\n')

