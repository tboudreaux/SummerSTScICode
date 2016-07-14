from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[146.995458,9.170083], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_sdssj_094758.91+091012.3/sdB_sdssj_094758.91+091012.3_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
