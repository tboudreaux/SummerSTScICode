from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[214.587167,-3.381692], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_HE_1415-0309 /sdB_HE_1415-0309_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
