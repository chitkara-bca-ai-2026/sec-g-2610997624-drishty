a = int(input("Enter Tution Fee:"))
b = int(input("Enter Lab Fee:"))
c = int(input("Enter Library Fee:"))
d = int(input("Enter Exam Fee:"))
e = int(input("Enter Discount Amount:"))
total = a+b+c+d
dis = a+b+c+d-e
annual = 2*dis
monthly = annual/12
print(f"Tution Fee:{a:.1f}")
print(f"Lab Fee:{b:.1f}")
print(f"Library Fee:{c:.1f}")
print(f"Exam Fee:{d:.1f}")
print(f"Total Fee:{total:.1f}")
print(f"Discount:{e:.1f}")
print(f"Fee After Discount:{dis:.1f}")
print(f"Annual Fee:{annual:.1f}")
print(f"Monthly Installment:{monthly:.1f}")