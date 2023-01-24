#Question9
#User inputs
N=int(input("Input the students count: "))
w_list=[]
print("Enter the {} students weights: ".format(N))
#looping
for a in range(0,N):
    wei_lbs=int(input())
    w_list.append(wei_lbs)
print("Weights of {} students(LBS):{} ".format(N, w_list))
#Kgs Conversion
wei_kgs= [round(x*0.453592,2) for x in w_list]
print("Weights of {} students(KGS):{} ".format(N, wei_kgs))