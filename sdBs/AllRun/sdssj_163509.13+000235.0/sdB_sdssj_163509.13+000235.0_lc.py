from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[248.788042,0.043056], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_sdssj_163509.13+000235.0/sdB_sdssj_163509.13+000235.0_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
