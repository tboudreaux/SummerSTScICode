from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[246.563417,11.834306], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_sdssj9-10_162615.22+115003.5/sdB_sdssj9-10_162615.22+115003.5_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
