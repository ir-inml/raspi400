import random
a = ['ぐぅ','ちょき','ぱぁ']
b = ['ちょき','ぱぁ','ぐぅ']
c = input("じゃんけんをします。")
while(c not in a):
    c = input("入力ミスです。")
com = random.choice(a)

print(f"あなたの手 {c} コンピューターの手 {com}")

if c == com:
    print("引き分けです。")
elif a.index(c) == b.index(com):
    print("あなたの勝ちです。")
else:
    print("あなたの負けです。")