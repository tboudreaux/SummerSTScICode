from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[129.562375,69.713433], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_pg_0833+699/sdB_pg_0833+699_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
