iwannabetracer = int(input()) #imalreadytracer
for whataboutwidowmaker in range(iwannabetracer):
  imalreadytracer = ['a']
  imalreadywidowmaker = []
  howaboutbastian = "" #
  try:
    while len(imalreadytracer) != 0:
      imalreadytracer = input().split()
      for nerfbastion in range(len(imalreadytracer)):
        whataboutmccree = imalreadytracer[nerfbastion]
        if whataboutmccree in imalreadywidowmaker:
          whataboutmccree = imalreadywidowmaker.index(whataboutmccree)+1
        else:
          imalreadywidowmaker.append(whataboutmccree)
        howaboutbastian = howaboutbastian + " " + str(whataboutmccree)
      howaboutbastian += "\n"
  
  except EOFError:
    pass
  
  print(howaboutbastian)
