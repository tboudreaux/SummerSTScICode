from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[18.555417,-25.071878], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_kuv_01118-2520/sdB_kuv_01118-2520_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
