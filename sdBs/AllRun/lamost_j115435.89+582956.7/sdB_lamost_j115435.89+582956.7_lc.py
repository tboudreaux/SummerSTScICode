from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[178.649542,58.499083], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_lamost_j115435.89+582956.7/sdB_lamost_j115435.89+582956.7_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
