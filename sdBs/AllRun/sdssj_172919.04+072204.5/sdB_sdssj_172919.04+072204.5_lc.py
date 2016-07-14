from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[262.329333,7.367917], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_sdssj_172919.04+072204.5/sdB_sdssj_172919.04+072204.5_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
