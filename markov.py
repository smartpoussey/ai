import matplotlib.pyplot as plt
import pandas as pd

# U(s)=R(s) + (  discount * max[s']{ T(s,a,s')*U(s') }  )

#define the R(s)->current reward of each state
sun_reward=4
wind_reward=0
hail_reward=-8

dis_sun=[sun_reward]
dis_wind=[wind_reward]
dis_hail=[hail_reward]


prob={'sun':{'sun':1/2,'wind':0},'wind':{'sun':1/2,'hail':1/2},'hail':{'hail':1/2,'wind':1/2}}
#print(prob['sun']['sun'])

#number of iterations
n=5

#discounted factor
discount=0.5

for i in range(1,n+1):
  temp_sun=sun_reward+(discount * max(prob['sun']['sun']*dis_sun[i-1],prob['sun']['wind']*dis_wind[i-1]))
  temp_wind=wind_reward+(discount * max(prob['wind']['sun']*dis_sun[i-1],prob['wind']['hail']*dis_hail[i-1]))
  temp_hail=hail_reward+(discount * max(prob['hail']['hail']*dis_hail[i-1],prob['hail']['wind']*dis_wind[i-1]))

  dis_sun.append(temp_sun)
  dis_wind.append(temp_wind)
  dis_hail.append(temp_hail)

print("Discounted Rewards for sun:",dis_sun)
print("Discounted Rewards for Wind:",dis_wind)
print("Discounted Rewards for Hail:",dis_hail)
