from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[309.699542,14.952083], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ_203847.89+145707.5 /sdB_SDSSJ_203847.89+145707.5_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
