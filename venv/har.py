import sys
sys.stdin.readline()

summad = set()
eelmised = []
for n in sys.stdin.readline().split():
    ulesannete_arv = int(n)
    summad.add(ulesannete_arv)
    uued_summad = [ulesannete_arv]
    for eelmine_summa in eelmised:
        summad.add(ulesannete_arv + eelmine_summa)
        uued_summad.append(ulesannete_arv + eelmine_summa)
    eelmised = uued_summad
for reas_lahendatud in sys.stdin.readline().split():
    if int(reas_lahendatud) in summad:
        print("JAH")
    else:
        print("EI")