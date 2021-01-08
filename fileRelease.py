import fileinput

commonRelease = "include /dls_sw/prod/R3.14.12.7/support/feMasterConfig/1-0/configure/FE_COMMON_RELEASE"
archRelease = "include /dls_sw/prod/R3.14.12.7/support/feMasterConfig/1-0/configure/FE_LINUX_RELEASE"

for line in fileinput.input("RELEASE",inplace=True):
    if "FE_COMMON" in line:
        print('{}'.format(commonRelease), end='\n')
    elif "FE_LINUX" in line or "FE_VXWORKS" in line:
        print('{}'.format(archRelease), end='\n')
    else:
        print('{}'.format(line), end='')
