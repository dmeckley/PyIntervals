def main():
    lowSP = 1
    hiSP = 9
    setpoint = -5
    if lowSP < setpoint < hiSP:
        print('The setpoint', setpoint, 'is within the range of', lowSP, 'and', hiSP, sep=' ')
    else:
        print('The setpoint', setpoint, 'is outside the range of', lowSP, 'and', hiSP, sep=' ')
    

if __name__ == "__main__":
    main()