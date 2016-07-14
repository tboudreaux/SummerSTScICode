from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[17.666875,-1.015972], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ_011040.05-010057.5 /sdB_SDSSJ_011040.05-010057.5_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
