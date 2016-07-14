from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[194.526583,24.101278], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ910_125806.38+240604.6 /sdB_SDSSJ910_125806.38+240604.6_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
