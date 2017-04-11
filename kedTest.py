import math

U_A = -320
U_B = 580
a = 0.03
b = 0.045
d = 0.48
EPSILON = 8.854187817e-12
N = 10

qa = []
qb= []
sa =[]
sb = []


qa0 = a * U_A
qb0 = b * U_B

sa0 = 0
sb0 = 0

qa.append(qa0)
qb.append(qb0)
sa.append(sa0)
sb.append(sb0)


def compute(i):
    qa_new = -(a*qb[i-1]/(d-sb[i-1]))
    qb_new = -(b*qa[i-1]/(d-sa[i-1]))
    sa_new = (a*a)/(d-sb[i-1])
    sb_new = (b*b)/(d-sa[i-1])

    qa.append(qa_new)
    qb.append(qb_new)
    sa.append(sa_new)
    sb.append(sb_new)

def Main():
    for i in range(1,N):
        compute(i)

    qa_sum = 0
    qb_sum = 0
    sa_sum = 0
    sb_sum = 0

    for i in range (0,N):
        qa_sum += qa[i]
        qb_sum += qb[i]
        sa_sum += sa[i]
        sb_sum += sb[i]

    q_total = (4 * math.pi * EPSILON*(qa_sum + qb_sum))
    print("qa sum is ", qa_sum, "qb_sum is ", qb_sum)
    print("the total electric charge is ", q_total)
Main()