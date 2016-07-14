from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[156.27525,12.006194], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_sdssj_102506.06+120022.3/sdB_sdssj_102506.06+120022.3_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()