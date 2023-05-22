path = "/dls_sw/prod/R3.14.12.7/ioc/SR01C/VA/5-5/bin/vxWorks-ppc604_long/stSR01C-VA-IOC-01.boot"
print(path)
iocRelease = "5-5"
path = path.replace("prod","work")
path = path.replace(f"/{iocRelease}","")
#pathToReleaseNumber = path.split("/bin")[0]
#prodRelease = pathToReleaseNumber.split("/")[-1]
print(path)
