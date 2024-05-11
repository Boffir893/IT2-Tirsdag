

def er_primtall(tall):
    for i in range(tall):
        if tall % i == 0:
            return True
        else:
            return False
        break
