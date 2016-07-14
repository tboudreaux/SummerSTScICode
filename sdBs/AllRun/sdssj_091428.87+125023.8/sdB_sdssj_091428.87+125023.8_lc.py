from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[138.620292,12.839944], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_sdssj_091428.87+125023.8/sdB_sdssj_091428.87+125023.8_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
