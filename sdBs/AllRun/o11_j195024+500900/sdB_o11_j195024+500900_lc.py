from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[297.6,50.15], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_o11_j195024+500900/sdB_o11_j195024+500900_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
