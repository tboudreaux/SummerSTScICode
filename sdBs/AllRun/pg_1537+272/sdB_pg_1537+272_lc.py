from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[234.909167,27.101783], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_pg_1537+272/sdB_pg_1537+272_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
