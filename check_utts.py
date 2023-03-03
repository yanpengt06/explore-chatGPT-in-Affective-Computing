import re

if __name__ == '__main__':
    target_len = []
    pred_len = []
    ignore_idx = []
    with open('dd-parsed-k-label.txt', 'r') as f1:
        lines = f1.read().split('\n')[:-1]
        for line in lines:
            labels = line.split(' ')[:-1]
            target_len.append(len(labels))
    with open('dd_act_chatGPT_few_shot_prpt_eng.txt','r') as f2:
        dlgs = re.split('#\d+\n', f2.read())[1:]
        for dlg in dlgs:
            utts = [utt for utt in dlg.split('\n') if utt != '']
            pred_len.append(len(utts))
    for idx, num in enumerate(pred_len):
        if num != target_len[idx]:
            ignore_idx.append(idx + 1)
    print(ignore_idx)