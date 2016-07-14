from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[277.8725,64.563056], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_kuv_18312+6431/sdB_kuv_18312+6431_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()