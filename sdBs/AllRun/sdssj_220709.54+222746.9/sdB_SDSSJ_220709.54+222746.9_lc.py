from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[331.78975,22.463028], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ_220709.54+222746.9 /sdB_SDSSJ_220709.54+222746.9_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
