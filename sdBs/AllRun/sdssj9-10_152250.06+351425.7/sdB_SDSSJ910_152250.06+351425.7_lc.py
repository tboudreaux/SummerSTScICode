from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[230.708583,35.240472], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ910_152250.06+351425.7 /sdB_SDSSJ910_152250.06+351425.7_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
