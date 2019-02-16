#Smoke weed everday
smoke = input()
score = []
scor = []
for i in range(4):
  DUX = list(map(float,input().split()))
  score.append(DUX[0]/DUX[1]*DUX[2]*100)
  scor.append(100*DUX[2])
if smoke == "trees!":
  score[score.index(max(score))] = scor[score.index(max(score))]
else:
  score[0] = 0
if sum(score) - round(sum(score)) == 0.5:
  print((round(sum(score)+0.1)))
else:
  print(round(sum(score)))
