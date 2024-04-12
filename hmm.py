# (a) Forward algorithm

op=input("Enter the sequence: ")


op=op.split()
op
n=len(op)

prob={'start':{'H':0.5,'L':0.5},'H':{'H':0.5,'L':0.5},'L':{'H':0.4,'L':0.6}}

prob_H={'A':0.2,'C':0.3,'G':0.3,'T':0.2}
prob_L={'A':0.3,'C':0.2,'G':0.2,'T':0.3}

prob_in_H=[]
prob_in_L=[]
prob_in_H.append(prob['start']['H']*prob_H[op[0]])
prob_in_L.append(prob['start']['L']*prob_L[op[0]])
print(prob_in_H)
print(prob_in_L)

for i in range(1,n):
  temp_H=(prob_in_H[i-1] * prob['H']['H'] * prob_H[op[i]]) + (prob_in_L[i-1] * prob['L']['H']*prob_H[op[i]])

  temp_L=(prob_in_H[i-1] * prob['H']['L'] * prob_L[op[i]]) + (prob_in_L[i-1] * prob['L']['L']*prob_L[op[i]])

  prob_in_H.append(temp_H)
  prob_in_L.append(temp_L)

print("Probability sequence in H state: ",prob_in_H)
print("Probabilty sequence in L state: ",prob_in_L)

total_prob=prob_in_H[n-1]+prob_in_L[n-1]
print("Probabilty that nodel generates this output is: ",total_prob)

# (b) Viterbi algorithm
# Pl(i,x) = el(i)* max[k] {Pk(j,x-1)*T(k,l)}

prob={'start':{'H':0.5,'L':0.5},'H':{'H':0.5,'L':0.5},'L':{'H':0.4,'L':0.6}}

prob_H={'A':0.2,'C':0.3,'G':0.3,'T':0.2}
prob_L={'A':0.3,'C':0.2,'G':0.2,'T':0.3}

prob_in_H=[]
prob_in_L=[]
prob_in_H.append(prob_H[op[0]]*prob['start']['H'])
prob_in_L.append(prob_L[op[0]]*prob['start']['L'])
for i in range(1,n):
  temp_H = prob_H[op[i]]* max(prob_in_H[i-1]*prob['H']['H'],prob_in_L[i-1]*prob['L']['H'])
  temp_L = prob_L[op[i]]* max(prob_in_H[i-1]*prob['H']['L'],prob_in_L[i-1]*prob['L']['L'])
  prob_in_H.append(temp_H)
  prob_in_L.append(temp_L)

print(prob_in_H)
print(prob_in_L)


final_seq=[]
for i in range(n):
  if(prob_in_H[i]>prob_in_L[i]):
    final_seq.append('H')
  else:
    final_seq.append('L')

print("The state sequence is: ",final_seq)

'''
#if given log probability
#here for the same state sequence "G G C A" in op
prob={'start':{'H':-1,'L':-1},'H':{'H':-1,'L':-1},'L':{'H':-1.322,'L':-0.737}}

prob_H={'A':-2.322,'C':-1.737,'G':-1.737,'T':-2.322}
prob_L={'A':-1.737,'C':-2.322,'G':-2.322,'T':-1.737}

prob_in_H=[]
prob_in_L=[]
prob_in_H.append(prob_H[op[0]]+prob['start']['H'])
prob_in_L.append(prob_L[op[0]]+prob['start']['L'])
for i in range(1,n):
  temp_H = prob_H[op[i]]+ max(prob_in_H[i-1]+prob['H']['H'],prob_in_L[i-1]+prob['L']['H'])
  temp_L = prob_L[op[i]]+ max(prob_in_H[i-1]+prob['H']['L'],prob_in_L[i-1]+prob['L']['L'])
  prob_in_H.append(temp_H)
  prob_in_L.append(temp_L)

'''
