from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[231.392292,9.980833], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ_152534.15+095851.0 /sdB_SDSSJ_152534.15+095851.0_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
