from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[18.439167,17.980292], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_PG_0111+177 /sdB_PG_0111+177_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()