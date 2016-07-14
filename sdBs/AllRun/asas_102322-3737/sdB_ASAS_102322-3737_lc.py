from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[155.84125,-37.616667], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_ASAS_102322-3737 /sdB_ASAS_102322-3737_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
