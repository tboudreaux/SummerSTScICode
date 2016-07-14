from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[124.880083,14.465611], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_sdssj_081931.22+142756.2/sdB_sdssj_081931.22+142756.2_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
