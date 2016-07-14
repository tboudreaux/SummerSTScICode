from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[189.348,25.066639], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_pg_1234+253/sdB_pg_1234+253_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
