from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[258.973292,43.098694], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ910_171553.59+430555.3 /sdB_SDSSJ910_171553.59+430555.3_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
