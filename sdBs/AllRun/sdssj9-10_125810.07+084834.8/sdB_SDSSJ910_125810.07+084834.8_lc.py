from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[194.541958,8.809667], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ910_125810.07+084834.8 /sdB_SDSSJ910_125810.07+084834.8_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
