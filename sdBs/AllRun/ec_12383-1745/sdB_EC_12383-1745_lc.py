from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[190.254917,-18.032556], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_EC_12383-1745 /sdB_EC_12383-1745_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
