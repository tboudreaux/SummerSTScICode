from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[53.029833,4.310283], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_kuv_03295+0408/sdB_kuv_03295+0408_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
