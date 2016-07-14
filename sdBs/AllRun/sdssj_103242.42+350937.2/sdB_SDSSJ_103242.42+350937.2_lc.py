from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[158.17675,35.160333], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ_103242.42+350937.2 /sdB_SDSSJ_103242.42+350937.2_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()