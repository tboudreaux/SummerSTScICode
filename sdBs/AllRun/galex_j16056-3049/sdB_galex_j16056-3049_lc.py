from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[241.400625,-30.820922], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_galex_j16056-3049/sdB_galex_j16056-3049_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
