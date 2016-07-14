from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[217.2635,11.926222], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ910_142903.24+115534.4 /sdB_SDSSJ910_142903.24+115534.4_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
