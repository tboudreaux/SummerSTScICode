from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[32.189333,-8.016581], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_kuv_02063-0815/sdB_kuv_02063-0815_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
