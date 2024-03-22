# Define the triangle coordinates
PM = [159, 191, 223]
PS = [127, 159, 191]

PM_membership = 0.15625
PS_membership = 0.15625

x = np.linspace(100, 250, 1000)


a, b, c = PM
PM_y = np.maximum(0, np.minimum((x - PM[0]) / (PM[1] - PM[0]), (PM[2] - x) / (PM[2] - PM[1])))
a, b, c = PS
PS_y = np.maximum(0, np.minimum((x - PS[0]) / (PS[1] - PS[0]), (PS[2] - x) / (PS[2] - PS[1])))

# Calculate the centroid of sums
centroid_of_sums = (sum(x * PM_y) + sum(x * PS_y)) / (sum(PM_y) + sum(PS_y))

plt.figure(figsize=(10, 6))
plt.plot(x, PM_y, label='PM')
plt.axhline(y=0.15625, color='b', linestyle='--', label='Intersection Membership Value')
plt.plot(x, PS_y, label='PS')

plt.axvline(x=centroid_of_sums, color='red', linestyle='--', label='Centroid of Sums')

plt.scatter([centroid_of_sums], [0.15625], color='green', label='Intersection')

plt.xlabel('Throttle')
plt.ylabel('Membership')
plt.title('Fuzzy Speed Sets')
plt.legend()
plt.grid(True)
plt.show()

print("Defuzzified value (centroid of sums):", centroid_of_sums)
