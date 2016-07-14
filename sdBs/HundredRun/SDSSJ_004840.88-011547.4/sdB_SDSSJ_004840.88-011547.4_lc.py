from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[182.554995,-1.263167], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ_004840.88-011547.4 /sdB_SDSSJ_004840.88-011547.4_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()