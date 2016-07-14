from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[341.646792,30.803583], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_sdssj_224635.23+304812.9/sdB_sdssj_224635.23+304812.9_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()