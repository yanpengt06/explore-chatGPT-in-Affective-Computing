from revChatGPT.V1 import Chatbot
import re


def annotate_a_dlg(dlg):
    chatbot = Chatbot(config={
        # "email": "yanpengt06@gmail.com",
        # "password": "t1234567"
        'session_token': 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..M0SaeW8ZPudxk-Wg.JCmJ_wrTpVZBtHJLwdc2nH6O2gReK_tJ5jQH_0wNeM6X6W-BZNadUpWPLgXAmuqWXg_ZWFOGd59B08V0gcVSj7CKcWKhqupn7xGmrfTuakNaddOcehk-eL5voLUBzPJGDcuOCw6mDcx3-MVK-sZybdn7G7dvBhZJzNHfbYc8c3OfvmrPP-2ZtjvRWmY-caDXXtrOmjeKFqQjKxHBdTqV-A07Osa7u7hXKeZ51rG_QU3ba-7FTxp4OkKu4lnHuYDoV5EwHkdNbD-_Tvjsx0q73XOFukROEWpMCK4d28GsFu8PEH05W2s-OMm6D5lNj5cMvqjpOaq946prJzXpx5CziHxkbANRn4GF7Bmo9CyKGkr-Ft7Y9jlHuVe-huOseIkwcrJ423TS_qXDhucaN5nDD6AehEHAIP6SwCu_C0yKcsLhms0TmXY_8tSPYNzkGVBUzg23jd_Xe1VroL_vSVer-VSzJZA3ME5waidevhUTFL7OGA_Y-H7F_zRw8Jd6XX3Je4aDXcnZvdW8V0_7CF2dlc3fZwoyyX4cWwYZPx4EnO0ydWD5Rwg77mU9Bp0mHBu7qRaJbtNfanOl7yWPLK1o5wbvTTQNJZ8fn0yehKdmGASwk9tj2q1XNFTShR4X3fGdTtPKZNuXo1r8pIvLhGDuZ1b83cylvpIrKBq_0SFmJ3pxqXzvdw9f6QXYZnoAOJuM_hy3VVMpvQajSScfeU3_nuT5xLvMFxcDZmFvS2nit68_dhH0bKdG5mTjzj-J-dcT0TdizjqpkD4Re4MAXV4Q8abCLz0jBvBMO614OtKZIUEMmSUcE5gv960b7WL1-n-PBBhP6PoqcUjW4N3lQgHxx1MLwxz0lhFs6OiXNNNbfWRbfQ2lx7CINcOvxJqQaVjp1xR_PARmExoi3dAhp3znlc8MBu8XIX5MB0y0CfExz-p-n2sjuaNTlcqJzfTcHE6qBBxJQltetSwXEiQxjbs0IhZxZg7wERnvv1kJdqlWln8x47ERcJngeVSBYUI-Lg49VbT3lJMRUQBBun6_2ZFwQ0KnTqCc0BOI7cwsblWTWX0I4U3EjaxQXGAXowiVCCjoORgw4Tpapokx_7daMBt0X9q3N9PJU980FMG4FelJszFMlU6aod4SSMiQTVprQuK8a37aSKgbGpxfJuHVQwFOzcA8_dbZGlxN5lUC2yUR0p9rvA7T6i_p2ko6Yynqmfqpb1KbI01AQy6ZmbOSPJrZNqRH-AB12Yae2vPiHra7q_u7_bQ62OknYxrv1h5iwThXYUvbbCtva9OO4BE9ArVniVSCu_gv5IVsj9dURAQh-0EZ35oyiv-kTP0idvq6Y3OP_Z6xf4mu-N9dPhUjNgEfk1Qg95nuHJtN0aZvnGW_jn6b0cUx0hmCCWZEOVGqM1V8VRqrq-smI2Q6SlYMmMb_ydSJlf6e8ff6Um3Qzq90MAC2dWV4JOzczgVaMQDmeMFdEaUrSndAZ_lVBn9oYZogGQlEvPqZtn0e9vN5G6JdnsTiqALDc9KWCzh4qJjC5HI0D9uERiRLIjxNeGjOaOjEqFhWiry0P8JrOSRJflhw-BSaHmSYb2NmQFHsJRqxWmIIAxGHkVpIQFbmxh4Mrb25yu6TIFUUwjgM7CUolTD-8rPyXwc2bhdkeIhkAxq_Q9ETxnwzf9eRI6VjpwDvpj9ywb4xSTbl-F_j_5u9w0LJ2FsJj7MwRn0IzTd58jamrIb87rF2HRmz1-1fycOLKf1aOnJJuUuZgWCdVlN0tM8gK_ghs4bo1N2-AWgZSZzqSfBSY5hXeUD9lCb-VVWJojA5it9deLEwyT-peu1ss1sBZcK5WEPcOwFt6V4z7RLi8Q99ijg5gwZ9R-1LqAVJEr7hzZzOTq9fytw95r9AKrwcg3QPteWnnakWTtYR9Xy8qT1TYtZDW1YXa0syqR37kmNvc5Wu8jbagyHyTqlFpe7AcdVHzC-L2BN6UGDixh1gCpv4PWeGmRVp_IPyj7vdfSn-_fnibCGMqyrEWMps2P3T5Nsc31ktcsw1P0r11YXSkf2I0b1Fjtor492tg858HrpuB09Eu1clFFH0Q7fTM9OB3SmEJPHaLQIv37fR7VQG8wQF72G8zLpfxsbkElFFAad6rZmVb6enM4CfCIZryfFGBQAkyFdhjR4dag1EZwuPE_9TGdL00yM6jsVGlAJfNCdYm9b1VS-J3hqUGilbTUH7LYMhLHKgGafAFJrQbgl1kW3X_ka4cX9l6FF9vd0iJ7L8G-ijA4tcEA61iNK2W7p2NeHXVynjhhLixpjjIkg2ZELl1rlHOE72GxXphG25MATYG12i2d2uE60lvkK9zURWI8Vrppfg_kMJPaQG_wTEuXrI-hXUfkC-vsN9G657oxLTn8NhoNF8ZUSSIRi525gh3BXxUmrpMjIvyVYJYVqO6ZYanDABkuMG_CpNAa7rcWQ7b-85vO0FFr3AZTWrtBKklM4llExJZvtFAO8Dq6EA7Yr3CDNXG5q2y2_R-wBDNObNu_Wsus-f._L8m6MjlLgRPpgfk2_cL8g'
    })

    template = '''Please mark an intention for each turn of the following conversation. The intention label can only come from the set {inform, question, directive, commissive}.The concepts of directive and commissive are as follows:
- Directive acts: These dialogue acts are used to direct or influence the behavior of the other participant. Examples of directive acts include making a request, giving an order, making a suggestion, or providing advice.
- Commissive acts: These dialogue acts commit the speaker to a future course of action. Examples of commissive acts include making a promise, offering to do something, or making a threat.
The annotation examples are as follows:
example1
---
A:Anything else , sir ? &question
B:That's all for now . How much do I owe you ? &question
A:That'll be fifty-five dollars and twenty cents .&inform
B:Can't you make it a little cheaper ? &directive
A:Oh , no , sir . We already gave you a discount on each item .&commissive
B:OK . I understand . Thank you .&inform
---
example2
---
A:Hello , can I speak to Mark Wyatt , please ?&directive
B:I am sorry . I can ’ t hear your very clearly . Could you say that again , please ?&directive
A:Does Mark Wyatt work there ?&question
B:Mark Wyatt ? I am sorry . The line is terrible.Could you spell that for me , please ?&directive
A:W-Y-A-T-T , Mark Wyatt .&inform
B:W-Y-A-T-T , Got it . I haven ’ t heard of the name.Could you hold on the line when I check .&directive
A:No problem .&commissive
---
example3
---
A:Room service , is there anything I can do for you ?&inform
B:Yes , I am afraid there are not enough outlets .&inform
A:Well , we have 6 for each room .&inform
B:Yes , but 4 of them are broken . Can you send someone here ?&directive
A:OK sir , please wait a minute .&commissive
---
Note: Annotations should be output in the format shown in the example without changing the content of the original text. Please annotate the following dialogue for me:
---
'''
    response = ""
    prompt = template + dlg
    print(prompt)
    for data in chatbot.ask(
            prompt
    ):
        # print(data)
        response = data["message"]
    return response


if __name__ == '__main__':
    results = []
    with open("./dd-parsed-k.txt", "r", encoding='utf-8') as f, open("./dd_act_chatGPT_few_shot_prpt_eng.txt", "a") as f2:
        dlgs = re.split('#\d+\n', f.read())[1:]
        for idx, dlg in enumerate(dlgs[56:]):
            result = annotate_a_dlg(dlg)
            print(f"{idx + 57}-th dialogue has been annotated!")
            print(result)
            print("-" * 60)
            f2.write(f"#{idx + 57}\n")
            f2.write(result + "\n")
