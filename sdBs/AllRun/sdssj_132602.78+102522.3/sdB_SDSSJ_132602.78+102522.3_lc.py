from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[201.511583,10.422861], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ_132602.78+102522.3 /sdB_SDSSJ_132602.78+102522.3_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
