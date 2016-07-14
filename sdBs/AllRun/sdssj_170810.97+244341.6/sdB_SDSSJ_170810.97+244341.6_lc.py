from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[257.045708,24.728222], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ_170810.97+244341.6 /sdB_SDSSJ_170810.97+244341.6_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
