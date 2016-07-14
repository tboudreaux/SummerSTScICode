from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[227.208875,0.902222], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ910_J150850.13+005408.0 /sdB_SDSSJ910_J150850.13+005408.0_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()