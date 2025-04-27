def calc(tp, tn, fp, fn):
    true_total = tp + fn
    false_total = fp + tn

    tp_percentage = (tp / true_total) * 100
    tn_percentage = (tn / false_total) * 100
    fp_percentage = (fp / false_total) * 100
    fn_percentage = (fn / true_total) * 100

    print(f"True Positives: {tp_percentage:.2f}%")
    print(f"True Negatives: {tn_percentage:.2f}%")
    print(f"False Positives: {fp_percentage:.2f}%")
    print(f"False Negatives: {fn_percentage:.2f}%")

print("Random Forest")
calc(563, 8554, 242, 588)
print("\nLog Reg")
calc(1288, 9788, 3434, 430)