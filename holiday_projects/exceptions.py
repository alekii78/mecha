def mydiv(items, beneficiaries):
        share = 0
        try:
            assert (items > beneficiaries), "Items to be shared are less"
            share = items / beneficiaries
        except AssertionError:
            print("Items to be shared are less.", end='\t')
        else:
            print("Shared Successfully.", end='\t')
        return share
print("Share = ", mydiv(20, 4))
print("Share = ", mydiv(4, 10))
print("Share = ", mydiv(9, 4))
print("Share = ", mydiv(7, 1))
print("Share = ", mydiv(12, 3))
