from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[120.208208,12.937333], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ910_080049.97+125614.4 /sdB_SDSSJ910_080049.97+125614.4_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
