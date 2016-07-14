from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[119.556792,20.884028], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_sdssj_075813.63+205302.5/sdB_sdssj_075813.63+205302.5_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
