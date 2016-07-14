from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[342.209542,10.545556], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_pg_2246+103/sdB_pg_2246+103_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
