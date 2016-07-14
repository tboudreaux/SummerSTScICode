from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[253.480958,13.212306], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ_165355.43+131244.3 /sdB_SDSSJ_165355.43+131244.3_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
