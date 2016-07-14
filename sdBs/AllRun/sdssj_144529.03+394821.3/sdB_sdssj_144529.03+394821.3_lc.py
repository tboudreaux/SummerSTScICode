from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[221.370958,39.805917], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_sdssj_144529.03+394821.3/sdB_sdssj_144529.03+394821.3_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
