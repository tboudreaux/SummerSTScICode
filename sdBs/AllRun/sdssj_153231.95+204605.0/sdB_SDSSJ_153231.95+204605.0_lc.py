from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[233.133125,20.768056], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ_153231.95+204605.0 /sdB_SDSSJ_153231.95+204605.0_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
