from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[0.3845,-5.321319], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_bps_cs22957-23/sdB_bps_cs22957-23_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
