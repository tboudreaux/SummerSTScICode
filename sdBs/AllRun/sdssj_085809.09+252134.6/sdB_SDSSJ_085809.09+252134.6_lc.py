from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[134.537875,25.359611], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ_085809.09+252134.6 /sdB_SDSSJ_085809.09+252134.6_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
