from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[149.055,-3.002556], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ910_095613.20-030009.2 /sdB_SDSSJ910_095613.20-030009.2_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
