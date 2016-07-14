from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[15.323167,-33.712608], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_ton_s183/sdB_ton_s183_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
