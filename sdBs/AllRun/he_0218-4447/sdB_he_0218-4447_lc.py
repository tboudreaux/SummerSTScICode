from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[35.101792,-44.557917], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_he_0218-4447/sdB_he_0218-4447_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
