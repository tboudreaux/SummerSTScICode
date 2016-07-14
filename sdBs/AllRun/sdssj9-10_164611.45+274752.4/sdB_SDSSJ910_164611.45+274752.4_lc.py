from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[251.547708,27.797889], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ910_164611.45+274752.4 /sdB_SDSSJ910_164611.45+274752.4_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()